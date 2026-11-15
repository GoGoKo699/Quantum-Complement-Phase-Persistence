# What phase persistence changes

Two sources can give the same density operator for every individual specimen and still require very different numbers of specimens for the same classical task. The difference is in the joint state delivered over time. This project quantifies that distinction for complement sampling.

## A sample can reveal an absent label

The receiver gets specimens supported on an unknown balanced set $`S`$ in a known $`N`$-label basis and must return one label outside $`S`$. Reading a specimen in that basis only reveals a member of the set. Enough such observations eventually make an unseen label a reliable complement guess, at linear sample cost.

A calibrated positive-amplitude specimen has an additional resource: its amplitudes interfere in a known phase convention. The complement swapper of Benedetti, Buhrman and Weggemans turns one such specimen into a state supported on the complement. That endpoint and the original sampling task are established prior work; see [related work](../references/related-work.md).

Here the phase convention is unknown. With fixed integer $`q\ge2`$, a specimen has the form

```math
|\psi_{S,z}\rangle
=\frac{1}{\sqrt M}\sum_{x\in S}\omega_q^{z_x}|x\rangle,
\qquad M=N/2,\quad \omega_q=e^{2\pi i/q}.
```

Its basis probabilities are unchanged. Nevertheless, applying the positive-state swapper directly need not find a complement label with a useful advantage. The algorithm must use the source's promise about how those unknown phases repeat.

## The same one-copy average conceals different experiments

For independent uniform hidden phase values at the supported labels,

```math
\mathbb E_z\bigl[|\psi_{S,z}\rangle\langle\psi_{S,z}|\bigr]
=\frac1M\sum_{x\in S}|x\rangle\langle x|.
```

This equation holds for every root alphabet in the theorem and for continuously uniform phases. It describes the receiver's one-copy average over the hidden source pattern. It does not say that each conditionally prepared specimen has been measured or physically dephased.

If the pattern is chosen once and reused, the received state is

```math
\mathbb E_z\bigl[
  (|\psi_{S,z}\rangle\langle\psi_{S,z}|)^{\otimes t}
\bigr].
```

If the pattern is independently chosen for each emission, the received state is the tensor power of the one-copy average. These expressions generally differ. A measurement restricted to one specimen cannot distinguish the schedules, while collective processing can use their different correlations.

The [source model](model.md) specifies known consecutive refresh blocks of exactly $`B`$ emissions. The unknown phase values remain fixed inside a block and may change at the next boundary. The lower-bound experiment draws independent uniform phase tables between blocks. The upper algorithm succeeds for every phase assignment permitted within those blocks. Exact block persistence is an input promise; a mere upper bound on block length would also allow complete refreshing at every emission.

## Repeated phases can be removed collectively

When $`q`$ supported amplitudes with the same label are multiplied coherently, their root phases cancel. A suitable collective instrument extracts those powered amplitudes while removing information in the remaining registers that could distinguish the surviving label. Measuring an ordinary repeated label would instead reveal a member of $`S`$ and would not supply the needed coherent specimen.

The multiplicity-corrected extractor is inherited from Quantum Coherent Collisions. The new schedule applies it to batches contained inside source blocks, then uses the established complement swapper. The [recovery account](coherent-recovery.md) gives the exact success probability; [implementation](implementation.md) charges the processing and precision.

The converse addresses the actual classical output. Below the relevant repeated-label scale, the finite-phase ensemble has a large common part with a continuously phase-averaged ensemble. The latter is exactly reproducible from ordinary classical samples by the established coupon-state simulator. This comparison bounds every joint receiver, including one retaining coherent memory across different source blocks. See [the converse](phase-twirl-converse.md) for the precise occupation-sector argument.

## The phase persistence frontier

At fixed alphabet size and fixed required success above one half, the optimal supplied-copy order is

```math
Q_q(N,B)
=\Theta_q\!\left(
  \min\left\{N,
    \max\left\{
       N^{1-1/q},\left(\frac NB\right)^{q-1}
    \right\}
  \right\}
\right).
```

The [main theorem](persistence-frontier.md) states the quantifiers and success conventions. Useful endpoints are:

| Source promise | Optimal supplied copies | Meaning |
| --- | --- | --- |
| Known positive phases | One | Established calibrated-phase complement sampler |
| Unknown signs frozen indefinitely | $`\Theta(\sqrt N)`$ | Persistent sign disorder retains a quadratic sample advantage |
| Unknown $`q`$-root phases frozen indefinitely | $`\Theta_q(N^{1-1/q})`$ | The required coincidence order determines the exponent |
| Independent refreshing at every emission | $`\Theta(N)`$ | The entire supplied joint state is reproducible from ordinary samples |
| Continuously uniform hidden phases, frozen within arbitrary blocks | $`\Theta(N)`$ | Persistent phases alone do not ensure a finite-order cancellation route |

For signs, the block law is $`\Theta(\min\{N,\max\{\sqrt N,N/B\}\})`$. Growing persistence improves the copy cost until blocks are long enough to reach the frozen-source scale. For a larger fixed alphabet, the full theorem specifies a different threshold. These are statements about the promised phase alphabets and refresh schedules, rather than a universal classification of noise with temporal correlations.

## Calibration and costs remain part of the result

The computational basis and root alphabet are specified. The receiver is not given the individual phase values, the set description, a membership oracle, a preparation circuit, a source inverse, or a source reflection. Adding any of those resources defines a different access problem.

The phase-cell extension allows offsets $`|\delta_x|\le\eta/q`$ around the discrete roots, with a fixed explicit margin between the desired success and $`\cos^2\eta`$. Coherent extraction then leaves phases $`e^{iq\delta_x}`$; it does not reconstruct an exactly positive state. The theorem's copy order survives because the remaining phase spread is bounded tightly enough for complement interference. This promise does not establish tolerance to arbitrary dephasing, unknown refresh boundaries, or drifting phases inside a block.

Every supplied copy counts, including failed batches and discarded block remainders. The receiver has an explicit reversible occupation-processing implementation without QRAM, with separately stated gates, workspace and finite-synthesis accuracy. Its efficiency as a receiver does not make a generic hidden source cheap: an arbitrary balanced set or phase table can require a description and preparation work growing with $`N`$. The result is therefore a sample-acquisition advantage for the stated source interface, with an explicit processing account. It establishes no industrial runtime advantage or hardware crossover.
