# Thirty milestones for phase persistence in complement sampling

This map follows one scientific question: **how long must an unknown phase pattern persist for collective quantum samples to help produce an element outside their own support?** Read it together with the [Watrous bridge](WATROUS_BRIDGE.md), the [worked example](WORKED_EXAMPLE.md), and the [scientific overview](../science/README.md).

There are exactly **30 milestones**: **12 background / preliminaries** milestones and **18 narrative / innovation** milestones. The first twelve establish the distinctions needed to read this particular source experiment: classical support versus quantum phase, a hidden table versus independent noise, full-state comparison versus one output event, and sample count versus a source clock. The remaining eighteen connect those foundations to the complete lower bound, the inherited recovery instrument, the refresh schedule, robustness, and resource accounting. “Narrative / innovation” names a part of the learning route; it does not claim that every ingredient in that part is new.

The educational anchor is John Watrous, *The Theory of Quantum Information* (2018), using the author's [available manuscript and chapter files](https://cs.uwaterloo.ca/~watrous/TQI/). The precise anchor pointers below were checked in the official chapters:

- **W2-states:** section 2.1.2, pp. 61–66: density operators, convex mixtures, pure states and composite systems.
- **W2-channels:** sections 2.2.1–2.2.2, pp. 72–90: channels and their representations, including Kraus operators.
- **W2-readout:** section 2.3.1, pp. 100–104, and section 2.3.2, pp. 105–113: measurements; the subsection “Nondestructive measurements and instruments,” pp. 111–113, supplies the flagged-process language.
- **W3-distance:** section 3.1.1, beginning p. 125: state discrimination, Theorem 3.4 and Proposition 3.5.
- **W7-symmetry:** section 7.1.1, beginning p. 391: permutation-invariant vectors, Proposition 7.1 and the symmetric occupation/bag basis beginning p. 393.

The chapter files are [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), [Chapter 3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf), and [Chapter 7](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf). The manuscript page numbers identify the inspected layout. The bridge explains how these foundations enter the project; Watrous does not state the phase-persistence frontier, the complement posterior bound, or the project's collision-recovery schedule.

## Background / preliminaries — M01 to M12

### M01 — One label outside a hidden set

- **Phase:** Background / preliminaries.
- **Central question:** What is actually returned by a complement sampler?
- **Understanding target:** Specify a universe of size $`N=2M`$, a hidden support of size $`M`$, one classical output label, and unconditional success at least $`2/3`$. Distinguish returning one valid label from identifying the support or reconstructing a state.
- **Dependencies and story role:** Entry milestone. It fixes the output contract that every later upper and lower bound must address.
- **Conceptual connection:** A relational task can be easier than learning the complete hidden object; output size alone does not determine its information cost.
- **Source pointers:** W2-readout, section 2.3.1; [model sections 1–3](../science/model.md); [related work: the task and calibrated endpoint](../references/related-work.md).

### M02 — Equal probabilities, different amplitudes

- **Phase:** Background / preliminaries.
- **Central question:** How can two pure specimens produce identical basis samples but behave differently under interference?
- **Understanding target:** Write a uniform-magnitude subset state with phases and verify that computational-basis measurement removes those phases from the label probabilities.
- **Dependencies and story role:** Uses M01. It introduces the information that is absent from the ordinary-sample interface and motivates keeping quantum specimens.
- **Conceptual connection:** Born probabilities are one measurement's statistics, whereas a pure state specifies the statistics of every permitted measurement.
- **Source pointers:** W2-states, section 2.1.2; W2-readout, section 2.3.1; [model sections 1–2](../science/model.md); [worked example](WORKED_EXAMPLE.md).

### M03 — A prior is a density operator

- **Phase:** Background / preliminaries.
- **Central question:** What state does a receiver without the hidden phase table receive?
- **Understanding target:** Form the density operator averaged over a specified table prior while keeping the support fixed. Explain why this average describes the receiver's accessible experiment without saying that each realized specimen was mixed.
- **Dependencies and story role:** Uses M02. It establishes the operational object compared by the converse.
- **Conceptual connection:** A description conditioned on a hidden parameter and the observer's averaged state answer different questions.
- **Source pointers:** W2-states, section 2.1.2, especially the mixture and pure-state formulas; [model section 7](../science/model.md); [phase-twirl converse section 1](../science/phase-twirl-converse.md).

### M04 — Reuse and refresh are different sources

- **Phase:** Background / preliminaries.
- **Central question:** Why does averaging after making several copies differ from independently averaging each copy?
- **Understanding target:** Compare one hidden table reused within a block with a fresh independent table per specimen. Identify the correlations retained by the first experiment even when their one-copy averages agree.
- **Dependencies and story role:** Uses M03. It isolates the source property whose cost the main theorem measures.
- **Conceptual connection:** Equal one-time marginals do not determine a joint experiment. A random global phase also differs from independent address phases.
- **Source pointers:** W2-states, section 2.1.2, composite and correlated systems; [model sections 2, 5 and 7](../science/model.md); [interpretation](../science/interpretation.md).

### M05 — Every receiver is a channel and a readout

- **Phase:** Background / preliminaries.
- **Central question:** How can one statement cover collective measurements, ancillas, feedback and quantum memory?
- **Understanding target:** Represent the receiver as a quantum process followed by a classical output register. Recognize that unrestricted processing does not create extra source-dependent side information.
- **Dependencies and story role:** Uses M03 and M04. It prevents the converse from being read as a bound only on the proposed algorithm.
- **Conceptual connection:** A source-access lower bound can permit powerful computation while limiting the information delivered by that source.
- **Source pointers:** W2-channels, sections 2.2.1–2.2.2; W2-readout, section 2.3.2; [model section 3](../science/model.md); [phase-twirl converse sections 4 and 6](../science/phase-twirl-converse.md).

### M06 — A flag does not erase the rejected copies

- **Phase:** Background / preliminaries.
- **Central question:** How does heralded internal recovery lead to an unconditional complement-sampling experiment?
- **Understanding target:** Separate success probability, conditional output state, eventual classical success and total acquisition cost. Count copies consumed on rejected trials and specify an output when every flag fails.
- **Dependencies and story role:** Uses M01 and M05. It supplies the accounting needed to assess a rare-event recovery instrument.
- **Conceptual connection:** A trace-nonincreasing successful map is one branch of a complete instrument; selecting that branch is not a free experimental resource.
- **Source pointers:** W2-readout, section 2.3.2, “Nondestructive measurements and instruments”; W2-channels, section 2.2.2; [model section 4](../science/model.md); [coherent recovery: hard schedule](../science/coherent-recovery.md).

### M07 — From a full-state bound to one output event

- **Phase:** Background / preliminaries.
- **Central question:** What does trace distance say about the final probability of returning an outside label?
- **Understanding target:** Use half trace distance to bound the change in any measurement event, including after a receiver channel. Keep the factor-of-two convention explicit.
- **Dependencies and story role:** Uses M03 and M05. It is the bridge from source-state simulation to the actual classical-output lower bound.
- **Conceptual connection:** The converse compares complete input states so that one bound survives every allowed downstream decision.
- **Source pointers:** W3-distance, section 3.1.1, Theorem 3.4 and Proposition 3.5; [phase-twirl converse sections 2, 4 and 6](../science/phase-twirl-converse.md); [Watrous bridge](WATROUS_BRIDGE.md).

### M08 — Occupations without measuring the labels

- **Phase:** Background / preliminaries.
- **Central question:** Why can identical copies be expressed by label multiplicities while retaining coherence?
- **Understanding target:** Define a normalized symmetric occupation state as the superposition of all ordered strings with one histogram. Distinguish this basis change from measuring a histogram or sorting and discarding its records.
- **Dependencies and story role:** Uses M02 and M05. It gives a common language for both the converse and recovery.
- **Conceptual connection:** Permutation symmetry reduces redundant descriptions while preserving the phase-bearing amplitudes required by the algorithm.
- **Source pointers:** W7-symmetry, section 7.1.1, Proposition 7.1 and the bag basis; [phase-twirl converse section 1](../science/phase-twirl-converse.md); [coherent recovery: finite-batch instrument](../science/coherent-recovery.md).

### M09 — The birthday weight inside a quantum state

- **Phase:** Background / preliminaries.
- **Central question:** Why do ordinary multinomial probabilities appear in a coherent-copy calculation?
- **Understanding target:** Derive the squared occupation coefficients and the bound on the probability of a $`q`$-fold repeated label. Identify which probability is being bounded and why it does not describe a measured collision label.
- **Dependencies and story role:** Uses M08. It introduces the scale that later controls both lost distinguishability and successful phase recovery.
- **Conceptual connection:** A classical occupancy law can quantify the weight of a coherent subspace without imposing a classical receiver.
- **Source pointers:** W7-symmetry, section 7.1.1, for normalized occupation vectors; [phase-twirl converse sections 1–2](../science/phase-twirl-converse.md); [coherent recovery: exact success probability](../science/coherent-recovery.md). The birthday estimate is supplied in these project proofs.

### M10 — Averaging phases selects characters

- **Phase:** Background / preliminaries.
- **Central question:** Which occupation matrix elements survive independent random root phases?
- **Understanding target:** Show that a $`q`$th-root phase average preserves an entry precisely when its two occupation vectors agree modulo $`q`$ at every address. Compare that condition with equality under continuous phases.
- **Dependencies and story role:** Uses M02 and M08. It identifies the exact structural difference the converse must bound.
- **Conceptual connection:** Group-character orthogonality turns an unknown phase prior into a block structure, rather than an arbitrary loss of all coherence.
- **Source pointers:** W2-states, section 2.1.2, for averaged density operators; W7-symmetry, section 7.1.1, for the chosen basis; [phase-twirl converse section 1](../science/phase-twirl-converse.md); [related work: random phases](../references/related-work.md). The cyclic-character calculation is given explicitly in the project.

### M11 — What an ordinary sample rules out

- **Phase:** Background / preliminaries.
- **Central question:** After seeing several labels in the support, how likely is an unseen label to lie outside it?
- **Understanding target:** Condition a uniform balanced-support prior on the observed distinct-label set. Obtain the posterior success bound and explain why arbitrary processing of that classical transcript cannot improve its information.
- **Dependencies and story role:** Uses M01 and M05. It fixes the matched classical baseline needed by the quantum converse.
- **Conceptual connection:** The sample transcript excludes known labels but leaves all unseen labels exchangeable.
- **Source pointers:** W2-readout, section 2.3.1, for classical outcome probabilities; [phase-twirl converse section 5](../science/phase-twirl-converse.md); [related work: BBW26 posterior argument](../references/related-work.md). The posterior calculation is a project-specific use of the established complement-sampling baseline.

### M12 — One complete source experiment

- **Phase:** Background / preliminaries.
- **Central question:** Which assumptions must remain fixed when comparing receivers?
- **Understanding target:** State the known support size, fixed phase order, exact known block length, copy-only access, hard acquisition cap and allowed cross-block memory. Explain why “at most $`B`$ copies per table” cannot support the upper bound.
- **Dependencies and story role:** Integrates M01 and M04–M11. It closes the preliminary framework before the scientific argument begins.
- **Conceptual connection:** A persistence promise concerns the source clock; it is distinct from a receiver batch limit or storage restriction.
- **Source pointers:** W2-states, section 2.1.2; W2-channels, section 2.2.1; [model sections 2–4 and 8](../science/model.md); [implementation: acquisition and classical costs](../science/implementation.md).

## Narrative / innovation — M13 to M30

### M13 — The calibrated one-copy endpoint

- **Phase:** Narrative / innovation.
- **Central question:** How does one positive quantum sample become a complement sample?
- **Understanding target:** Apply the known uniform-state reflection and verify that balanced cardinality maps the positive support state exactly to the positive complement state.
- **Dependencies and story role:** Uses M02, M05 and M12. It establishes the inherited capability that unknown phases obstruct.
- **Conceptual connection:** An output absent from the measured input support can arise through interference; this is the original complement-sampling mechanism.
- **Source pointers:** W2-states, section 2.1.2; W2-readout, section 2.3.1; [model section 5](../science/model.md); [coherent recovery: subset to complement](../science/coherent-recovery.md); [related work: BBW26](../references/related-work.md).

### M14 — Continuous phases give an exact sample simulator

- **Phase:** Narrative / innovation.
- **Central question:** What can ordinary samples reproduce when a continuous phase table is hidden and frozen?
- **Understanding target:** Draw ordinary labels, prepare their normalized symmetric histogram state, and recover the complete continuous-phase averaged block exactly, including repeated labels.
- **Dependencies and story role:** Uses M08, M10 and M12. It supplies the inherited reference experiment for the new finite-alphabet converse.
- **Conceptual connection:** Quantum processing of classical data can preserve permutation coherence without receiving additional hidden-support information.
- **Source pointers:** W7-symmetry, section 7.1.1; W2-states, section 2.1.2; [phase-twirl converse section 3](../science/phase-twirl-converse.md); [related work: GMR25](../references/related-work.md).

### M15 — A good occupation has no modular partner

- **Phase:** Narrative / innovation.
- **Central question:** Why does agreement modulo $`q`$ force exact equality when every occupation is below $`q`$?
- **Understanding target:** Reconstruct the nonnegative-shift proof using equal total occupation. Verify both identical good-good blocks and the absence of good-bad cross terms.
- **Dependencies and story role:** Uses M09, M10 and M14. This is the load-bearing inference that permits a full-state comparison rather than a heuristic birthday argument.
- **Conceptual connection:** An arithmetic uniqueness statement identifies where finite phase alphabets first become distinguishable from continuous phases.
- **Source pointers:** W7-symmetry, section 7.1.1, for the occupation basis; [phase-twirl converse section 2, Lemma 1](../science/phase-twirl-converse.md); [related work: occupation-sector antecedents](../references/related-work.md).

### M16 — Common positive blocks bound distinguishability

- **Phase:** Narrative / innovation.
- **Central question:** How does a common good block yield a trace-distance bound with the correct constant?
- **Understanding target:** Write each state as the shared positive good component plus a positive residual with equal trace. Bound half trace distance by the bad occupation probability.
- **Dependencies and story role:** Uses M07 and M15. It turns the modular argument into a quantitative bound valid before every receiver.
- **Conceptual connection:** Positivity controls the entire state without conditioning away unsuccessful events or assuming a classical algorithm.
- **Source pointers:** W3-distance, section 3.1.1; W2-states, section 2.1.2; [phase-twirl converse section 2, equations (3)–(5)](../science/phase-twirl-converse.md).

### M17 — Independent source blocks, unrestricted receiver memory

- **Phase:** Narrative / innovation.
- **Central question:** How does the comparison survive a receiver that coherently combines all refresh blocks?
- **Understanding target:** Tensor the conditional-on-support block states, replace factors one at a time, and sum the trace-distance errors. Identify why independence is used for the source prior, not imposed on the receiver.
- **Dependencies and story role:** Uses M04 and M16. It introduces persistence length while retaining the full allowed receiver class.
- **Conceptual connection:** A hybrid comparison of joint input states can remain valid under downstream correlations created by quantum memory.
- **Source pointers:** W2-states, section 2.1.2, composite systems; W3-distance, section 3.1.1; [phase-twirl converse section 4](../science/phase-twirl-converse.md); [model section 3](../science/model.md).

### M18 — Bound the actual complement label

- **Phase:** Narrative / innovation.
- **Central question:** How do the posterior baseline and phase-state comparison constrain the receiver's final label?
- **Understanding target:** Combine the ordinary-sample success bound with the sum of block collision weights. Include adaptive early stopping by padding to the hard acquisition cap.
- **Dependencies and story role:** Uses M11 and M17. It proves a lower bound for the agreed classical output, rather than borrowing an incompatible coherent-state transformation bound.
- **Conceptual connection:** A weaker output contract requires its own payoff argument even when the source-state machinery is familiar.
- **Source pointers:** W3-distance, section 3.1.1, Proposition 3.5; W2-readout, section 2.3.2; [phase-twirl converse sections 5–6, Theorem 2](../science/phase-twirl-converse.md).

### M19 — Two obstructions and one lower frontier

- **Phase:** Narrative / innovation.
- **Central question:** Why must a successful receiver pay both a global collision scale and a refresh-limited scale?
- **Understanding target:** Bound the block sum once by total copies to power $`q`$ and once by total copies times $`B^{q-1}`$. Use a fixed success gap to derive the maximum of the two scales, capped by ordinary linear cost.
- **Dependencies and story role:** Uses M18. It establishes the asymptotic lower half of the principal theorem with constants uniform in $`B`$ for fixed $`q`$.
- **Conceptual connection:** An interaction between total resources and source persistence produces a frontier, not one universal birthday exponent.
- **Source pointers:** W3-distance, section 3.1.1, for the event-comparison foundation; [phase-twirl converse section 7](../science/phase-twirl-converse.md); [persistence frontier sections 1–3](../science/persistence-frontier.md).

### M20 — An admissible inherited recovery instrument

- **Phase:** Narrative / innovation.
- **Central question:** Why do the proposed successful Kraus operators define a physical process?
- **Understanding target:** Identify accepted occupations, the unique distinguished repeated label, the residual vector and the bounded falling-factorial coefficient. Verify that the sum of successful effects is at most the identity.
- **Dependencies and story role:** Uses M05, M06 and M08. It begins the constructive half with the actual inherited instrument, rather than an unspecified nonlinear operation.
- **Conceptual connection:** A nonlinear normalized target can arise on a heralded branch of a linear completely positive map.
- **Source pointers:** W2-channels, section 2.2.2; W2-readout, section 2.3.2, instruments; [coherent recovery: finite-batch instrument](../science/coherent-recovery.md); [related work: QCC26](../references/related-work.md).

### M21 — Factorization removes the hidden phase

- **Phase:** Narrative / innovation.
- **Central question:** Why may the successful residual registers be discarded without losing the recovered subset coherence?
- **Understanding target:** Cancel the occupation multiplicity factors and factor the successful vector into a coordinatewise powered output and one residual vector. Show that the $`q`$th power removes root phases.
- **Dependencies and story role:** Uses M20. It justifies coherent phase recovery, including the cleanup requirement that a measured collision label would violate.
- **Conceptual connection:** Residual independence, rather than a convenient notation for postselection, licenses the partial trace.
- **Source pointers:** W2-states, section 2.1.2, composite systems; W2-channels, section 2.2.2; [coherent recovery: factorization calculation](../science/coherent-recovery.md); [implementation: cleanup](../science/implementation.md).

### M22 — The exact finite-batch success probability

- **Phase:** Narrative / innovation.
- **Central question:** What does one complete recovery attempt cost and how often does it succeed?
- **Understanding target:** Sum the residual multinomial weights to obtain the falling-factorial success formula times a no-$`q`$-collision occupancy probability. Check that the answer is independent of the hidden phases and support labels.
- **Dependencies and story role:** Uses M09 and M21. It supplies the finite probability required to choose a charged schedule.
- **Conceptual connection:** The same ordinary occupancy law quantifies a useful coherent subspace in the upper bound and an inaccessible one in the converse.
- **Source pointers:** W7-symmetry, section 7.1.1, for normalized occupations; W2-readout, section 2.3.2, for successful trace; [coherent recovery: exact success probability](../science/coherent-recovery.md).

### M23 — Choose a batch before it becomes too large

- **Phase:** Narrative / innovation.
- **Central question:** Which batch sizes retain a useful success lower bound within one source phase block?
- **Understanding target:** Use the no-collision union bound to cap the residual batch near the frozen collision scale, then intersect that cap with the exact available block length. Recognize that oversized batches need not improve success.
- **Dependencies and story role:** Uses M22. It converts the exact instrument into a known, implementable choice of batch size.
- **Conceptual connection:** A collective advantage can depend on a bounded useful window, rather than monotonic improvement with more simultaneous inputs.
- **Source pointers:** W7-symmetry, section 7.1.1; [coherent recovery: exact probability and hard schedule](../science/coherent-recovery.md); [persistence frontier section 4](../science/persistence-frontier.md).

### M24 — Count every phase-block tail

- **Phase:** Narrative / innovation.
- **Central question:** How can repeated recovery attempts respect boundaries without an uncharged refresh or a hidden additive block cost?
- **Understanding target:** Pack complete attempts into each known block, charge discarded remainders, stop before an unused final tail, and derive the deterministic total-copy cap. Give a uniform fallback label if all attempts fail.
- **Dependencies and story role:** Uses M06, M12 and M23. It establishes a hard-budget upper bound for the actual source clock.
- **Conceptual connection:** A persistence resource must be acquired through the same interface that defines the lower bound.
- **Source pointers:** W2-readout, section 2.3.2, instruments and recorded outcomes; [coherent recovery: hard schedule](../science/coherent-recovery.md); [implementation: acquisition and classical costs](../science/implementation.md).

### M25 — The classical branch closes the costly regimes

- **Phase:** Narrative / innovation.
- **Central question:** Why is an ordinary-sample fallback part of the optimal quantum algorithm?
- **Understanding target:** Measure a known number of specimens, count unseen support labels, and use convexity to prove a constant complement success. Compare deterministic caps before choosing the coherent or classical branch.
- **Dependencies and story role:** Uses M11 and M12. It supplies the outer minimum and covers small blocks and finite dimensions.
- **Conceptual connection:** Matching a frontier can require different algorithms in different regimes; a quantum receiver is allowed to use ordinary sampling.
- **Source pointers:** W2-readout, section 2.3.1; [coherent recovery: classical fallback](../science/coherent-recovery.md); [persistence frontier sections 2 and 4](../science/persistence-frontier.md).

### M26 — Read the complete persistence law

- **Phase:** Narrative / innovation.
- **Central question:** What changes when the phase order or persistence scale changes?
- **Understanding target:** Combine the lower and upper bounds and locate the ordinary, refresh-limited and frozen regimes. Derive the sign and three-phase examples while keeping phase order fixed.
- **Dependencies and story role:** Uses M19, M24 and M25. It assembles the central result from its independently justified halves.
- **Conceptual connection:** Identical one-copy averaged density operators can support distinct optimal multicopy capabilities because their hidden-source correlations differ.
- **Source pointers:** W2-states, section 2.1.2, for the marginal/joint distinction; [persistence frontier sections 1, 5 and 6](../science/persistence-frontier.md); [interpretation](../science/interpretation.md).

### M27 — Phase cells and an explicit success margin

- **Phase:** Narrative / innovation.
- **Central question:** Does the recovery advantage survive bounded departures from exact roots?
- **Understanding target:** Assume $`|\delta_x|\le\eta/q`$, $`0\le\eta<\pi/2`$ and $`\cos^2\eta>2/3`$. Bound the mean residual phase after powering by the real part of the arc $`[-\eta,\eta]`$. Relate the resulting complement success to that fixed positive margin, and retain exact roots as the lower-bound subfamily.
- **Dependencies and story role:** Uses M13, M21, M24 and M26. It shows which robustness statement the theorem actually supports.
- **Conceptual connection:** A fixed phase promise can preserve a resource order without implying tolerance to arbitrary source noise or within-block drift.
- **Source pointers:** W2-states, section 2.1.2, pure-state amplitudes; W2-readout, section 2.3.1; [model section 6](../science/model.md); [coherent recovery: fixed-width phase cells](../science/coherent-recovery.md).

### M28 — Rare success requires finer synthesis

- **Phase:** Narrative / innovation.
- **Central question:** Why is a constant circuit approximation error insufficient for a rare recovery branch?
- **Understanding target:** Compare subnormalized successful outputs before conditioning, scale the batch error with its success lower bound, and control the full adaptive schedule with a hybrid over all attempted batches.
- **Dependencies and story role:** Uses M07, M24 and M27. It preserves the unconditional output guarantee when ideal rotations are replaced by finite gates.
- **Conceptual connection:** Normalizing a small successful state can magnify error; a complete-run bound also covers changed failure flags.
- **Source pointers:** W2-channels, section 2.2.2; W2-readout, section 2.3.2; W3-distance, section 3.1.1; [implementation: finite universal gates and complete hard schedule](../science/implementation.md). The circuit synthesis result is separately attributed there.

### M29 — Price the source and the processor separately

- **Phase:** Narrative / innovation.
- **Central question:** Which resource advantage has actually been established?
- **Understanding target:** Account for acquisition, batch width, known gates, classical schedules and source preparation. Explain the stated near-linear processing overhead and why it does not supply a free preparation circuit or a hardware crossover.
- **Dependencies and story role:** Uses M12, M24, M25 and M28. It fixes the implementation scope of the algorithmic conclusion.
- **Conceptual connection:** Supplied-copy complexity, coherent width, gate count and the cost of creating each specimen are distinct quantities.
- **Source pointers:** W2-channels, section 2.2.1, for the declared input/output interface; [implementation](../science/implementation.md); [model section 8](../science/model.md); [interpretation](../science/interpretation.md).

### M30 — One connected scientific account

- **Phase:** Narrative / innovation.
- **Central question:** What remains after the inherited ingredients, exact assumptions and full charges are stated together?
- **Understanding target:** Reconstruct the phase-persistence frontier from the source promise through the classical-output converse and attaining schedule. Identify the contributions of BBW26, GMR25, phase-moment work and QCC26, and keep unsupported extensions outside the conclusion.
- **Dependencies and story role:** Integrates M26–M29 and the proof routes they depend on. It closes the account at its established scope rather than adding an optional new research target.
- **Conceptual connection:** A precise operational connection can be the result while its foundational methods remain credited antecedents.
- **Source pointers:** W2-states, W2-channels, W2-readout, W3-distance and W7-symmetry as mapped in the [Watrous bridge](WATROUS_BRIDGE.md); [scientific overview](../science/README.md); [persistence frontier section 8](../science/persistence-frontier.md); [related work and attribution](../references/related-work.md).

## Where to return for a specific gap

Use the central question of a milestone to locate the missing part of the argument. M01–M12 resolve the experiment and language; M13–M19 reconstruct the converse; M20–M25 reconstruct the attaining algorithm; M26–M30 reconcile the frontier, robustness, implementation and attribution. The [worked example](WORKED_EXAMPLE.md) provides finite instances, and the [verification guide](../verification/README.md) identifies the actual checks and their limits.
