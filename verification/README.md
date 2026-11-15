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

## Learning-route structure

```bash
python3 verification/check_learning.py
```

This second standard-library check verifies stable milestone identifiers M01–M30, the partition of 12 background and 18 narrative milestones, six required fields, earlier-only dependencies including ID ranges, the selected Watrous 2018 anchor identity, and local retrieval links and heading fragments from the README, LLM guide and learning files. It also reports a limited qualifier-word inventory and rejects explicit private coaching or authorization markers. These are structural aids: a separate reading must check the teaching, actual book pointers, scientific qualifiers and rendered mathematics.

## Hosted presentation checks

The same-repository pull-request workflow in `.github/workflows/hosted-math.yml` uses `contents: read`, checks out the exact proposed commit without persisted credentials, and visits its public GitHub Markdown pages anonymously. The unchanged helpers in `verification/hosted_math/` first probe the README and then compare every tracked Markdown page at widths 1440 and 760. They record source hashes, accessible mathematical structure, display geometry, HTML and screenshots.

A passing report supports source-to-host agreement at the recorded revision and time. It is separate from visual inspection of the captures and from mathematical or pedagogical review. A green job alone is not a proof of correctness. Workflow artifacts have limited retention and should not be treated as permanent scientific preservation.
