# Learning route

The educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. Its [official author page](https://cs.uwaterloo.ca/~watrous/TQI/) identifies the edition and provides the author's manuscript. The textbook supplies the language of states, channels, measurements, distinguishability and symmetric tensors; the persistence theorem is established in this repository.

Start with the [Watrous bridge](WATROUS_BRIDGE.md), which translates the selected textbook sections into the source model and supplies the extra occupation and phase calculations. Then follow the [30 milestones](MILESTONES.md) in order. The [four-label worked example](WORKED_EXAMPLE.md) makes the distinction between a one-copy average and repeated-source correlations explicit before returning to the asymptotic theorem.

## Why 12 background milestones and 18 narrative milestones?

M01–M12 build the complete language needed to ask the question: the support task, quantum versus classical data, correlated ensembles, instruments, unconditional success, trace-distance bounds, occupations, phase characters, posterior sampling and the source clock. M13–M30 then follow the actual argument from its simple endpoints through the unrestricted converse, the attaining instrument and schedule, and the implementation and interpretation limits. The longer second phase reflects the two matching proofs and their resource accounting.

Within each phase, the route goes from a local calculation to its global role. The dependency list on each milestone names earlier steps that it uses. The map describes the project rather than a particular reader's progress.

| Route | Use |
| --- | --- |
| [Watrous bridge](WATROUS_BRIDGE.md) | Selected sections, notation translation, and proof steps beyond the textbook |
| [Four-label example](WORKED_EXAMPLE.md) | A small source, its output, its phase correlations and its charged acquisition cost |
| [M01–M12](MILESTONES.md#m01--one-label-outside-a-hidden-set) | Background and preliminaries |
| [M13–M30](MILESTONES.md) | Narrative, proof and scientific contribution |
| [Scientific route](../science/README.md) | Full definitions and derivations |
| [Verification guide](../verification/README.md) | Reproducible finite and structural checks, with their limits |

The result assumes a balanced support, fixed phase order, known blocks of exactly the stated number of consecutive source calls, and unconditional classical-label success. It charges failed batches and discarded tails. The phase-cell extension has an explicit arc and success margin. Receiver costs are separate from source preparation; the supplied-copy result does not establish an end-to-end classical-data runtime advantage.
