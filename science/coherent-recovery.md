# Coherent recovery of a complement sample

[Model](model.md) · [Persistence frontier](persistence-frontier.md) · [Implementation](implementation.md)

The recovery step uses the exact finite-batch Hadamard-power instrument from [Quantum Coherent Collisions](https://github.com/GoGoKo699/Quantum-Coherent-Collisions/blob/219f590010247124f48feffaf244a60f306335f4/science/coherent_extraction.md). That instrument is an inherited construction. Here its powered output removes a finite alphabet of unknown phases, and a known diffuser converts the recovered subset state into a complement label. The phase-persistence frontier, including its classical-output converse, is proved separately in [the frontier](persistence-frontier.md).

Throughout, $`N=2M\ge2`$, the hidden subset $`S`$ has size $`M`$, and $`q\ge2`$ is fixed. One phase block supplies identical copies of

```math
|\psi\rangle=\sum_{x\in[N]}\alpha_x|x\rangle,
\qquad
\alpha_x=\begin{cases}
M^{-1/2}\omega_q^{z_x},&x\in S,\\
0,&x\notin S,
\end{cases}
\qquad \omega_q=e^{2\pi i/q}.
```

The processor receives copies only. It is not given a preparation circuit, an inverse, a reflection about the source, or a membership oracle for $`S`$.

## The finite-batch instrument

For $`b\ge q`$, let $`|n\rangle_{\mathrm{sym}}`$ be the normalized symmetric occupation state for a vector $`n\in\mathbb Z_{\ge0}^{N}`$ with $`\sum_xn_x=b`$. Identical copies have expansion

```math
|\psi\rangle^{\otimes b}
=\sum_{|n|=b}\sqrt{\frac{b!}{\prod_xn_x!}}
\left(\prod_x\alpha_x^{n_x}\right)|n\rangle_{\mathrm{sym}}.
```

Define

```math
C_q=\frac{(2q-1)!}{(q-1)!}.
```

For each residual occupation vector $`z`$ satisfying $`|z|=b-q`$ and $`0\le z_x<q`$, the successful Kraus operator is

```math
K_z=\sum_{x\in[N]}
\sqrt{\frac{(z_x+q)!}{z_x!\,C_q}}
|x\rangle\langle z+q e_x|_{\mathrm{sym}}.
```

It acts as zero outside the indicated symmetric occupations. A successful input occupation has one distinguished coordinate of size $`k\in\{q,\ldots,2q-1\}`$ and every other coordinate below $`q`$. The distinguished coordinate and its residual are unique. Consequently,

```math
\sum_zK_z^\dagger K_z
=\sum_{\substack{n\ \mathrm{accepted}\\x\ \mathrm{distinguished}}}
\frac{n_x!}{(n_x-q)!\,C_q}
|n\rangle_{\mathrm{sym}}\langle n|
\le I.
```

The inequality follows because the falling factorial $`k!/(k-q)!`$ is increasing and equals $`C_q`$ at $`k=2q-1`$. A failure effect completes a physical instrument. It does not depend on the unknown amplitudes.

For every accepted residual, the multiplicity factor cancels the multinomial coefficient:

```math
K_z|\psi\rangle^{\otimes b}
=\sqrt{\frac{b!}{C_q\prod_xz_x!}}
\left(\prod_x\alpha_x^{z_x}\right)
\sum_x\alpha_x^q|x\rangle.
```

Thus every successful branch has the same normalized output, proportional to the coordinatewise power $`\sum_x\alpha_x^q|x\rangle`$. If the residual is retained coherently, the successful joint vector factors into this output and one residual vector. The residual may therefore be discarded after the required cleanup. Measuring the distinguished label, or discarding a label-dependent sorting record, would destroy this argument.

For the root-phase source, $`\alpha_x^q=M^{-q/2}`$ on $`S`$. The exact normalized successful state is therefore

```math
|S\rangle=\frac1{\sqrt M}\sum_{x\in S}|x\rangle.
```

## Exact success probability

Let $`Q_q^{\mathrm{occ}}(L;M)`$ be the probability that no label occurs $`q`$ times among $`L`$ independent uniform draws from an $`M`$-element set. This occupancy probability is distinct from the project's copy complexity. With $`(b)_q=b(b-1)\cdots(b-q+1)`$, the complete instrument, including its eligibility test, succeeds with probability

```math
p_b=\frac{(b)_q}{C_qM^{q-1}}\,Q_q^{\mathrm{occ}}(b-q;M).
```

This is an exact finite identity. In particular, $`Q_q^{\mathrm{occ}}(0;M)=1`$ and

```math
p_q=\frac{q!}{C_qM^{q-1}}.
```

To obtain the formula, sum the squared branch norms and use

```math
\sum_{\substack{|z|=L\\z_x<q}}
\frac{L!}{\prod_xz_x!}\prod_x(M^{-1})^{z_x}
=Q_q^{\mathrm{occ}}(L;M).
```

The probability depends only on the magnitudes, so it is the same for every hidden subset and every permitted phase table. No averaging over the unknown phases is used for this upper bound.

An ordinary union bound gives

```math
Q_q^{\mathrm{occ}}(L;M)\ge1-\binom LqM^{1-q},
```

where $`\binom Lq=0`$ for $`L<q`$. Oversized batches need not improve success; the schedule below stays within a range where this lower bound is positive.

## From a subset state to a complement label

Prepare the known uniform state $`|u_N\rangle=N^{-1/2}\sum_x|x\rangle`$ and define its known reflection

```math
D_N=2|u_N\rangle\langle u_N|-I.
```

Since $`N=2M`$,

```math
D_N|S\rangle=\sqrt2|u_N\rangle-|S\rangle
=|\overline S\rangle.
```

Measuring the output label therefore gives a uniform element outside $`S`$. This balanced positive-subset diffuser is inherited from the complement-sampling protocol of [Benedetti, Buhrman and Weggemans](https://arxiv.org/html/2502.08721v3). The new source promise is what makes its positive input recoverable after phase disorder.

## A hard schedule with exact refresh boundaries

The source promises blocks of exactly $`B`$ copies, with known boundaries. If $`B<q`$, use the classical fallback below. Otherwise define the integer

```math
L_* =\max\{L\in\mathbb Z_{\ge0}:(2L)^q\le M^{q-1}\},
\qquad b_*=q+L_*,\qquad b=\min\{B,b_*\}.
```

These quantities are computed by integer arithmetic. Writing $`R=M^{1-1/q}`$, one has $`L_*=\lfloor R/2\rfloor`$. Hence $`b-q\le R/2`$, and the rational constant

```math
\xi_q=1-\frac1{2^q q!}>0
```

gives the known lower bound

```math
\beta_b=\xi_q\frac{(b)_q}{C_qM^{q-1}}
\le p_b\le\frac{\beta_b}{\xi_q}.
```

For a chosen constant $`0<\delta<1`$, choose an integer $`a_\delta\ge1`$ with $`2^{-a_\delta}\le\delta`$ and take

```math
J=a_\delta\left\lceil\frac1{\beta_b}\right\rceil.
```

Only rational and integer arithmetic is needed for the run length. One can take $`a_\delta=\lceil\log_2(1/\delta)\rceil`$, or compile any larger certified integer.

Run at most $`J`$ fresh $`b`$-copy attempts, stopping at the first successful flag. At each source block, pack

```math
h=\lfloor B/b\rfloor\ge1,\qquad r=B-hb<b
```

attempts. If another block is needed, consume and discard its $`r`$-copy tail before starting the next block. Stop without consuming a final unused tail. Every attempted batch is wholly inside one phase block. The deterministic copy cap is

```math
T_{\mathrm{coh}}
=Jb+\left\lfloor\frac{J-1}{h}\right\rfloor r
<2Jb.
```

This cap counts rejected attempts and discarded copies; there is no additive $`B`$ charge for a large final block. Fresh product copies make the conditional success probability $`p_b`$ after every failure, even when several attempts share one phase table. Thus

```math
\Pr[\text{all attempts fail}]=(1-p_b)^J
\le e^{-J\beta_b}\le e^{-a_\delta}\le2^{-a_\delta}\le\delta.
```

If all flags fail, output an independent uniform label, whose complement probability is $`1/2`$. Exact roots therefore give unconditional complement success at least $`1-\delta/2`$.

For fixed $`q`$ and fixed $`\delta`$, the inequalities $`(b)_q\ge(q!/q^q)b^q`$ and $`b_*=\Theta_q(R)`$ show

```math
T_{\mathrm{coh}}
=O_q\!\left(\max\{M^{1-1/q},(M/B)^{q-1}\}\right).
```

When that bound exceeds the classical cost, use the classical branch. All branch choices use known $`N,B,q`$ and the displayed deterministic caps.

## Classical fallback and small cases

Measure $`m=M`$ source copies in the known basis, collect their distinct observed labels, and output a uniformly random unobserved label. This uses no within-block phase coherence. If $`D`$ labels have been seen and $`Z=M-D`$ labels of $`S`$ remain unseen, the conditional complement probability is exactly $`M/(M+Z)`$. Since

```math
\mathbb EZ=M(1-1/M)^M\le Me^{-1},
```

convexity gives unconditional success at least $`1/(1+e^{-1})>2/3`$. For $`M=1`$, one observed label identifies the complement exactly. Output selection can be performed from the sorted observed list by selecting a uniformly random rank among the missing labels; it needs no coherent memory or quantum RAM.

Taking the cheaper of this $`M`$-copy branch and the coherent schedule establishes

```math
T=O_q\!\left(
\min\{N,\max\{N^{1-1/q},(N/B)^{q-1}\}\}
\right).
```

This includes $`B<q`$ and all finite $`N\ge2`$; constants may depend on the fixed phase order. No large-support or $`q\le M`$ assumption is needed. The lower bound and its minimax quantifiers are in [the converse](phase-twirl-converse.md).

## Fixed-width phase cells

Suppose instead that the phase on $`x\in S`$ is $`2\pi z_x/q+\delta_x`$, where $`|\delta_x|\le\eta/q`$ and $`0\le\eta<\pi/2`$. The same instrument has exactly the same probability $`p_b`$, and its successful state is

```math
|\phi\rangle=\frac1{\sqrt M}\sum_{x\in S}e^{iq\delta_x}|x\rangle.
```

After $`D_N`$, the probability of an outside label is

```math
\left|\frac1M\sum_{x\in S}e^{iq\delta_x}\right|^2
\ge\cos^2\eta=:s_\eta.
```

The inequality follows from the real part of every summand being at least $`\cos\eta`$. If $`s_\eta>2/3`$, choose the constant failure allowance

```math
\delta_\eta=
\frac{s_\eta-2/3}{4(s_\eta-1/2)}.
```

With a uniform label on total heralding failure, ideal unconditional success is at least

```math
s_\eta-\delta_\eta(s_\eta-1/2)
=\frac23+\frac34(s_\eta-2/3).
```

The remaining positive margin permits finite-gate synthesis as detailed in [implementation](implementation.md). The bound holds for every phase table in each cell, even if it changes adversarially at the declared refresh boundaries. It gives no tolerance to unequal magnitudes, mixed source copies, unknown boundaries, or fluctuations inside a block.
