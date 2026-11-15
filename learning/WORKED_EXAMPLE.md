# Four labels: the same one-copy state, different two-copy states

This example uses the density-operator, instrument and symmetric-space language connected to the selected Watrous 2018 anchor in the [bridge](WATROUS_BRIDGE.md). It is a complete finite calculation, not evidence for an asymptotic lower bound or for a sample advantage at this small size.

Let $`N=4`$, $`M=2`$, $`q=2`$ and, for the calculation, take

```math
S=\{0,1\},\qquad \bar S=\{2,3\}.
```

The receiver is not told $`S`$. Fixing its labels here merely makes the states and output probabilities visible; the displayed receiver operations do not depend on that choice.

## 1. Positive input and every diffuser output

The positive subset state and known uniform state are

```math
|S\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2},
\qquad
|u_4\rangle=\frac{|0\rangle+|1\rangle+|2\rangle+|3\rangle}{2}.
```

The established balanced-subset diffuser is

```math
D_4=2|u_4\rangle\langle u_4|-I
=\frac12
\begin{pmatrix}
-1&1&1&1\\
1&-1&1&1\\
1&1&-1&1\\
1&1&1&-1
\end{pmatrix}.
```

Direct multiplication gives

```math
D_4|S\rangle=\frac{|2\rangle+|3\rangle}{\sqrt2}.
```

For signs, a global sign has no effect on a density operator, so the independent uniform sign prior can be written as a uniform relative sign $`r\in\{+1,-1\}`$ with

```math
|\psi_r\rangle=\frac{|0\rangle+r|1\rangle}{\sqrt2}.
```

The plus input is the positive state above. The minus input is orthogonal to $`|u_4\rangle`$, hence $`D_4|\psi_{-1}\rangle=-|\psi_{-1}\rangle`$. All four measurement probabilities after diffusion are:

| Input to the diffuser | Output 0 | Output 1 | Output 2 | Output 3 | Complement probability |
| --- | --- | --- | --- | --- | --- |
| $`\lvert\psi_{+1}\rangle`$ | $`0`$ | $`0`$ | $`1/2`$ | $`1/2`$ | $`1`$ |
| $`\lvert\psi_{-1}\rangle`$ | $`1/2`$ | $`1/2`$ | $`0`$ | $`0`$ | $`0`$ |
| Uniform hidden sign prior | $`1/4`$ | $`1/4`$ | $`1/4`$ | $`1/4`$ | $`1/2`$ |

Thus applying the positive-state protocol directly to an unknown-sign specimen does not preserve its guarantee. The diffuser and the original positive-state complement task are inherited from Benedetti, Buhrman and Weggemans; see [related work](../references/related-work.md).

## 2. Compute the one-copy average

The two pure-state matrices have opposite off-diagonal entries. Their average is

```math
\rho_S
=\frac12|\psi_{+1}\rangle\langle\psi_{+1}|
 +\frac12|\psi_{-1}\rangle\langle\psi_{-1}|
=\frac12|0\rangle\langle0|
 +\frac12|1\rangle\langle1|.
```

Every individual emission has this averaged state whether its hidden signs will be reused or independently refreshed. That agreement does not fix the joint state of two emissions.

## 3. Freeze the signs for two calls

Suppose both calls belong to one known phase block, so $`B\ge2`$ and the same $`r`$ is used. Write

```math
|a\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2},
\qquad
|b\rangle=\frac{|01\rangle+|10\rangle}{\sqrt2}.
```

Then

```math
|\psi_r\rangle^{\otimes2}
=\frac12\bigl(|00\rangle+r|01\rangle+r|10\rangle+|11\rangle\bigr)
=\frac{|a\rangle+r|b\rangle}{\sqrt2}.
```

Averaging the fixed sign gives

```math
\Omega_{2,S}^{(2)}
=\frac12|a\rangle\langle a|+\frac12|b\rangle\langle b|
=\frac14
\begin{pmatrix}
1&0&0&1\\
0&1&1&0\\
0&1&1&0\\
1&0&0&1
\end{pmatrix},
```

where the displayed basis is $`00,01,10,11`$; all other two-register basis entries have zero weight. In particular,

```math
\langle00|\Omega_{2,S}^{(2)}|11\rangle=\frac14.
```

The coherence survives because its phase factor is the square of a sign. In occupation language, $`(2,0)`$ and $`(0,2)`$ have the same coordinatewise residues modulo two.

## 4. Refresh the signs at every call

If the tables are independently redrawn for each call, the joint average is

```math
\rho_S\otimes\rho_S
=\frac14\left(
|00\rangle\langle00|+|01\rangle\langle01|
+|10\rangle\langle10|+|11\rangle\langle11|
\right).
```

Now the $`|00\rangle\langle11|`$ entry is zero. The $`|01\rangle\langle10|`$ entry is also zero: the two source calls no longer share a relative sign.

The frozen state is supported on symmetric vectors. The refreshed state commutes with swapping the registers, but has weight $`1/4`$ on the antisymmetric vector $`(|01\rangle-|10\rangle)/\sqrt2`$. Commuting with a permutation is therefore weaker than being supported on its invariant-vector subspace.

As an exact comparison at this fixed support,

```math
D\!\left(\Omega_{2,S}^{(2)},\rho_S^{\otimes2}\right)=\frac12.
```

Indeed, their difference has four eigenvalues $`1/4,1/4,-1/4,-1/4`$ on the displayed subspace. This distinguishes joint states; it is not a complement-sampling lower bound with an unknown support.

For comparison, phases drawn uniformly from the circle and then frozen for the pair give

```math
\Gamma_S^{(2)}
=\frac14|00\rangle\langle00|
 +\frac12|b\rangle\langle b|
 +\frac14|11\rangle\langle11|.
```

It retains the permutation coherence inside $`|b\rangle`$ but loses the coherence between different occupations. Thus continuous-phase averaging is not the same operation as independently dephasing every emission. In this example $`D(\Omega_{2,S}^{(2)},\Gamma_S^{(2)})=1/4`$, below the converse's collision bound $`\binom22/M=1/2`$.

## 5. Recover coherently: two filters with different probabilities

The inherited general-batch instrument in [coherent recovery](../science/coherent-recovery.md) has

```math
C_2=\frac{3!}{1!}=6.
```

For $`b=q=2`$, the only residual occupation is zero, so its success operator reduces to

```math
K_0=\frac1{\sqrt3}\sum_{x=0}^{3}|x\rangle\langle xx|.
```

For either fixed sign,

```math
K_0|\psi_r\rangle^{\otimes2}
=\frac{|0\rangle+|1\rangle}{2\sqrt3}
=\frac1{\sqrt6}|S\rangle.
```

Its success probability is therefore

```math
p_2=\frac{(2)_2}{C_2M}
=\frac{2}{6M}
=\frac1{3M}
=\frac16.
```

On the successful branch, the known diffuser gives a complement label with certainty. The success record reveals no surviving label, so the relative coherence needed by the diffuser remains.

There is also a stronger filter for this particular two-copy case:

```math
A=\sum_{x=0}^{3}|x\rangle\langle xx|,
\qquad
A^\dagger A=\sum_x|xx\rangle\langle xx|\le I.
```

It succeeds with probability $`1/M=1/2`$ and has the same normalized powered output on frozen-sign inputs. It is the unscaled coherent equality filter, not the $`K_0`$ operator of the general-batch construction. Hence $`1/M`$ must not be substituted into that construction's stated success formula. Reading both labels and recording which equal label occurred would also have equality probability $`1/M`$, but would destroy the coherent recovered state.

On independently refreshed inputs, the coherent equality filter succeeds with the same probability, yet its average successful output is $`\rho_S`$, not $`|S\rangle\langle S|`$. Equal labels alone are insufficient; persistence is what makes the signs cancel coherently.

## 6. Include failure branches and ordinary samples

Complete the inherited $`K_0`$ instrument with failure, and on failure return an independent uniform label. This gives a hard two-copy protocol with every run returning an answer. Its four output probabilities are

```math
(\Pr[Y=0],\Pr[Y=1],\Pr[Y=2],\Pr[Y=3])
=\left(\frac5{24},\frac5{24},\frac7{24},\frac7{24}\right).
```

The unconditional complement probability is $`7/12`$, not one. Certainty applies only after the success flag.

Three fresh two-copy attempts using the inherited operator, with a uniform label only if all fail, have success

```math
1-\frac12(1-1/6)^3
=\frac{307}{432}>\frac23.
```

For exact blocks of length $`B=2`$, this has a hard six-copy cap. For $`B=3`$, each failed block leaves one specimen to acquire and discard before the next attempt, so the cap becomes eight copies. Those tails count even though the receiver does not use them. At $`B=1`$, no pair of consecutive calls has the promised frozen signs, so this recovery argument cannot be applied.

The small example also makes clear why a successful coherent branch is not itself a copy advantage. Measure one ordinary specimen and return a uniformly chosen different label. For every balanced support, two of the remaining three labels lie outside $`S`$, giving unconditional success exactly $`2/3`$. For the fixed support used here its output probabilities are $`(1/6,1/6,1/3,1/3)`$.

Under a uniform prior over the six balanced supports, this is also the optimal one-copy averaged success: after seeing one supported label, all three unobserved labels have posterior complement probability $`2/3`$. Two ordinary draws followed by a uniform unobserved label give success $`5/6`$: equal observations occur with probability $`1/2`$ and give success $`2/3`$, while distinct observations reveal the whole support and give success one.

These finite values illustrate source correlations, coherent cancellation, unconditional success and charged acquisition. The fixed-$`q`$, growing-$`N`$ optimal law requires the full [frontier proof](../science/persistence-frontier.md). The known basis, balanced size and exact block boundaries remain assumptions; no hidden-set oracle, source inverse, reflection, preparation program or free data loading has been introduced.

[Watrous bridge](WATROUS_BRIDGE.md) · [Source model](../science/model.md) · [Converse](../science/phase-twirl-converse.md) · [Recovery and schedule](../science/coherent-recovery.md)
