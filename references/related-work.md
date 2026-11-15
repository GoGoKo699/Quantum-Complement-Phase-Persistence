# Related work and attribution

The contribution is the matching supplied-copy law for **one classical complement label** when an unknown phase pattern persists for a specified number of emissions. The complement task, phase-moment calculations, classical-data simulation, and coherent power extractor have separate antecedents. This page identifies those dependencies and the operational statement that remains.

## The task and the calibrated-phase endpoint

Benedetti, Buhrman and Weggemans [BBW26] introduced complement sampling: receive samples from an unknown set and return an element outside it. Their positive-amplitude quantum sample has a specified phase convention. For a balanced set, one application of the known uniform-state reflection converts that sample to its complement state. Their classical posterior argument supplies the linear sample baseline for a constant success advantage.

The present [model](../science/model.md) changes the supplied source: each supported basis label carries an unknown root-of-unity phase, shared within known refresh blocks. The [persistence frontier](../science/persistence-frontier.md) determines the optimal classical-output copy cost under that promise. The positive-amplitude one-copy endpoint is credited to [BBW26], rather than claimed here.

The experimental follow-up of Benedetti et al. [BMMWRB26] uses structured Bernstein–Vazirani subsets and carefully distinguishes them from pseudorandom-permutation subsets. Its single-copy classicality separation does not give the uniform balanced-set multicopy lower bound: its supplementary analysis permits a successful classical strategy with order the bit-string length many BV samples. Our converse uses uniformly random balanced sets; the attaining algorithm works for every allowed set. No BV or cryptographic-source conclusion is inferred from that converse.

## Random phases and classical-data simulation

Goyal, Malavolta and Roberts [GMR25], Theorems 3–4 and Section 3.1, give an exact simulation for random-phase coupon states. When the phase modulus exceeds the number of copies, averaging one phase vector reused across those copies produces a mixture of normalized permutation states of ordinary sampled coupons. This identity includes repeated coupons and parallel instances. The simulator performs quantum processing on classical samples; it is not a classical simulation of arbitrary quantum circuits.

Their result supplies the exact continuous-phase comparison used here: for each finite copy budget, continuous phase averaging enforces the same occupation equality as a sufficiently large modulus. The additional argument in [our converse](../science/phase-twirl-converse.md) isolates the extra coherences admitted by a fixed alphabet and bounds their total mass across independently refreshed blocks. Thus the continuous-phase simulation is inherited; the finite-alphabet complement-output lower bound and its dependence on block length are the task-specific conclusions.

Aaronson et al. [ABFGVZZ24], Lemma 2.4 of arXiv:2211.00747v2, already analyze binary subset-phase states at a fixed support. Their proof groups occupations modulo two, uses permutation/type states, and bounds the effect of repeated labels by a birthday estimate. Its purpose is pseudorandomness and pseudoentanglement. We credit that occupation-sector method; the present law does not introduce phase averaging or the birthday principle.

Alrabiah et al. [AAGW26], Appendix B, explicitly derive the general finite-field moment condition: a matrix element survives random phase averaging when every label's occupation numbers agree modulo the phase alphabet. They compare random phase moments with Haar moments on a collision-free sector. Here the relevant common sector allows every occupation below the alphabet size, rather than only distinct labels. Combining that sector with the coupon simulator and the complement payoff gives the sharper task-dependent collision threshold. The proof here uses cyclic root phases for every fixed integer alphabet size; no finite-field structure is needed.

## The coherent recovery algorithm is inherited

The public [Quantum Coherent Collisions account](https://github.com/GoGoKo699/Quantum-Coherent-Collisions/tree/219f590010247124f48feffaf244a60f306335f4) [QCC26] supplies a universal multiplicity-corrected instrument that extracts the normalized state with amplitudes raised to a fixed integer power from identical unknown input copies. Its exact success formula and occupation compiler are the constructive dependencies used in [coherent recovery](../science/coherent-recovery.md) and [implementation](../science/implementation.md).

For root-of-unity phases, the appropriate power removes the unknown discrete phase. The known balanced-set diffuser then gives a complement label. This application and the schedule respecting refresh blocks do not constitute a new power extractor.

The earlier converse has a different output contract: a coherent powered state for arbitrary continuous phases, even on known support. That statement does not by itself lower-bound production of a single classical label outside an unknown set. Our converse directly bounds that weaker classical output and permits arbitrary coherent processing across all received blocks.

## Related public source models

| Account | Actual source and task | Shared ingredient and distinct conclusion |
| --- | --- | --- |
| [Quantum Example Entropy](https://github.com/GoGoKo699/Quantum-Example-Entropy/tree/d1077fac179d33972a63f57d60d54b822721b328) [QEE26] | A pure graph example includes an address and a hidden random label register. The same label table may be frozen across copies. A quantum simulator receives ordinary classical examples. | Its common positive component and coherent permutation simulator preserve the underlying classical signal under a conditional-label collision criterion. It does not state a phase-only complement-sampling frontier. |
| [Local Quantum Complement Sampling](https://github.com/GoGoKo699/Local-Quantum-Complement-Sampling/tree/1d5f10d2ee166ce02dea3bfcdd21bf9f26959d39) [LQCS26] | One positive-amplitude balanced-subset sample has specified input qubits measured computationally before decoding. It gives an exact average success frontier and one-copy residual-dephasing analysis. | It quantifies access within one specimen. The present source has unrestricted collective access to many specimens and varies the persistence of hidden phases between specimens. |

These comparisons concern scientific statements at the linked revisions. Shared techniques are credited once; changing the output task or source correlation does not automatically imply a new theorem or transfer an existing converse.

## What this account adds

For fixed phase alphabet size, the [main theorem](../science/persistence-frontier.md) combines a matching complement-output converse with an attaining copy schedule across known refresh blocks. It identifies when phase persistence restores a sample advantage despite an identical one-copy averaged density operator. The phase-cell result retains that order under its explicit calibrated width and success margin.

The result charges every supplied specimen, including failed extraction attempts and unused block remainders. Preparation of a general hidden subset source, source descriptions, receiver gates and workspace are separate resources. No efficient preparation of arbitrary balanced subsets, industrial application advantage, hardware crossover, or optimal growing-alphabet asymptotic follows from the copy law.

The comparisons above cover the stated primary sources and the linked public accounts. They do not certify exhaustive priority or rule out every related formulation. Bibliographic identifiers and inspected source versions appear in [references.bib](references.bib).

## References

- **[BBW26]** Marcello Benedetti, Harry Buhrman and Jordi Weggemans, [*Provable and Verifiable Quantum Advantage in Sample Complexity*](https://doi.org/10.1103/q55v-wm7y), *Physical Review Letters* **136**, 040601 (2026). [arXiv:2502.08721v3](https://arxiv.org/html/2502.08721v3), Theorem 1 and the complement swapper; Supplemental Material Theorems 5–6.
- **[BMMWRB26]** Marcello Benedetti, Gabriel Marin-Sanchez, Jordi Weggemans, Matthias Rosenkranz and Harry Buhrman, [*Unconditional and exponentially large violation of classicality*](https://doi.org/10.1038/s41467-026-77413-3), *Nature Communications* **17**, 10557 (2026). [arXiv:2511.11008](https://arxiv.org/abs/2511.11008); Results and Supplementary Notes 1–2.
- **[GMR25]** Vipul Goyal, Giulio Malavolta and Bhaskar Roberts, [*Unconditional Quantum Cryptography with a Bounded Number of Keys*](https://doi.org/10.62056/ayzoxrxqi), *IACR Communications in Cryptology* **2**(1) (2025), Theorems 3–4 and Section 3.1.
- **[ABFGVZZ24]** Scott Aaronson, Adam Bouland, Bill Fefferman, Soumik Ghosh, Umesh Vazirani, Chenyi Zhang and Zixin Zhou, [*Quantum Pseudoentanglement*](https://doi.org/10.4230/LIPIcs.ITCS.2024.2), ITCS 2024, pp. 2:1–2:21. The fixed-support comparison used here is [arXiv:2211.00747v2, Lemma 2.4](https://arxiv.org/html/2211.00747v2).
- **[AAGW26]** Omar Alrabiah, Srinivasan Arunachalam, Sabee Grewal and John Wright, [*No low-degree tests for quantum states*](https://arxiv.org/html/2608.00265v1), arXiv:2608.00265v1 (2026), Appendix B.
- **[QCC26]**, **[QEE26]**, **[LQCS26]** The three public scientific accounts linked above, at their stated revisions.
