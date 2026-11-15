# Implementation and complete resource accounting

[Coherent recovery](coherent-recovery.md) · [Model](model.md) · [Persistence frontier](persistence-frontier.md)

The algorithm consumes supplied quantum examples. Its copy law is not a claim that an arbitrary hidden subset state can be prepared efficiently. This page charges the processing after acquisition, including rejected attempts, phase-block tails, coherent workspace and finite-gate approximation.

The occupation compiler is inherited from [Quantum Coherent Collisions, implementation Sections 2–7](https://github.com/GoGoKo699/Quantum-Coherent-Collisions/blob/219f590010247124f48feffaf244a60f306335f4/science/implementation.md). Its coherent symmetrization dependency is [Liu, Childs and Gottesman, *Low-Depth Quantum Symmetrization*, Result 2 and Section IV](https://journals.aps.org/prx/pdf/10.1103/9qhy-ms2y). The application here transfers that compiler to the fixed phase order $`q`$; it does not introduce a new symmetrizer or a new collision extractor.

## The coherent circuit for one batch

Use $`b\ge q`$ identical copies from one declared phase block. The circuit has two measured Boolean flags, with every label-dependent work record cleared before either flag is measured.

1. **Eligibility.** Reversibly sort the $`b`$ label registers and retain the comparison records. Scan the sorted list to test that exactly one run has length at least $`q`$ and no run has length at least $`2q`$. Copy only this Boolean predicate to a flag, then reverse the scan and sort. Measure the flag. Reject the batch when it is zero. Because eligibility is permutation invariant, a successful flag preserves the symmetric occupation amplitudes.
2. **Clean occupation compression.** Apply the inverse of the inherited coherent symmetrizer. On the accepted subspace, it maps each normalized symmetric occupation state to its sorted list with clean work registers. This is stronger than sorting and discarding the comparison record.
3. **Remove the distinguished run.** Reversibly scan for the unique run of length $`k\in\{q,\ldots,2q-1\}`$, starting at position $`a`$. For $`j=1,\ldots,b-q`$ in increasing order, swap label registers $`j`$ and $`j+q`$ controlled on $`a\le j`$. The first $`b-q`$ registers become the sorted residual list; the last $`q`$ contain the distinguished label. Copy that label coherently into the output and XOR it out of all tail registers.
4. **Multiplicity correction.** On a fresh flag, apply the known rotation with successful amplitude

```math
a_k=\sqrt{\frac{k!}{(k-q)!\,C_q}},
\qquad C_q=\frac{(2q-1)!}{(q-1)!}.
```

5. **Cleanup and readout.** Recompute the original records from the output label $`x`$ and the residual list $`z^{\rm list}`$:

```math
a=1+\#\{j:z_j^{\rm list}<x\},
\qquad
k=q+\#\{j:z_j^{\rm list}=x\}.
```

XOR these values into the old records and reverse the recomputation. Measure the multiplicity flag. On success, apply the known diffuser $`D_N`$ and measure the output label. The successful output factors from the residual by the identity in [coherent recovery](coherent-recovery.md), so the residual can now be discarded.

Each scan uses comparisons against explicitly held fixed-position label registers. No coherently addressed external array or quantum RAM is assumed. A rejected batch still consumes all $`b`$ copies.

### Why compression is a charged subroutine

The inherited repeated-list symmetrizer separates a uniform global permutation resource from the stabilizer permutations within equal-label runs. Global permutation resources use known integer ranges up to $`b`$. On the accepted subspace every run has length at most $`2q-1`$, so its stabilizer state has constant dimension for fixed $`q`$. Conditional preparation at each possible run start, followed by inverse preparation, erases the run-dependent permutation information coherently.

The stabilizer size of an occupation is $`\prod_xn_x!`$. Its normalized resource is essential: after cleanup the coefficient of each distinct ordering is $`\sqrt{\prod_xn_x!/b!}`$, producing the normalized symmetric occupation state. The inverse therefore preserves each occupation coefficient instead of inserting an uncharged multiplicity-dependent normalization. Source-dependent phases and permutation records are not discarded during this step.

## Ideal gates, width and depth

Set

```math
n=\lceil\log_2 N\rceil,
\qquad \ell=\lceil\log_2(b+1)\rceil.
```

The ideal model allows known one-qubit rotations and bounded-arity reversible gates with unrestricted connectivity. The inherited conservative batch bounds are

```math
G_0(b,N)=O_q\!\left(
b(n+\ell^2)\ell^4\log(n+\ell+2)
\right),
\qquad
W_0(b,N)=O_q\!\left(b(n+\ell^2)\right).
```

Known-range state preparations, bitonic sorting records, coherent compression, the multiplicity rotation and all cleanup are included. These are upper bounds, not optimal gate or width claims. Sequential extraction has depth $`O_q(b(n+\ell))`$; a conservative bound for the complete batch is $`D_0\le G_0`$. No polylogarithmic complete-depth claim is made.

For $`N=2^n`$, the diffuser uses Hadamards, a computational-basis reflection and inverse Hadamards. For a general known even $`N`$, prepare the uniform superposition on the first $`N`$ labels by known-range binary rotations, reflect about the zero state, and unprepare. The known-range circuit has polynomial logarithmic cost. It uses no information about $`S`$ and fits the displayed conservative bound. Unused computational labels have zero ideal amplitude.

The hard schedule has at most $`J`$ attempted batches and fewer than $`Jb`$ discarded tail copies. They can be consumed and disposed of sequentially; only $`b`$ source registers must be stored coherently together. Choose the classical branch whenever its $`M`$-copy cap is smaller. No executed branch then acquires more than $`M`$ copies, so its scheduling logic needs only $`\min\{B,M\}`$: a declared block longer than the entire run requires no stored long boundary counter. Thus ideal processing uses

```math
O_q\!\left(T\,\mathrm{polylog}(N)\right)
```

gates, where $`T`$ is the charged deterministic copy cap, and peak coherent width $`W_0(b,N)`$. Block counters and schedule arithmetic use ordinary classical memory. Persistent quantum storage across failed batches is unnecessary.

## Finite universal gates: rare success must be included

Exact extraction refers to ideal known rotations. A finite universal gate set implements an approximate flagged instrument, so the flag alone does not certify an exact powered state.

Let $`\tau`$ bound the operator-norm approximation error of all coherent stages of one batch together, including their relative controlled phases and the diffuser. Standard unitary telescoping achieves this by approximating each of at most $`O(G_0)`$ gates to error $`O(\tau/G_0)`$. One may assign half the error allowance to each side of the intermediate eligibility measurement. Measurements and discards contract trace distance.

For an ideal successful subnormalized output $`A`$ of trace $`p_b`$ and the corresponding synthesized output $`\widetilde A`$, conservative bounds are

```math
\|A-\widetilde A\|_1\le2\tau,
\qquad
|p_b-\operatorname{Tr}\widetilde A|\le2\tau.
```

Consequently, provided $`2\tau<p_b`$,

```math
D\!\left(
\frac{\widetilde A}{\operatorname{Tr}\widetilde A},
\frac A{p_b}\right)
\le\frac{2\tau}{p_b-2\tau}.
```

In particular, $`\tau\le\beta_b\varepsilon_{\rm out}/8`$ guarantees conditional trace error at most $`\varepsilon_{\rm out}`$ and preserves a positive fraction of the ideal heralding probability, because $`\beta_b\le p_b`$. Constant operator error is insufficient for a rare batch. The correct allowance is proportional to its success probability.

### Control the entire hard schedule

The schedule contains at most $`J`$ batches, and stops adaptively at the first accepted flag. Approximation must cover failed attempts and the possibility that their flags change. A hybrid over this complete adaptive instrument gives total output trace distance at most $`2J\tau`$ from the ideal schedule, uniformly over all allowed phase tables. Thus choose

```math
\tau\le
\min\left\{
\frac{\varepsilon_{\rm run}}{2J},
\frac{\beta_b\varepsilon_{\rm out}}8
\right\}.
```

This is a finite known precision prescription. For the fixed target confidence, $`J=O_q(1/\beta_b)`$ and $`p_b/\beta_b\in[1,1/\xi_q]`$, so it requires only $`\tau=O_q(p_b\min\{\varepsilon_{\rm run},\varepsilon_{\rm out}\})`$ up to fixed constants. It controls the unconditional success probability of the whole run; it does not condition an error estimate on whichever rare transcript happened to be observed.

For the phase-cell guarantee, take $`s_\eta=\cos^2\eta>2/3`$ and the failure allowance $`\delta_\eta`$ from coherent recovery. The ideal total success is at least $`2/3+3(s_\eta-2/3)/4`$. Choosing $`\varepsilon_{\rm run}\le(s_\eta-2/3)/4`$ leaves success strictly above $`2/3`$. Exact roots are the case $`s_\eta=1`$. These margins can also absorb a bounded classical random-selection approximation at the final fallback.

The [Dawson–Nielsen Solovay–Kitaev construction](https://arxiv.org/abs/quant-ph/0505030) gives the conservative finite-gate batch cost

```math
G_{\rm fin}
=O_q\!\left[
G_0(b,N)
\log^4\!\left(2+\frac{G_0(b,N)}{\tau}\right)
\right].
```

Controlled operations require a consistent matrix representative: approximating a gate only up to an arbitrary global phase can create a relative phase between control branches. The stated operator-norm prescription fixes those phases before controlled compilation.

In the chosen batch range, $`\beta_b\ge c_qM^{-(q-1)}`$ and $`J\le C_{q,\eta}M^{q-1}`$. Hence $`\log(1/\tau)=O_{q,\eta}(\log N+\log(1/\varepsilon_{\rm out})+\log(1/\varepsilon_{\rm run}))`$. For fixed phase order and fixed phase-cell margin, finite synthesis therefore retains total processing cost

```math
O_{q,\eta}\!\left(
T\,\mathrm{polylog}(N/\varepsilon)
\right),
```

by taking $`\varepsilon_{\rm out}=\varepsilon_{\rm run}=\varepsilon`$ subject to the fixed success margin above. The result is a quantified approximation in otherwise ideal gates, flags and supplied copies. It is not a hardware-noise or imperfect-source theorem.

## Acquisition and classical costs

| Resource | What is charged |
|---|---|
| Supplied examples | Every attempted copy and each discarded source-block tail; cap $`T`$ |
| Source preparation | If one example costs $`C_{\rm prep}`$, acquisition costs $`T C_{\rm prep}`$; no bound on this cost is assumed |
| Coherent memory | $`W_0(b,N)`$ qubits for the realized fixed batch, including data and cleanable work registers |
| Gates | The inherited occupation compiler, cleanup, known diffuser and the finite-synthesis overhead above |
| Classical fallback | $`M`$ basis measurements; sorting/deduplicating their labels and selecting a missing rank in $`O(M\,\mathrm{polylog}(N))`$ bit operations |
| Schedule | Known-boundary counters and integer comparisons, with polynomial logarithmic classical overhead |

The classical branch never needs to wait for a phase refresh. The coherent branch assumes that examples can be acquired in sequence and held until the batch is complete. Acquisition duration, physical storage lifetime and a particular architecture's routing cost are distinct from the supplied-copy cap. A source with only an upper bound on persistence could refresh after every copy and would not support the attaining schedule.

The processing bounds establish that the copy frontier is compatible with explicit source-independent circuits of near-linear cost in the acquired examples, up to logarithms. They do not establish an end-to-end runtime advantage for preparing arbitrary hidden subsets, nor a separation against classical algorithms given an executable description or membership oracle for that subset.
