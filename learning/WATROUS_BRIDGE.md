# From Watrous to phase persistence

The selected educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**, published by Cambridge University Press in April 2018. The [author's official book page](https://cs.uwaterloo.ca/~watrous/TQI/) supplies a [pre-publication manuscript](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf) for personal use, with a restriction against selling or redistributing it. This repository links to that manuscript; it does not reproduce or distribute it.

The book provides the mathematical language for reading this project. The phase-persistence theorem is a research result developed in the [science route](../science/README.md), with its research dependencies identified in [related work](../references/related-work.md). Those papers and constructions are dependencies, not additional educational anchors.

## A focused route through the selected book

Section numbers and page numbers below refer to the author's standard-layout manuscript linked from the official page.

| Official chapter | Verified sections to use | Connection to this project |
| --- | --- | --- |
| [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) | §2.1.2, pp. 61–66; §§2.2.1–2.2.2; §§2.3.1–2.3.2, especially the instruments discussion on pp. 111–113 | Density operators and mixtures describe hidden phases; channels and measurements describe the receiver; an instrument records success while retaining a quantum output. |
| [Chapter 3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf) | §3.1.1, especially Theorem 3.4 and Proposition 3.5, pp. 128–130 | Trace norm controls changes in observable output probabilities. |
| [Chapter 7](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf) | §7.1.1, especially Proposition 7.1 and the bag-indexed basis, pp. 391–394 | Identical pure copies admit an occupation basis, which makes phase averaging explicit. |

## Translate the notation before the argument

Watrous uses ordinary vectors and their adjoints rather than Dirac notation. The translation is:

| Book notation | Notation used here |
| --- | --- |
| A classical alphabet $`\Sigma`$ and space $`\mathcal X=\mathbb C^\Sigma`$ | The known labels $`[N]=\{0,\ldots,N-1\}`$ and their $`N`$-dimensional register |
| Standard vector $`e_x`$; matrix unit $`E_{x,y}=e_xe_y^*`$ | $`\lvert x\rangle`$; $`\lvert x\rangle\langle y\rvert`$ |
| Pure state $`uu^*`$ | $`\lvert\psi\rangle\langle\psi\rvert`$ |
| Identity $`1_{\mathcal X}`$ and adjoint $`A^*`$ | $`I`$ and $`A^\dagger`$ |
| Measurement effect $`\mu(y)`$ | An effect $`E_y`$, with outcome probability $`\mathrm{Tr}(E_y\rho)`$ |
| $`n`$ tensor factors in Chapter 7; a bag $`\varphi\in\mathrm{Bag}(n,\Sigma)`$ | $`t`$ copies in one block; an occupation vector with entries $`n_x=\varphi(x)`$ |

The last row prevents a useful ambiguity: the book's tensor count $`n`$ is not the universe size $`N`$. In this project $`N=2M`$, the hidden support $`S`$ has size $`M`$, $`q\ge2`$ is a fixed phase order, $`B`$ is the known number of consecutive source calls sharing one table, and $`T`$ is the hard total acquisition budget. An individual block contributes $`t\le B`$ observed copies. The receiver knows these parameters and the basis, but does not know $`S`$ or the phase table.

## Mixture and product are different operations

For a fixed hidden support and table, define

```math
|\psi_{S,z}\rangle
=\frac1{\sqrt M}\sum_{x\in S}\omega_q^{z_x}|x\rangle,
\qquad \omega_q=e^{2\pi i/q}.
```

Averaging independent uniform table entries gives the one-copy state

```math
\rho_S
=\mathbb E_z|\psi_{S,z}\rangle\langle\psi_{S,z}|
=\frac1M\sum_{x\in S}|x\rangle\langle x|.
```

The convex-mixture and tensor-product rules from Chapter 2 must be applied in the order specified by the source. A table drawn once for $`t`$ emissions gives

```math
\Omega_{q,S}^{(t)}
=\mathbb E_z\!\left[
 (|\psi_{S,z}\rangle\langle\psi_{S,z}|)^{\otimes t}
\right],
```

whereas independent redraws at every emission give $`\rho_S^{\otimes t}`$. Their one-register reductions agree; their joint states need not. This is a correlation created by reusing a hidden classical parameter. No entangling source operation is assumed: conditioned on the table, the emitted copies are a product state.

The [four-label worked example](WORKED_EXAMPLE.md) displays an off-diagonal entry that survives the first average and disappears in the second.

## From the symmetric basis to the phase-specific step

A vector $`|\psi\rangle^{\otimes t}`$ is unchanged by permutations of the copies. The bag basis in §7.1.1 becomes the normalized occupation state $`|n\rangle_{\mathrm{sym}}`$: the uniform superposition of ordered strings in which label $`x`$ occurs $`n_x`$ times. For the uniform-magnitude source, its coefficient has squared magnitude

```math
p_n=\frac{t!}{M^t\prod_x n_x!},
\qquad \sum_xn_x=t.
```

The new calculation to perform in this basis is a finite character average:

```math
\frac1q\sum_{z=0}^{q-1}\omega_q^{(n_x-m_x)z}
=\begin{cases}
1,&n_x\equiv m_x\pmod q,\\
0,&\text{otherwise}.
\end{cases}
```

It follows that a root-phase block retains exactly the occupation coherences with coordinatewise equal residues modulo $`q`$. Continuous independent address phases retain only equal occupations. These two averaging rules are research ingredients applied here; the textbook's symmetric-space framework alone does not establish the persistence law.

If every $`n_x\lt q`$, no different nonnegative occupation vector of the same total can have those residues. Indeed, writing $`m_x=n_x+qk_x`$ forces every $`k_x\ge0`$, and equal totals force all of them to vanish. Thus the two averaged states have an identical good component. Their remaining weight is bounded by

```math
\Pr[\text{a label occurs at least }q\text{ times}]
\le \binom tq M^{1-q}.
```

Here permutation-invariant vectors and permutation-invariant density operators should be distinguished. A refreshed state can commute with every register permutation without being supported entirely on the symmetric-vector subspace. The worked example gives both kinds of state explicitly.

## Why trace norm reaches every receiver

This project defines trace distance with the factor

```math
D(\rho,\sigma)=\frac12\|\rho-\sigma\|_1.
```

The measurement comparison in §3.1.1 implies that, for any effect $`0\le E\le I`$,

```math
|\mathrm{Tr}(E\rho)-\mathrm{Tr}(E\sigma)|
\le D(\rho,\sigma).
```

For example, this follows from Proposition 3.5 applied to the two-outcome measurement $`\{E,I-E\}`$: the two probability differences are opposite, so their total absolute sum is twice the displayed difference. Any receiver followed by a final yes/no success readout induces such an effect on its entire input. Its ancillas, adaptive operations and memory therefore cannot evade the full-state comparison.

For a fixed support, replace each root-phase block by its continuous-phase comparison state and telescope across blocks. The [converse](../science/phase-twirl-converse.md) obtains

```math
D(\Omega_{q,S}^{\mathbf t},\Gamma_S^{\mathbf t})
\le\min\left\{1,
 M^{1-q}\sum_j\binom{t_j}{q}\right\}.
```

This is an unconditional comparison of normalized inputs. It does not condition the experiment on a collision and does not restrict the receiver to separate block measurements.

## Three further steps supplied by the research argument

The textbook tools need three task-specific additions before they become the theorem.

1. **A comparison that preserves all input information.** The continuous-phase block is generated exactly by drawing ordinary labels from $`S`$, computing their histogram and coherently preparing its normalized occupation state. This inherited coupon-state simulation retains permutation coherence, including repeated labels; it is not a claim that the block is diagonal in the ordered-string basis.
2. **The posterior for an absent label.** Under a uniform prior on balanced supports, a transcript containing $`d`$ distinct labels leaves a uniform posterior over supports containing them. Every unobserved label then has complement probability $`M/(N-d)`$. No computation on that transcript can improve on its best posterior choice. Together with the trace-distance comparison, this bounds the actual classical output.
3. **A physical route to the matching upper bound.** The inherited coherent power instrument removes the root phases while erasing any residual record that would identify the output label. Its success probability, failed attempts and block tails must all be charged. The established positive-subset diffuser then produces a complement label. General channel and instrument definitions make this a legitimate operation; they do not supply its multiplicity correction or its success formula.

The [attribution account](../references/related-work.md) identifies the phase-moment, coupon-simulation, power-extraction and positive-diffuser antecedents. The two directions combine to give, for fixed $`q`$,

```math
Q_q(N,B)
=\Theta_q\!\left(
\min\left\{N,
\max\left\{N^{1-1/q},(N/B)^{q-1}\right\}
\right\}\right).
```

The [frontier](../science/persistence-frontier.md) supplies the complete theorem and quantifiers. It counts every acquired specimen, has unconditional success at least $`2/3`$, and allows arbitrary joint processing across known exact $`B`$-call source blocks. The upper bound works for every permitted table sequence; the converse uses independent uniform tables as a hard prior. The basis and finite root alphabet are promises, not learned free resources.

This is a supplied-copy result. No membership oracle, source preparation program, inverse, reflection or QRAM is supplied. Source construction and receiver gates, storage and synthesis are accounted for separately in [implementation](../science/implementation.md). The bridge and finite example do not establish an end-to-end classical-data runtime advantage, unknown-boundary robustness or the asymptotic proof by numerical inspection.

[Worked example](WORKED_EXAMPLE.md) · [Source model](../science/model.md) · [Scientific reading route](../science/README.md)
