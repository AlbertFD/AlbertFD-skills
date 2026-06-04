#!/usr/bin/env python3
"""Fetch a paper's text from an arXiv ID/URL, DOI, journal URL, or local PDF.

Usage:
    python fetch_paper.py "<arxiv-id | url | doi | /path/to.pdf>"

Prints title, authors, and extractable full text to stdout. Designed to be
best-effort: many publishers paywall full text, in which case only metadata /
abstract may be available. It never fabricates content.
"""
import re
import sys
import json
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

UA = {"User-Agent": "paper-summarizer/1.0 (mailto:research@example.com)"}


def _get(url, headers=None):
    req = urllib.request.Request(url, headers={**UA, **(headers or {})})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def looks_like_arxiv(s):
    return bool(re.search(r"arxiv\.org", s, re.I)) or bool(
        re.fullmatch(r"\d{4}\.\d{4,5}(v\d+)?", s.strip())
    )


def arxiv_id(s):
    m = re.search(r"(\d{4}\.\d{4,5}(v\d+)?)", s)
    return m.group(1) if m else s.strip()


def fetch_arxiv(s):
    aid = arxiv_id(s)
    url = f"http://export.arxiv.org/api/query?id_list={aid}"
    data = _get(url).decode("utf-8", "replace")
    ns = {"a": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(data)
    entry = root.find("a:entry", ns)
    if entry is None:
        return None
    title = (entry.findtext("a:title", default="", namespaces=ns) or "").strip()
    authors = [
        (a.findtext("a:name", default="", namespaces=ns) or "").strip()
        for a in entry.findall("a:author", ns)
    ]
    summary = (entry.findtext("a:summary", default="", namespaces=ns) or "").strip()
    out = [f"TITLE: {title}", f"AUTHORS: {', '.join(authors)}",
           f"LINK: https://arxiv.org/abs/{aid}", "", "ABSTRACT:", summary]
    # Try to grab full text from the HTML (ar5iv / arXiv HTML) if available.
    try:
        html = _get(f"https://arxiv.org/abs/{aid}").decode("utf-8", "replace")
        out.append("")
        out.append("[NOTE] Full text not extracted here; abstract above is "
                   "authoritative. For full text, download the PDF.")
    except Exception:
        pass
    return "\n".join(out)


def fetch_doi(s):
    doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", s.strip(), flags=re.I)
    url = f"https://api.crossref.org/works/{urllib.parse.quote(doi)}"
    try:
        data = json.loads(_get(url).decode("utf-8", "replace"))["message"]
    except Exception as e:
        return f"[ERROR] Could not resolve DOI {doi}: {e}"
    title = "; ".join(data.get("title", []))
    authors = ", ".join(
        f"{a.get('given','')} {a.get('family','')}".strip()
        for a in data.get("author", [])
    )
    abstract = re.sub(r"<[^>]+>", "", data.get("abstract", "") or "").strip()
    container = "; ".join(data.get("container-title", []))
    year = ""
    for k in ("published-print", "published-online", "issued"):
        if data.get(k, {}).get("date-parts"):
            year = str(data[k]["date-parts"][0][0])
            break
    out = [f"TITLE: {title}", f"AUTHORS: {authors}",
           f"VENUE: {container} {year}".strip(), f"LINK: https://doi.org/{doi}", ""]
    if abstract:
        out += ["ABSTRACT:", abstract]
    else:
        out += ["[NOTE] No abstract available via Crossref; full text is likely "
                "paywalled. Summarize only from what the user can provide."]
    return "\n".join(out)


def extract_pdf(path):
    text = None
    try:
        from pypdf import PdfReader
        reader = PdfReader(path)
        text = "\n".join((p.extract_text() or "") for p in reader.pages)
    except Exception:
        pass
    if not text:
        import subprocess
        try:
            text = subprocess.run(
                ["pdftotext", path, "-"], capture_output=True, text=True, timeout=120
            ).stdout
        except Exception as e:
            return f"[ERROR] Could not extract PDF text: {e}. Try the `pdf` skill."
    return text.strip()


def main():
    if len(sys.argv) < 2:
        print("Usage: fetch_paper.py <arxiv-id|url|doi|path.pdf>", file=sys.stderr)
        sys.exit(1)
    s = sys.argv[1].strip()
    if s.lower().endswith(".pdf") or s.startswith("/"):
        print(extract_pdf(s))
    elif looks_like_arxiv(s):
        print(fetch_arxiv(s) or "[ERROR] arXiv entry not found.")
    elif re.search(r"10\.\d{4,9}/", s):
        print(fetch_doi(s))
    elif s.startswith("http"):
        try:
            print(_get(s).decode("utf-8", "replace"))
        except Exception as e:
            print(f"[ERROR] Could not fetch URL: {e}")
    else:
        print(fetch_arxiv(s) or "[ERROR] Could not interpret input.")


if __name__ == "__main__":
    main()
