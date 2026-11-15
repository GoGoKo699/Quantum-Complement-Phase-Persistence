# The phase-persistence frontier

The input distribution alone does not fix the usefulness of a quantum sample. For a balanced hidden support, calibrated positive samples permit one-copy complement sampling. An unknown phase pattern can remove that capability, while retaining the same pattern across specimens allows a collective receiver to recover part of it.

The result below quantifies this effect with a matched lower bound and an explicit attaining construction. The [model](model.md) fixes the source, output, acquisition charge and implementation boundaries.

## 1. Main theorem

Let $`N=2M`$ be even. Fix an integer phase order $`q\ge2`$ independently of $`N`$. The unknown support has size $`M`$. Source calls come in known blocks of exactly $`B`$ consecutive copies sharing one hidden table of $`q`$th-root phases; the support remains fixed across blocks.

Let $`Q_q(N,B)`$ be the minimum hard total-copy budget for unconditional complement-sampling success at least $`2/3`$, uniformly over supports and phase-table sequences. Arbitrary collective processing and protected memory across blocks are allowed.

**Theorem 1 — phase-persistence law.**  
There are positive constants depending only on fixed $`q`$ such that, uniformly over integers $`B\ge1`$,

```math
\boxed{
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
}
\tag{1}
```

The statement is asymptotic in $`N`$. The constants also depend on the chosen fixed success threshold if that threshold is changed. Small finite dimensions do not alter the order.

Every acquired specimen is charged, including unsuccessful attempts and discarded source-block tails. There is no receiver-side measurement-batch restriction in the converse.

The same order holds when the source itself independently draws uniform root-phase tables per block and success is averaged over those tables, with worst-case support: the upper bound works for every table, and the lower bound already uses that random-table source.

## 2. Why two scales occur

Write

```math
R=M^{1-1/q},
\qquad
L=\left(\frac MB\right)^{q-1}.
```

The globally frozen scale $`R`$ is the number of specimens needed to obtain a $`q`$-fold repeated label with constant collective weight. At that scale an inherited coherent extractor can remove the unknown root phases without learning them.

Finite source persistence contributes the second scale $`L`$. A batch of size $`b`$ has useful $`q`$-fold collision weight of order $`b^q/M^{q-1}`$. When a refresh limits $`b`$ to order $`B`$, repeated trials consume order $`M^{q-1}/B^{q-1}`$ specimens.

Neither mechanism must be used when it costs more than the ordinary-sample strategy. That strategy needs only order $`N`$ specimens, giving the outer minimum in (1).

These are operational scales in one supplied-copy task. They are not claims that the receiver must literally perform a collision test.

## 3. Proof route: lower bound

The [phase-twirl converse](phase-twirl-converse.md) proves the following finite bound. For a receiver using at most $`T<N`$ source outputs, with observed phase-block lengths $`t_j`$,

```math
\Pr[Y\notin S]
\le
\min\!\left\{
1,\frac{M}{N-T}
\right\}
+
\min\!\left\{
1,\frac{1}{M^{q-1}}
\sum_j\binom{t_j}{q}
\right\}.
\tag{2}
```

The probability averages a uniform balanced support and independent uniform root-phase tables. This prior is sufficient for a minimax lower bound.

The first term is the optimal posterior bound available from ordinary samples. The second bounds every possible advantage supplied by finite-phase coherences beyond an exactly classically generated histogram state.

Since $`\sum_jt_j=T`$ and $`t_j\le B`$,

```math
\sum_j\binom{t_j}{q}
\le
\frac{1}{q!}\min\{T^q,T B^{q-1}\}.
\tag{3}
```

For $`T\le N/8`$, the first term of (2) is at most $`4/7`$. Reaching $`2/3`$ success therefore requires constant weight in the second term, forcing both

```math
T=\Omega_q(R),
\qquad
T=\Omega_q(L).
```

If $`T>N/8`$, the ordinary order $`\Omega(N)`$ is already reached. These alternatives give the lower half of (1).

This proof compares full states before the receiver acts. It therefore includes arbitrary quantum memory, adaptive instruments and joint processing across independently refreshed blocks.

## 4. Proof route: attaining algorithm

The [coherent-recovery account](coherent-recovery.md) uses the exact collective extractor from *Quantum Coherent Collisions*. Its construction and compiler are inherited; the phase-persistence schedule and complement output are the present application.

For a batch of $`b\ge q`$ identical specimens with uniform magnitudes on $`S`$, its exact success probability is

```math
p_b
=
\frac{(b)_q}{C_q M^{q-1}}\,
Q_q^{\mathrm{occ}}(b-q;M),
\qquad
C_q=\frac{(2q-1)!}{(q-1)!}.
\tag{4}
```

Here $`(b)_q=b(b-1)\cdots(b-q+1)`$, and $`Q_q^{\mathrm{occ}}(\ell;M)`$ is the probability that no label appears $`q`$ times among $`\ell`$ ordinary uniform draws. This probability notation is distinct from the copy complexity $`Q_q(N,B)`$.

Choose a batch no larger than $`B`$ and no larger, up to a fixed $`q`$-dependent factor, than $`R`$. Then

```math
p_b=\Theta_q\!\left(\frac{b^q}{M^{q-1}}\right).
\tag{5}
```

On heralded success, raising the amplitudes to their $`q`$th power cancels every root phase and leaves exactly $`|S\rangle`$. The known diffuser maps it to $`|\bar S\rangle`$. The output label is therefore certainly outside the support on that branch.

A deterministic number of fresh attempts raises the recovery probability to a chosen constant. Each source block is filled with as many complete $`b`$-copy attempts as fit; its remainder is acquired and discarded before the next block. The exact tail accounting in [coherent recovery](coherent-recovery.md) bounds the acquisition cost by less than twice the number of trial copies. No rare successful branch is treated as free.

Taking $`b=\Theta_q(\min\{B,R\})`$ when $`B\ge q`$ gives a hard budget of order

```math
\frac{M^{q-1}}{b^{q-1}}
=
O_q(\max\{R,L\}).
```

For $`B<q`$, or whenever this budget exceeds the ordinary-sample cost, use the classical strategy instead. Measure ordinary samples, collect their observed labels, and return a uniformly chosen unseen label. Order $`N`$ copies suffice.

Combining these two permitted strategies proves the upper half of (1). A uniform fallback output after all coherent attempts fail makes the total output unconditional. The detailed schedule chooses a success margin before finite synthesis error is allocated.

Known processing uses an explicitly held batch, ordinary reversible operations and source-independent gates, with no QRAM. The [implementation account](implementation.md) charges gate synthesis, coherent width and source preparation separately.

## 5. Three useful regimes

For fixed $`q`$, the scales in (1) give:

| Persistence | Copy order | Operational meaning |
| --- | --- | --- |
| $`B=O(N^{(q-2)/(q-1)})`$ | $`\Theta_q(N)`$ | The refresh-limited coherent strategy does not improve the asymptotic ordinary-sample order. |
| $`N^{(q-2)/(q-1)}\ll B\ll N^{1-1/q}`$ | $`\Theta_q((N/B)^{q-1})`$ | More specimens sharing one table improve the attainable copy order. |
| $`B=\Omega(N^{1-1/q})`$ | $`\Theta_q(N^{1-1/q})`$ | Persistence is sufficient to attain the indefinitely frozen order. |

The first row allows constant-factor improvements hidden by the order notation. The middle row is an asymptotic regime with both scale separations; it may be empty for a particular finite instance.

If $`B=N^\beta`$ up to fixed multiplicative factors, the copy exponent is

```math
a_q(\beta)
=
\min\!\left\{
1,\,
\max\!\left\{
1-\frac1q,\,
(q-1)(1-\beta)
\right\}
\right\}.
```

This exponent formula keeps $`q`$ fixed and does not assert uniform constants in $`q`$.

### Unknown signs

For $`q=2`$,

```math
Q_2(N,B)
=
\Theta\!\left(
\min\!\left\{
N,\max\left\{\sqrt N,\frac NB\right\}
\right\}
\right).
```

Per-specimen sign refresh has ordinary linear cost. An indefinitely frozen unknown sign pattern permits square-root cost. Persistence of order $`\sqrt N`$ is sufficient for that full quadratic sample advantage; shorter growing persistence gives the intermediate order $`N/B`$.

### Three phase values

For $`q=3`$,

```math
Q_3(N,B)
=
\Theta\!\left(
\min\!\left\{
N,\max\left\{N^{2/3},\frac{N^2}{B^2}\right\}
\right\}
\right).
```

Sublinear copy order requires persistence growing faster than $`\sqrt N`$. Persistence of order $`N^{2/3}`$ is sufficient for the fully frozen order.

## 6. Calibrated, finite and continuous phases

| Source promise | Required copy order for constant complement advantage |
| --- | --- |
| Calibrated positive amplitudes | One copy |
| Frozen unknown $`q`$th-root phases, fixed $`q\ge2`$ | $`\Theta_q(N^{1-1/q})`$ |
| Root phases refreshed independently every specimen | $`\Theta(N)`$ |
| Arbitrary continuous phases, including indefinitely frozen tables | $`\Theta(N)`$ |

The continuous-phase lower bound uses an independent uniform phase prior. It therefore lower-bounds the minimax arbitrary-phase family. It is not obtained by sending $`q`$ to infinity in the constants of (1).

For every fixed support, all the root ensembles in this table with $`q\ge2`$ and the continuous-phase ensemble have the same averaged one-copy density operator,

```math
\frac1M\sum_{x\in S}|x\rangle\langle x|,
```

and every realized pure specimen has the same computational-basis probabilities. Their different copy costs come from the correlations created by reusing a hidden table.

## 7. Robustness within phase cells

Suppose each phase in a source block lies within $`\eta/q`$ of a $`q`$th root, with fixed $`0\le\eta<\pi/2`$ and

```math
\cos^2\eta>\frac23.
```

The extractor returns a uniform-magnitude state with residual phases in the arc $`[-\eta,\eta]`$. The complement diffuser then succeeds with probability

```math
\left|
\frac1M\sum_{x\in S}e^{iq\delta_x}
\right|^2
\ge
\cos^2\eta.
```

Repeating recovery enough times leaves a fixed unconditional success margin above $`2/3`$. Exact root phases are allowed within the cells, so the converse remains unchanged. The result is

```math
Q_{q,\eta}(N,B)
=
\Theta_{q,\eta}\!\left(
\min\!\left\{
N,\,
\max\!\left\{
N^{1-1/q},
\left(\frac NB\right)^{q-1}
\right\}
\right\}
\right).
```

The constants deteriorate as the guaranteed margin closes. This robustness concerns bounded phase offsets frozen within a block, not arbitrary mixed-state noise or unknown within-block drift.

## 8. Scope of the consequence

The frontier identifies when the memory of a hidden phase pattern remains useful for one classical-output algorithm. It establishes a supplied-copy advantage with an explicit processing route and a converse against unrestricted quantum receivers.

The extraction mechanism, phase twirling, histogram simulation and original positive-state complement sampler are credited antecedents. The resulting dependence on phase alphabet and temporal persistence is the operational statement proved here.

Known source blocks, balanced support, fixed phase order and supplied-copy access are essential to the claim. A generic classical-data speedup, efficient preparation of an arbitrary random support state, unknown-boundary inference, receiver-memory optimality and hardware performance are not established.

[Model](model.md) · [Complete converse](phase-twirl-converse.md) · [Coherent recovery](coherent-recovery.md) · [Implementation](implementation.md) · [Interpretation](interpretation.md)

