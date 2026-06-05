# Understanding Map: Eigenvectors

*you · 2026-06-05 · subject: linear algebra*

## What you already understand
These pieces are correct and load-bearing — the lesson was built directly on them:

- You can compute \(Av\) (row-times-column) without trouble.
- You can run the determinant route, \(\det(A-\lambda I)=0\), to find eigenvalues.
- You read a vector \((x, y)\) correctly as "x along, y up" — the coordinate idea is solid.

You came in further along than it felt.

## The gap we found
**Type: brittle procedure / missing geometric model.**

You were experiencing a matrix as a *rule that grinds out a new vector*, not as a
*transformation that picks up the whole plane and moves it* (stretch, rotate, shear,
flip). That's why eigenvectors felt hollow: "a direction the matrix doesn't knock
off its line" is meaningless until you can see the plane being deformed in the first
place. The symptom — "I can compute them but don't know what they *are*" — is exactly
what a working procedure sitting on a missing picture feels like.

## The lesson
A matrix is a transformation of space. Multiplying by \(A\) moves every point at
once. Once you see that, the definition reads in plain English:

$$A v = \lambda v \;\;\Longrightarrow\;\;
\text{"}A \text{ moves the whole plane, but } v \text{ isn't turned off its line — only scaled by } \lambda\text{."}$$

Eigenvectors are the special directions a transformation leaves on their own line;
the eigenvalue \(\lambda\) is just how much that direction is stretched (\(\lambda>1\)),
squashed (\(0<\lambda<1\)), or flipped (\(\lambda<0\)). A pure rotation has *no* real
eigenvectors — every direction turns — which is why its eigenvalues come out complex.
That's not an error; it's the algebra reporting "nothing stays put."

## Check yourself
1. A matrix has eigenvalue \(\lambda = 0.5\) along some direction. What happens to a
   vector pointing that way? *(It halves in length, same line — it does **not** vanish.)*
2. A 2×2 rotation's eigenvalues are complex. Bug, or meaningful? *(Meaningful: no real
   direction is left fixed.)*
3. Is \((1,1)\) an eigenvector of \(\begin{pmatrix}3&1\\0&2\end{pmatrix}\)?
   *(No — \(M(1,1)=(4,2)\) points a different way. \((1,0)\) and \((1,-1)\) are the eigenvectors.)*

## Where to go next
Now that "matrix = transformation" is in place, **diagonalisation** is the natural
next step: choosing eigenvectors as your axes so the transformation becomes plain
scaling. After that, where this pays off in your world — normal modes, and the
eigenvalue equation \(\hat H\psi = E\psi\) in quantum mechanics, which is the same
picture with operators.
