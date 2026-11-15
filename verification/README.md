# Finite scientific checks

Run from the repository root with Python 3.10 or later:

```bash
python3 verification/check_science.py
```

The program uses only the Python standard library. It exits on a failed assertion and prints a JSON summary with the actual case counts on success.

| Check | Independent finite comparison |
| --- | --- |
| Root and continuous phase twirls | Explicit averages over phase assignments versus occupation residue classes; small matrix eigensystems versus the collision-mass trace bound |
| Collision extraction | Ordered-word enumeration versus the exact batch probability; directly constructed Kraus effects; reduced output matrices for complex amplitude profiles |
| Classical comparator | Ordered samples versus a sequential occupancy recursion; exhaustive support posteriors versus the unseen-label bound |
| Refresh blocks | Exact source-call partitions, including blocks shorter than the phase order; charged batch schedules at every tested starting offset |
| Phase-cell robustness | Full coordinate application of the uniform reflection to powered states, over balanced supports and phase-cell endpoints |
| Refresh assumptions | Independent address phases versus a zero-mean common global phase; persistent-table permutation coherence versus fresh one-copy tables |

Combinatorial comparisons use exact rational arithmetic. State vectors, phase averages and small real symmetric eigensystems use floating point with an explicit numerical tolerance. The cases include phase orders two, three and four, failed extraction sectors, and several finite support and batch sizes. A counterexample also checks why the phase-cell arc restriction cannot be omitted from the success-margin condition.

The source clock tested here keeps each phase pattern for exactly the specified number of consecutive source calls and exposes the block boundaries. Discarded boundary tails count as source calls. This is different from an unspecified upper bound on persistence.

These checks support the calculations at the tested sizes. The scientific proofs establish the general resource laws; the program does not prove asymptotic optimality, independently establish novelty, test every joint quantum protocol, or implement the complete symmetrization circuit on hardware.
