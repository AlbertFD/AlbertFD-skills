#!/usr/bin/env bash
# Repackage skill source folders into installable .skill files under build/.
# Usage: ./build.sh [skill-name ...]   (no args = build all skills)
set -euo pipefail

cd "$(dirname "$0")"
mkdir -p build

# Skills to build: args if given, else every dir containing a SKILL.md.
if [ "$#" -gt 0 ]; then
  skills=("$@")
else
  skills=()
  for d in */; do
    [ -f "${d}SKILL.md" ] && skills+=("${d%/}")
  done
fi

for skill in "${skills[@]}"; do
  if [ ! -f "${skill}/SKILL.md" ]; then
    echo "skip: ${skill} (no SKILL.md)" >&2
    continue
  fi
  out="build/${skill}.skill"
  rm -f "$out"
  # Zip the folder (top-level dir preserved), excluding junk.
  zip -rq "$out" "$skill" -x '*.DS_Store' '*/__pycache__/*' '*.pyc'
  echo "built: $out"
done
