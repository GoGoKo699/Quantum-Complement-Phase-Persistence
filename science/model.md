# Source model and operational task

A quantum sample can reveal an element outside its own support by interference. That capability depends on more than the probability distribution obtained by measuring the sample. This project asks how it depends on an unknown phase pattern and on the number of consecutive specimens that retain that pattern.

The [frontier theorem](persistence-frontier.md) concerns supplied specimens, with every acquisition charged. It compares arbitrary collective quantum receivers with receivers given ordinary classical samples. It does not assume that an arbitrary hidden subset can be prepared efficiently from classical data.

## 1. The hidden support

Let $`N=2M`$ be even, and let $`[N]=\{0,\ldots,N-1\}`$ label a known computational basis. A hidden set $`S\subset[N]`$ has known size $`|S|=M`$. Its complement is $`\bar S=[N]\setminus S`$.

The support remains fixed throughout one experiment. The receiver knows $`N`$, $`M`$ and the source promises, but receives no description of $`S`$.

An ordinary sample is a uniformly distributed label from $`S`$. A positive quantum sample is

```math
|S\rangle=\frac{1}{\sqrt M}\sum_{x\in S}|x\rangle.
```

The task is to output one label $`Y\in[N]`$ with

```math
\Pr[Y\notin S]\ge \frac23.
```

This is a relational output requirement. The receiver need not identify $`S`$, output its size, reconstruct a quantum state, or certify its own answer. It must return an answer on every execution; failure flags and rejected attempts do not become discarded experimental trials.

The fixed threshold $`2/3`$ is a convention. The same asymptotic orders hold for any fixed target success strictly between $`1/2`$ and $`1`$ in the exact-root model, with constants depending on that target. The phase-cell version has the additional success margin stated below.

## 2. Frozen phase blocks

Fix an integer $`q\ge2`$ and set

```math
\omega_q=e^{2\pi i/q}.
```

The order $`q`$ is fixed as $`N`$ grows. A phase table $`z:S\to\{0,\ldots,q-1\}`$ defines the pure specimen

```math
|\psi_{S,z}\rangle
=\frac{1}{\sqrt M}\sum_{x\in S}\omega_q^{z_x}|x\rangle.
```

Fix a known integer $`B\ge1`$. The source calls are partitioned into the consecutive blocks

```math
\{1,\ldots,B\},\quad
\{B+1,\ldots,2B\},\quad\ldots.
```

Within each block, exactly $`B`$ consecutive source calls provide independent copies of the same pure state. A new phase table may be used in the next block. The boundaries and $`B`$ are known to the receiver. The last block actually observed by a finite experiment may be partial.

**The promise is a fixed available block length, not merely an upper bound on persistence.** A source promised only to retain a table for at most $`B`$ calls could refresh after every call; that weaker promise does not support the attaining frontier.

For a deterministic sequence of phase tables $`\mathbf z=(z^{(1)},z^{(2)},\ldots)`$, the first $`T`$ source outputs are the product state

```math
\rho_{S,\mathbf z}^{(T)}
=
\bigotimes_{j=1}^{J(T)}
\left(
|\psi_{S,z^{(j)}}\rangle
\langle\psi_{S,z^{(j)}}|
\right)^{\otimes t_j},
```

where the observed block lengths satisfy

```math
t_1=\cdots=t_{J(T)-1}=B,\qquad
1\le t_{J(T)}\le B,\qquad
\sum_j t_j=T.
```

No phase is refreshed within one such block. Conditioned on the table sequence, the source does not entangle different specimens.

### Worst-case and random-table guarantees

The primary upper bound works for every hidden balanced support and every admissible sequence of root-phase tables. It therefore also works if the tables are independently and uniformly redrawn.

The lower bound chooses $`S`$ uniformly among the balanced supports and chooses every table entry independently and uniformly from $`\mathbb Z_q`$, independently between blocks. This is a prior used to prove a lower bound against arbitrary receivers. An average-case lower bound under this prior implies the worst-case lower bound.

Consequently, the same order holds both for the minimax family of all table sequences and for the source model in which uniform random phase tables are part of the specified experiment. These statements should not be interchanged with a guarantee for a particular known table.

## 3. Receiver access and allowed processing

The receiver may use:

- arbitrary ancillary states independent of the hidden support and tables;
- arbitrary known unitaries, collective instruments and adaptive measurements;
- unrestricted protected quantum memory connecting different source blocks;
- unrestricted classical records and computation;
- arbitrary joint processing of all acquired specimens.

The lower bound imposes no measurement-batch cap and no coherent-memory cap. In particular, the parameter $`B`$ restricts the persistence of the source phase table, not the receiver's storage or the number of specimens it may jointly measure.

The receiver does not receive any of the following resources:

- a membership or value oracle for $`S`$;
- a preparation circuit for the unknown specimen, its inverse or a controlled version;
- a reflection about the unknown specimen or support state;
- the hidden phase table, its seed or a phase-reference program depending on it;
- a free loader or a quantum random-access memory containing hidden classical data.

Known gates, source-independent reflections and ordinary classical data structures are allowed. The diffuser about the known uniform state is one such known operation.

## 4. Hard copy cost

A receiver has hard copy budget $`T`$ if it acquires at most $`T`$ specimens on every execution branch. The budget counts all acquired specimens:

- those used in unsuccessful coherent recovery attempts;
- those measured only for classical information;
- those discarded to reach the next known source boundary;
- those retained and later ignored.

Stopping before acquisition of a future specimen does not charge that unacquired specimen. Waiting does not provide a free command to reset the source phase table. To cross an unconsumed part of a source block, the receiver must acquire and charge its specimens.

Let $`Q_q(N,B)`$ be the smallest hard budget for which an allowed receiver achieves success at least $`2/3`$ for every balanced $`S`$ and every root-phase table sequence.

A protocol that adaptively requests at most $`T`$ specimens can be represented as one channel acting on the first $`T`$ source registers: supply those registers in advance and let the protocol ignore the unused suffix. This representation is only a lower-bound device. It does not supply an inverse source oracle or alter the actual copy charge.

The principal result is

```math
Q_q(N,B)
=
\Theta_q\!\left(
\min\!\left\{
N,\,
\max\!\left\{
N^{1-1/q},
\left(\frac NB\right)^{q-1}
\right\}
\right\}
\right).
```

The constants may depend on fixed $`q`$ and the fixed success threshold, but not on $`N`$ or $`B`$. The claim is uniform over positive integer $`B`$ as $`N`$ grows. Small finite dimensions can be absorbed into the $`q`$-dependent constants. No growing-$`q`$ theorem or uniform limit from finite $`q`$ to continuous phases is asserted.

## 5. The comparison sources

### Positive phases

If the source supplies $`|S\rangle`$, one specimen suffices. With

```math
|u\rangle=\frac1{\sqrt N}\sum_{x\in[N]}|x\rangle,
\qquad
R_u=2|u\rangle\langle u|-I,
```

balanced cardinality gives

```math
R_u|S\rangle=|\bar S\rangle.
```

Measuring this output returns a uniformly distributed complement element. This operation and the original complement-sampling separation are due to Benedetti, Buhrman and Weggemans; see [related work](../references/related-work.md).

The comparison is with calibrated positive samples. A known arbitrary phase-correction circuit could also be charged explicitly, but it is not supplied in the hidden-phase experiment.

### Continuous hidden phases

Replace the root phases by arbitrary phases $`e^{i\theta_x}`$. For the lower bound, draw each $`\theta_x`$ uniformly from the circle, once per source block. The upper bound may simply measure the acquired specimens and use ordinary samples. For every block length,

```math
Q_{\mathrm{continuous}}(N,B)=\Theta(N).
```

The [converse](phase-twirl-converse.md) proves this using the inherited exact correspondence between random-phase copies and classical samples followed by coherent histogram preparation. It does not claim that the averaged many-copy state is diagonal in the ordered computational basis.

### Independently refreshed phases

When $`B=1`$, assume each new table has vanishing cross-address phase moments,

```math
\mathbb E[e^{i(\theta_x-\theta_y)}]=0
\qquad(x\ne y).
```

Independent zero-mean phases across addresses satisfy this condition. Zero mean at each address alone does not: a shared random global phase has no dephasing effect. Under the cross-address condition, each averaged specimen is

```math
\frac1M\sum_{x\in S}|x\rangle\langle x|.
```

Independent refresh makes the full source exactly a sequence of ordinary samples, expressed as diagonal quantum registers. Thus constant complement advantage requires $`\Theta(N)`$ specimens. Retaining a zero-mean phase pattern across specimens is therefore operationally different from independently refreshing it.

## 6. Fixed-width phase cells

The discrete phases need not be exact. Fix a known $`\eta\ge0`$ with

```math
s_\eta:=\cos^2\eta>\frac23,
\qquad
0\le\eta\lt \frac{\pi}{2}.
```

Within each source block, permit

```math
\theta_x=\frac{2\pi z_x}{q}+\delta_x,
\qquad
|\delta_x|\le\frac{\eta}{q}.
```

The offsets and root indices remain fixed throughout that block and may change at the next boundary. A global phase is immaterial. The receiver need not know the individual offsets.

The same copy order holds, with constants also depending on the positive margin $`s_\eta-2/3`$. The exact-root family is a subfamily and supplies the lower bound. For the upper bound, the inherited power extractor cancels the root phase and leaves phases $`e^{iq\delta_x}`$. The known diffuser then has complement success at least $`s_\eta`$ on each successful recovery. The [recovery account](coherent-recovery.md) makes the repeated-trial and unconditional-success margins explicit.

This is a promise about bounded coherent phase offsets. It is not a theorem for arbitrary mixed-state source noise, uncontrolled drift within one block, or imperfect hardware.

## 7. What identical one-copy states do and do not imply

For fixed $`S`$, averaging any independent uniform root phases with $`q\ge2`$ gives

```math
\mathbb E_z
|\psi_{S,z}\rangle\langle\psi_{S,z}|
=
\frac1M\sum_{x\in S}|x\rangle\langle x|.
```

Uniform continuous phases give the same density operator. All of these pure specimens also have exactly the same computational-basis distribution before averaging.

Their many-copy sources differ because a hidden table is reused. In general,

```math
\mathbb E_z
\left[
\left(
|\psi_{S,z}\rangle\langle\psi_{S,z}|
\right)^{\otimes t}
\right]
\ne
\left(
\mathbb E_z
|\psi_{S,z}\rangle\langle\psi_{S,z}|
\right)^{\otimes t}.
```

The frontier measures a consequence of those correlations for one classical-output task. Equal one-copy averaged states do not determine the information available from a persistent source.

## 8. Implementation and boundaries

The theorem counts supplied copies. The attaining quantum processing uses an explicitly held batch and an inherited occupation-basis compiler, with known gate and workspace costs given in [implementation](implementation.md). Arbitrary connectivity and controlled finite synthesis are material implementation assumptions.

Preparing an arbitrary hidden subset state is a separate source operation. The result does not turn an arbitrary classical dataset into these specimens at no cost. It establishes neither a hardware crossover nor a generic end-to-end exponential runtime improvement.

The support is balanced and known in size; the source block length and boundaries are known; $`q`$ is fixed; and the target is one complement label. Unknown boundaries, unknown support size, growing phase alphabets, general phase distributions and minimum receiver-memory questions require separate analyses.

[Frontier and regimes](persistence-frontier.md) · [Phase-twirl converse](phase-twirl-converse.md) · [Coherent recovery](coherent-recovery.md)

