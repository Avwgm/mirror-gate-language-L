# Mirror Gate Language L — Recursive Symbolic NP Instance

These scripts implement a constructive example of a language L ∈ NP  
as described in Walecki (2025), “NP No Problem” — a symbolic reframe of the P vs NP structure.

## Language Definition

L = { x | r(h(x)) = h(x) }

Where:
- `h(x)` is a keyed XOR transformation.
- `r(y)` is a bitwise reverse and bitwise NOT (mirror inversion).

This defines a **symbolically constrained language** with:

- Polynomial-time verification (verify.py)
- Exponential-time generation (generate.py)

## Files

- `mirrorgate.generate.L.py` — Exhaustively generates valid x ∈ L
- `mirrorgate.verify.L.py` — Verifies a given x ∈ L

## Purpose

To provide a **demonstrable system** showing:

- Tractable verification
- Symbolically obfuscated generation
- Structural asymmetry akin to mirror logic systems


---

## Reference

Walecki, G. (2025). *NP = No Problem: Reflective Language Systems and Symbolic P vs NP Mirrors.*

---
