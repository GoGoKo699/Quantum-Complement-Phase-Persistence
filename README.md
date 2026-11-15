# Quantum Complement Phase Persistence

**The same one-copy mixed state can support different collective sampling costs.** A hidden phase pattern can look like complete dephasing on one specimen while still supplying useful correlations across repeated specimens. This project determines how long those phases must persist to help solve complement sampling.

An unknown set $`S`$ contains half of a known $`N`$-label universe. The receiver gets quantum specimens supported on $`S`$ and must output one label outside $`S`$, with unconditional success at least $`2/3`$. No membership oracle, source inverse, source reflection or hidden-set description is supplied.

## Principal result

Fix an integer phase order $`q\ge2`$. Each supported amplitude has an unknown $`q`$th-root phase. A phase table persists for **exactly $`B`$ consecutive source calls**, and the refresh boundaries are known. The receiver may retain and process all specimens jointly, including across different blocks.

The optimal hard budget of supplied copies is

```math
Q_q(N,B)
=\Theta_q\!\left(
\min\!\left\{N,
\max\!\left\{N^{1-1/q},\left(\frac NB\right)^{q-1}\right\}
\right\}
\right).
```

The constants depend on fixed $`q`$ and the fixed success threshold. The order is uniform in the positive integer $`B`$. Every acquired copy counts, including failed batches and discarded block tails.

For unknown signs, the law is $`\Theta(\min\{N,\max\{\sqrt N,N/B\}\})`$:

| Source promise | Optimal supplied copies |
| --- | --- |
| Positive amplitudes in the known basis | One, by the established complement swapper |
| Unknown signs fixed across all specimens | $`\Theta(\sqrt N)`$ |
| Unknown signs fixed for known blocks of $`B`$ calls | $`\Theta(\min\{N,\max\{\sqrt N,N/B\}\})`$ |
| Independent uniform signs at every address and every call | $`\Theta(N)`$ |
| Arbitrary continuous hidden phases, with any block length | $`\Theta(N)`$ |

The independent root-phase priors and continuous-phase prior have the same one-copy averaged density operator at fixed support. Their repeated-copy states differ. The matching lower bound covers arbitrary collective receivers with a **classical label** as output; it does not impose a memory or measurement-batch restriction.

For fixed $`q>2`$, sublinear copy cost requires persistence $`B\gg N^{(q-2)/(q-1)}`$. Reaching the full frozen-phase order requires $`B=\Omega(N^{1-1/q})`$. Fixed-width phase cells around the roots retain the same orders under an explicit success margin.

## Why repeated phases help

A collective collision instrument coherently raises supported amplitudes to the $`q`$th power. Root phases then cancel without measuring the surviving label. The known reflection about the uniform state turns the recovered balanced positive subset state into its complement. Restricting each recovery batch to one phase block gives the attaining persistence schedule.

Conversely, below the relevant $`q`$-fold repetition scale, the finite-phase ensemble has a large common component with a continuously phase-averaged ensemble. The latter can be reproduced exactly from ordinary classical samples followed by coherent histogram preparation. Bounding the extra component across blocks yields the converse for every joint receiver.

The complement task and positive-state swapper are due to Benedetti, Buhrman and Weggemans. The power extractor and its occupation compiler are inherited from [Quantum Coherent Collisions](https://github.com/GoGoKo699/Quantum-Coherent-Collisions/tree/219f590010247124f48feffaf244a60f306335f4). Random-phase coupon simulation and phase-moment methods also have prior sources. [Related work](references/related-work.md) separates those ingredients from the output-specific persistence law.

## Read the science

Start with the [connected scientific route](science/README.md), or go directly to a question:

| Question | Authoritative account |
| --- | --- |
| What is supplied, hidden, persistent and charged? | [Source model](science/model.md) |
| What is the exact theorem and its regime map? | [Persistence frontier](science/persistence-frontier.md) |
| Why can no collective receiver beat the copy order? | [Phase-twirl converse](science/phase-twirl-converse.md) |
| How does recovery work within a refresh block? | [Coherent recovery](science/coherent-recovery.md) |
| How are gates, workspace and rare-success precision charged? | [Implementation](science/implementation.md) |
| What does equality of one-copy states leave undetermined? | [Interpretation](science/interpretation.md) |
| Which conclusions and tools are inherited? | [Attribution](references/related-work.md) and [bibliography](references/references.bib) |

[llms.txt](llms.txt) maps theorem, story and reproduction requests to those files.

## Reproduce the finite checks

With Python 3.10 or later, no additional packages are needed:

~~~bash
python3 verification/check_science.py
~~~

The suite independently checks phase ensembles, occupation blocks, Kraus admissibility and factorization, exact batch probabilities, classical posteriors, charged source-clock schedules and phase-cell diffusion. The [verification guide](verification/README.md) gives its finite scope. These checks support the derivations; they are not an asymptotic proof, hardware experiment or priority certificate.

## Scope and costs

The main result is a supplied-quantum-data copy advantage. Preparing a general hidden subset source is a separate operation and may require work growing with $`N`$. Receiver gates, coherent batch storage, arbitrary connectivity and finite synthesis have explicit separate costs; no QRAM is assumed. No end-to-end classical-data runtime advantage or hardware crossover is established.

The source clock counts acquisitions. Waiting does not reset a phase block for free. Known exact boundaries, a balanced support, a fixed cyclic phase order and a fixed success margin are material assumptions. The result does not cover arbitrary drifting phases, general mixed-state noise, unknown boundaries or a growing-$`q`$ limit. The phase-cell extension controls coherent offsets around the stated roots.

## Purpose and contact

This repository serves as a record of the work and a guide for the author's self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
