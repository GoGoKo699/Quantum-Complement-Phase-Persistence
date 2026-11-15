# A converse for classical-output complement sampling

The lower bound must address a receiver that returns one classical label. A lower bound for recovering an entire coherent state would not suffice. The proof here compares the complete received many-copy state with a state generated from ordinary samples, before any receiver operation.

The two inherited ideas are phase averaging in the symmetric occupation basis and coherent preparation of a sampled histogram. The additional use is a quantitative bound on complement-sampling success across source refresh blocks. Attribution and source-level comparisons appear in [related work](../references/related-work.md).

Throughout, $`N=2M`$, $`|S|=M`$, the integer $`q\ge2`$ is fixed, and phase tables persist for exactly $`B`$ source calls as specified in the [model](model.md). All trace distances use

```math
D(\rho,\sigma)=\frac12\|\rho-\sigma\|_1.
```

## 1. One block in the occupation basis

Fix a support $`S`$ and a block of $`t`$ copies. An occupation vector is a collection

```math
n=(n_x)_{x\in S},
\qquad
n_x\in\mathbb Z_{\ge0},
\qquad
\sum_{x\in S}n_x=t.
```

Let $`|n\rangle_{\mathrm{sym}}`$ be the normalized uniform superposition of all ordered label strings with those occupations. These vectors form an orthonormal basis of the symmetric subspace on the support.

Define the multinomial weight

```math
p_n=\frac{t!}{M^t\prod_{x\in S}n_x!}.
```

It is exactly the probability that $`t`$ independent uniform labels from $`S`$ have histogram $`n`$. Consequently,

```math
\sum_n p_n=1.
```

For a fixed root-phase table,

```math
|\psi_{S,z}\rangle^{\otimes t}
=
\sum_n
\sqrt{p_n}\,
\omega_q^{\sum_x n_xz_x}
|n\rangle_{\mathrm{sym}}.
```

Let the operational state of one block, averaged over independent uniform root phases, be

```math
\Omega_{q,S}^{(t)}
=
\mathbb E_z
\left[
\left(
|\psi_{S,z}\rangle\langle\psi_{S,z}|
\right)^{\otimes t}
\right].
```

Orthogonality of the characters of $`\mathbb Z_q`$ gives the exact identity

```math
\Omega_{q,S}^{(t)}
=
\sum_{\substack{n,m\\
n_x\equiv m_x\pmod q\;\forall x}}
\sqrt{p_np_m}\,
|n\rangle_{\mathrm{sym}}
\langle m|_{\mathrm{sym}}.
\tag{1}
```

By comparison, independent uniform continuous phases at each address give

```math
\Gamma_S^{(t)}
=
\sum_n p_n
|n\rangle_{\mathrm{sym}}
\langle n|_{\mathrm{sym}}.
\tag{2}
```

The phase vector is drawn once for the whole block in both equations. Equation (2) is generally not diagonal in the ordered computational basis: permutations of the same histogram remain coherent.

## 2. Which coherences require a repeated label?

Call an occupation vector good when every label occurs fewer than $`q`$ times. Let

```math
\Pi_{\mathrm{good}}
=
\sum_{\max_x n_x<q}
|n\rangle_{\mathrm{sym}}
\langle n|_{\mathrm{sym}},
\qquad
\Pi_{\mathrm{bad}}=I_{\mathrm{sym}}-\Pi_{\mathrm{good}}.
```

**Lemma 1 — uniqueness below a $`q`$-fold repetition.**  
If $`n`$ is good, $`m`$ has the same total occupation, and $`m_x\equiv n_x\pmod q`$ for all $`x`$, then $`m=n`$.

**Proof.** Write $`m_x=n_x+qk_x`$ with integers $`k_x`$. Since $`0\le n_x<q`$ and $`m_x\ge0`$, a negative $`k_x`$ is impossible. Thus all $`k_x\ge0`$. Equality of the total occupations gives $`q\sum_xk_x=0`$, so every $`k_x=0`$. $`\square`$

The lemma has two consequences. First, the good-good blocks of (1) and (2) are identical. Second, the root-phase state has no good-bad cross terms: a good occupation cannot be congruent to a distinct bad occupation with the same total.

Therefore both states have the decomposition

```math
\begin{aligned}
\Omega_{q,S}^{(t)}
&=G_{S,t}+A_{S,t},\\
\Gamma_S^{(t)}
&=G_{S,t}+C_{S,t},
\end{aligned}
\tag{3}
```

where all three operators are positive, $`G_{S,t}`$ is supported on the good subspace, and $`A_{S,t},C_{S,t}`$ are supported on the bad subspace. Their common residual trace is

```math
\operatorname{Tr}A_{S,t}
=
\operatorname{Tr}C_{S,t}
=
P_q(t;M),
```

with

```math
P_q(t;M)
=
\Pr[\text{some label appears at least }q\text{ times
among }t\text{ uniform draws from }S].
```

The diagonal entries in (1) and (2) are both $`p_n`$, which proves this trace statement. It follows that

```math
\begin{aligned}
D\!\left(\Omega_{q,S}^{(t)},\Gamma_S^{(t)}\right)
&=\frac12\|A_{S,t}-C_{S,t}\|_1\\
&\le\frac12
\left(\operatorname{Tr}A_{S,t}
+\operatorname{Tr}C_{S,t}\right)\\
&=P_q(t;M).
\end{aligned}
\tag{4}
```

This argument does not discard a postselected bad event. It compares the full normalized states.

For any chosen $`q`$ sample positions, the probability that all their labels agree is $`M^{1-q}`$. The union bound gives

```math
P_q(t;M)
\le
\min\!\left\{1,\binom tq M^{1-q}\right\},
\tag{5}
```

where $`\binom tq=0`$ for $`t<q`$.

Equations (4)–(5) show why the relevant phase order is $`q`$. Until a label can occur $`q`$ times, the finite-phase source carries exactly the same information as the continuous-phase source. The distinction is not controlled by a one-copy coherence parameter.

## 3. Continuous-phase copies are generated from ordinary samples

Draw $`t`$ independent labels from $`S`$, compute their histogram $`n`$, and prepare the known state $`|n\rangle_{\mathrm{sym}}`$. The resulting average state is exactly (2).

This preparation depends on the observed labels and their multiplicities, not on any unseen part of $`S`$. It may use coherent permutations and source-independent quantum operations. Goyal, Malavolta and Roberts established this exact correspondence for random-phase coupon states; finite phase modulus greater than the copy count already reproduces the continuous-phase moment. The present proof uses that correspondence as an inherited ingredient.

For a sample-complexity lower bound, the cost of the simulator's subsequent computation is immaterial. Even granting arbitrary quantum computation after receipt of ordinary classical labels cannot reveal membership information absent from those labels.

## 4. Several independently refreshed phase blocks

Suppose a hard-budget experiment acquires $`T`$ source outputs, with observed block lengths $`t_1,\ldots,t_J`$. Under the lower-bound prior, the phase tables are independent between blocks. Conditional on $`S`$, the two comparison states are

```math
\Omega_{q,S}^{\mathbf t}
=
\bigotimes_{j=1}^{J}\Omega_{q,S}^{(t_j)},
\qquad
\Gamma_S^{\mathbf t}
=
\bigotimes_{j=1}^{J}\Gamma_S^{(t_j)}.
```

A telescoping replacement of the tensor factors, together with trace-norm multiplicativity on tensor products with a state, gives

```math
D\!\left(
\Omega_{q,S}^{\mathbf t},
\Gamma_S^{\mathbf t}
\right)
\le
\sum_{j=1}^{J}
D\!\left(
\Omega_{q,S}^{(t_j)},
\Gamma_S^{(t_j)}
\right).
```

Thus the full-state comparison is

```math
D\!\left(
\Omega_{q,S}^{\mathbf t},
\Gamma_S^{\mathbf t}
\right)
\le
\Delta_q(\mathbf t;M)
:=
\min\!\left\{
1,\,
\frac{1}{M^{q-1}}
\sum_{j=1}^{J}\binom{t_j}{q}
\right\}.
\tag{6}
```

The reference state $`\Gamma_S^{\mathbf t}`$ is generated from exactly $`T`$ ordinary samples, grouped according to the known block boundaries. The hidden support is the same in all blocks, and the simulator preserves that dependence through the ordinary sample distribution.

Every allowed receiver is a channel followed by a classical readout. Trace-distance contractivity therefore bounds the change in each final success probability by (6), including receivers with quantum memory and coherent processing across blocks.

Two useful estimates are

```math
\sum_j\binom{t_j}{q}
\le
\frac{1}{q!}\sum_j t_j^q
\le
\frac{T^q}{q!},
\tag{7}
```

and, because $`t_j\le B`$,

```math
\sum_j\binom{t_j}{q}
\le
\frac{1}{q!}\sum_j t_j B^{q-1}
=
\frac{T B^{q-1}}{q!}.
\tag{8}
```

The first estimate retains the globally frozen collision scale. The second charges the finite number of coherent repetitions available before a phase refresh.

If $`B<q`$, every observed block has fewer than $`q`$ copies, so each term in (6) vanishes exactly. In that regime the entire phase-averaged root source is simulable from ordinary samples, for every total budget.

## 5. The ordinary-sample posterior bound

Choose $`S`$ uniformly among all $`M`$-element subsets of $`[N]`$. After observing an ordered sequence of ordinary samples, let $`D`$ be its set of distinct labels and $`d=|D|`$.

The likelihood of the particular sequence is $`M^{-T}`$ for every support containing $`D`$ and zero otherwise. Hence the posterior support is uniform among all balanced sets containing $`D`$.

A label in $`D`$ is certainly in $`S`$. For every label $`y\notin D`$,

```math
\Pr[y\notin S\mid\text{sample transcript}]
=
\frac{N-M}{N-d}
=
\frac{M}{N-d}.
\tag{9}
```

Any randomized decision, including one produced by arbitrary quantum processing of that classical transcript, is a mixture of possible output labels. It cannot exceed the largest posterior success probability. Since $`d\le T`$, for $`T<N`$ the ordinary-sample success is at most

```math
C_T
\le
\min\!\left\{
1,\frac{M}{N-T}
\right\}.
\tag{10}
```

This is the established complement-sampling posterior argument. The bound is deliberately simple; repeated samples only make it looser.

## 6. A finite success bound for every quantum receiver

Combining (6) and (10), averaging over the uniform support prior, and applying contractivity proves the following statement.

**Theorem 2 — success under a hard acquisition cap.**  
For $`T<N`$, every receiver using at most $`T`$ specimens satisfies

```math
\boxed{
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
}
\tag{11}
```

The right side may additionally be capped by one. The probability on the left averages the initial support and phase tables under the stated prior, together with the receiver's own randomness and measurements.

The theorem includes arbitrary collective measurements and arbitrary source-independent ancillas. A receiver that stops before its cap is supplied the unused source suffix and ignores it. Its final channel is therefore still covered by the full $`T`$-register comparison. All observed block lengths in (11) then refer to that padded prefix.

No assumption is made that the receiver itself uses an occupation measurement or a collision algorithm.

## 7. Extracting the optimal asymptotic order

Put

```math
R=M^{1-1/q},
\qquad
L=\frac{M^{q-1}}{B^{q-1}},
\qquad
F_q(N,B)=\min\{N,\max\{R,L\}\}.
```

Suppose an allowed receiver has success at least $`2/3`$ for every support and phase-table sequence. It has at least that average success under the lower-bound prior.

If $`T>N/8`$, then immediately $`T\ge F_q(N,B)/8`$. Otherwise,

```math
\frac{M}{N-T}
\le \frac47.
```

Equation (11) then requires

```math
\Delta_q(\mathbf t;M)
\ge
\frac23-\frac47
=
\frac{2}{21}.
```

Using both (7) and (8),

```math
T
\ge
\left(\frac{2q!}{21}\right)^{1/q}R,
\qquad
T
\ge
\frac{2q!}{21}L.
```

There is therefore a positive constant depending only on fixed $`q`$ for which

```math
T\ge c_q F_q(N,B).
\tag{12}
```

Replacing $`M=N/2`$ by $`N`$ inside the powers changes only $`q`$-dependent constants. Thus

```math
Q_q(N,B)
=
\Omega_q\!\left(
\min\!\left\{
N,\,
\max\!\left\{
N^{1-1/q},
\left(\frac NB\right)^{q-1}
\right\}
\right\}
\right).
```

The [coherent-recovery construction](coherent-recovery.md) gives the matching upper bound, including failed attempts and discarded boundary tails.

## 8. Continuous and refreshed phases

For continuous independent uniform phases within each source block, the received state is already $`\Gamma_S^{\mathbf t}`$. There is no comparison error. Equation (10) alone implies $`T\ge N/4`$ for average success $`2/3`$. Ordinary basis measurement and an unseen-label rule use $`O(N)`$ samples, so the order is $`\Theta(N)`$ for every $`B`$.

For independently refreshed root phases, $`B=1<q`$ and the finite-phase comparison is also exact. In fact each averaged register is diagonal, so the source is directly equivalent to ordinary samples.

These arguments do not assert that a single realized pure continuous-phase state is mixed. They concern the information available when the hidden table is unknown and drawn according to the lower-bound prior.

## 9. What is new in the converse

The occupation-residue method is inherited. Binary-phase subset-state moment comparisons already use collision-free types, and the continuous-phase histogram simulator is an established exact construction.

The lower bound established here is for **one complement label**, not for coherent amplitude powering, tomography or identification of the support. The finite phase alphabet and the known persistence length jointly determine when this classical-output task escapes the ordinary-sample posterior bound. That conclusion requires the receiving task and output payoff in Sections 5–7; it does not follow from a state-transformation lower bound alone.

[Source model](model.md) · [Frontier](persistence-frontier.md) · [Attaining recovery](coherent-recovery.md)

