#!/usr/bin/env python3
"""Finite checks for phase-persistent complement sampling (standard library only).

These checks exercise finite instances and independent representations. They do
not prove asymptotic complexity, establish priority, or compile a quantum device.
"""

from __future__ import annotations

import cmath
import itertools
import json
import math
from collections import Counter, defaultdict
from fractions import Fraction


TOL = 2e-9


def compositions(total, length):
    if length == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in compositions(total - first, length - 1):
            yield (first,) + tail


def histogram(word, size):
    return tuple(word.count(i) for i in range(size))


def ordered_counts(size, copies):
    """Count actual ordered words, without using multinomial coefficients."""
    return Counter(histogram(list(word), size)
                   for word in itertools.product(range(size), repeat=copies))


def choose(n, k):
    return math.comb(n, k) if n >= k else 0


def eigvals_symmetric(matrix):
    """Jacobi diagonalization for the small real symmetric matrices below."""
    a = [list(row) for row in matrix]
    n = len(a)
    if n <= 1:
        return [a[0][0]] if n else []
    for _ in range(100 * n * n):
        p, q = max(((i, j) for i in range(n) for j in range(i + 1, n)),
                   key=lambda ij: abs(a[ij[0]][ij[1]]))
        if abs(a[p][q]) < 1e-13:
            return [a[i][i] for i in range(n)]
        app, aqq, apq = a[p][p], a[q][q], a[p][q]
        angle = 0.5 * math.atan2(2 * apq, aqq - app)
        c, s = math.cos(angle), math.sin(angle)
        for k in range(n):
            if k not in (p, q):
                akp, akq = a[k][p], a[k][q]
                a[k][p] = a[p][k] = c * akp - s * akq
                a[k][q] = a[q][k] = s * akp + c * akq
        a[p][p] = c * c * app - 2 * s * c * apq + s * s * aqq
        a[q][q] = s * s * app + 2 * s * c * apq + c * c * aqq
        a[p][q] = a[q][p] = 0.0
    raise AssertionError("Jacobi diagonalization did not converge")


def twirl_matrix(size, q, copies):
    hs = list(compositions(copies, size))
    counts = ordered_counts(size, copies)
    ps = [Fraction(counts[h], size ** copies) for h in hs]
    rho = [[math.sqrt(float(ps[i] * ps[j]))
            if all((x - y) % q == 0 for x, y in zip(h, k)) else 0.0
            for j, k in enumerate(hs)] for i, h in enumerate(hs)]
    return hs, ps, rho


def check_twirls():
    cases = 0
    phase_averages = 0
    max_excess = 0.0
    for size in (2, 3, 4):
        for q in (2, 3, 4):
            for copies in range(8):
                hs, ps, rho = twirl_matrix(size, q, copies)
                good = [max(h) < q for h in hs]
                bad = sum((p for p, g in zip(ps, good) if not g), Fraction())
                for i, h in enumerate(hs):
                    for j, k in enumerate(hs):
                        if good[i] or good[j]:
                            expected = float(ps[i]) if i == j else 0.0
                            assert abs(rho[i][j] - expected) < TOL
                # Residue classes are independent blocks of the actual matrix.
                # Diagonalize those blocks instead of invoking a trace-bound formula.
                classes = defaultdict(list)
                for i, h in enumerate(hs):
                    classes[tuple(x % q for x in h)].append(i)
                distance = 0.0
                for indices in classes.values():
                    difference = [[rho[i][j] - (float(ps[i]) if i == j else 0.0)
                                   for j in indices] for i in indices]
                    distance += sum(abs(x) for x in eigvals_symmetric(difference)) / 2
                union = Fraction(choose(copies, q), size ** (q - 1))
                assert distance <= float(bad) + TOL
                assert bad <= union
                max_excess = max(max_excess, distance - float(bad))
                cases += 1
                if size <= 3 and copies <= 4:
                    # Independently average all q^size phase assignments. This
                    # checks the residue selection rule against the source ensemble.
                    assignments = list(itertools.product(range(q), repeat=size))
                    for i, h in enumerate(hs):
                        for j, k in enumerate(hs):
                            phase_mean = sum(cmath.exp(2j * math.pi * sum(
                                phase * (x - y) for phase, x, y in zip(assignment, h, k)) / q)
                                for assignment in assignments) / len(assignments)
                            element = math.sqrt(float(ps[i] * ps[j])) * phase_mean
                            assert abs(element - rho[i][j]) < TOL
                    phase_averages += 1
    return {"occupation_twirl_cases": cases,
            "explicit_phase_ensemble_cases": phase_averages,
            "max_trace_bound_excess": max_excess}


def normalize(values):
    norm = math.sqrt(sum(abs(x) ** 2 for x in values))
    return [x / norm for x in values]


def check_extraction():
    cases = factor_cases = occupation_inputs = 0
    for size in (2, 3, 4):
        for q in (2, 3, 4):
            c_q = math.factorial(2 * q - 1) // math.factorial(q - 1)
            for copies in range(q, q + 4):
                hs = list(compositions(copies, size))
                counts = ordered_counts(size, copies)
                # Build the Kraus maps directly from residual occupations.
                maps = {}
                effects = defaultdict(Fraction)
                for z in compositions(copies - q, size):
                    if max(z) >= q:
                        continue
                    entries = []
                    for label in range(size):
                        n = list(z)
                        n[label] += q
                        n = tuple(n)
                        weight = Fraction(math.factorial(n[label]),
                                          math.factorial(n[label] - q) * c_q)
                        entries.append((n, label, weight))
                        effects[n] += weight
                    maps[z] = entries
                for h in hs:
                    assert 0 <= effects[h] <= 1
                    exceptional = [i for i, value in enumerate(h) if value >= q]
                    expected_eligible = (len(exceptional) == 1 and
                                         h[exceptional[0]] < 2 * q)
                    assert bool(effects[h]) == expected_eligible
                    occupation_inputs += 1
                observed = sum((Fraction(counts[h], size ** copies) * effects[h]
                                for h in hs), Fraction())
                residual_words = ordered_counts(size, copies - q)
                collision_free = sum(count for z, count in residual_words.items() if max(z) < q)
                formula = (Fraction(math.factorial(copies), math.factorial(copies - q) * c_q)
                           * Fraction(1, size ** (q - 1))
                           * Fraction(collision_free, size ** (copies - q)))
                assert observed == formula
                cases += 1
                profiles = [normalize([cmath.exp(2j * math.pi * i / q)
                                       for i in range(size)]),
                            normalize([complex(i + 1, (-1) ** i * (i + 2) / 3)
                                       for i in range(size)])]
                for alpha in profiles:
                    # Assemble symmetric input amplitudes by summing actual
                    # ordered-word amplitudes, rather than inserting a factorial.
                    sums = defaultdict(complex)
                    for word in itertools.product(range(size), repeat=copies):
                        h = histogram(list(word), size)
                        amplitude = math.prod(alpha[label] for label in word)
                        sums[h] += amplitude
                    symmetric = {h: value / math.sqrt(counts[h]) for h, value in sums.items()}
                    outputs = []
                    for entries in maps.values():
                        vector = [0j] * size
                        for h, label, weight in entries:
                            vector[label] += math.sqrt(float(weight)) * symmetric[h]
                        outputs.append(vector)
                    reduced = [[sum(v[i] * v[j].conjugate() for v in outputs)
                                for j in range(size)] for i in range(size)]
                    probability = sum(reduced[i][i].real for i in range(size))
                    target = normalize([value ** q for value in alpha])
                    for i in range(size):
                        for j in range(size):
                            expected = probability * target[i] * target[j].conjugate()
                            assert abs(reduced[i][j] - expected) < TOL
                    factor_cases += 1
    return {"exact_extraction_probability_cases": cases,
            "kraus_occupation_inputs": occupation_inputs,
            "complex_factorization_cases": factor_cases}


def check_classical_samples():
    enumeration_cases = posterior_records = 0
    for size in range(1, 6):
        universe = 2 * size
        for copies in range(7):
            distribution = defaultdict(Fraction)
            for word in itertools.product(range(size), repeat=copies):
                distribution[len(set(word))] += Fraction(1, size ** copies)
            # Independent sequential occupancy recursion.
            dynamic = {0: Fraction(1)}
            for _ in range(copies):
                nxt = defaultdict(Fraction)
                for distinct, probability in dynamic.items():
                    nxt[distinct] += probability * Fraction(distinct, size)
                    nxt[distinct + 1] += probability * Fraction(size - distinct, size)
                dynamic = {k: v for k, v in nxt.items() if v}
            assert dict(distribution) == dynamic
            success = sum((p * Fraction(size, universe - d) for d, p in distribution.items()),
                          Fraction())
            if copies < size:
                assert success <= Fraction(size, universe - copies)
            if copies >= math.ceil(size * math.log(2)):
                assert success >= Fraction(2, 3)
            enumeration_cases += 1
    for universe in (2, 4, 6):
        size = universe // 2
        supports = [set(s) for s in itertools.combinations(range(universe), size)]
        for copies in range(5):
            for record in itertools.product(range(universe), repeat=copies):
                seen = set(record)
                compatible = [s for s in supports if seen <= s]
                if not compatible:
                    continue
                expected = Fraction(size, universe - len(seen))
                for label in range(universe):
                    posterior = Fraction(sum(label not in s for s in compatible), len(compatible))
                    assert posterior == (0 if label in seen else expected)
                posterior_records += 1
    return {"ordered_sampling_vs_recursion_cases": enumeration_cases,
            "exhaustive_posterior_records": posterior_records}


def check_block_bounds_and_clock():
    scalar_cases = clock_cases = 0
    for q in (2, 3, 4):
        for block_length in range(1, 13):
            for copies in range(25):
                for offset in range(block_length):
                    remaining = copies
                    first = min(remaining, block_length - offset)
                    parts = [first] if first else []
                    remaining -= first
                    while remaining:
                        part = min(block_length, remaining)
                        parts.append(part)
                        remaining -= part
                    collision_subsets = sum(choose(part, q) for part in parts)
                    assert collision_subsets <= choose(copies, q)
                    assert collision_subsets <= Fraction(copies * block_length ** (q - 1),
                                                          math.factorial(q))
                    if block_length < q:
                        assert collision_subsets == 0
                    scalar_cases += 1
    for block_length in range(1, 13):
        for batch in range(1, block_length + 1):
            for offset in range(block_length):
                for trials in range(1, 13):
                    position = offset
                    discarded = 0
                    for _ in range(trials):
                        tail = block_length - position % block_length
                        if tail < batch:
                            position += tail
                            discarded += tail
                        assert position // block_length == (position + batch - 1) // block_length
                        position += batch
                    charged = position - offset
                    assert charged == trials * batch + discarded
                    assert charged <= 2 * trials * batch + batch
                    clock_cases += 1
    return {"exact_block_collision_bound_cases": scalar_cases,
            "aligned_batch_clock_cases": clock_cases}


def check_phase_cells():
    cases = 0
    for universe in (2, 4, 6, 8):
        size = universe // 2
        for support in itertools.combinations(range(universe), size):
            complement = set(range(universe)) - set(support)
            for q in (2, 3, 4):
                for eta in (0.0, 0.2, math.pi / 6, 0.9):
                    for signs in itertools.product((-1, 1), repeat=size):
                        alpha = [0j] * universe
                        for k, label in enumerate(support):
                            phase = 2 * math.pi * ((label + k) % q) / q + signs[k] * eta / q
                            alpha[label] = cmath.exp(1j * phase) / math.sqrt(size)
                        powered = normalize([a ** q for a in alpha])
                        # Apply the full known uniform reflection in coordinates.
                        total = sum(powered)
                        reflected = [2 * total / universe - value for value in powered]
                        success = sum(abs(reflected[i]) ** 2 for i in complement)
                        assert success + TOL >= math.cos(eta) ** 2
                        predicted = abs(sum(cmath.exp(1j * sign * eta)
                                            for sign in signs) / size) ** 2
                        assert abs(success - predicted) < TOL
                        if eta == 0:
                            assert abs(success - 1) < TOL
                        cases += 1
    # The arc restriction cannot be replaced by cos(eta)^2 > 2/3 alone:
    # eta=pi would satisfy that scalar condition while admitting opposite
    # residual phases whose mean vanishes.
    outside_arc = [1j / math.sqrt(2), -1j / math.sqrt(2), 0j, 0j]
    reflected = [sum(outside_arc) / 2 - value for value in outside_arc]
    success = sum(abs(reflected[i]) ** 2 for i in (2, 3))
    assert success < 1e-12 and math.cos(math.pi) ** 2 > 2 / 3
    return {"root_phase_and_robust_cell_diffusion_cases": cases,
            "phase_cell_arc_necessity_counterexamples": 1}


def check_refresh_independence():
    cases = 0
    for size in (2, 3):
        for q in (2, 3, 4):
            roots = [cmath.exp(2j * math.pi * k / q) for k in range(q)]
            assert abs(sum(roots) / q) < TOL
            assignments = list(itertools.product(roots, repeat=size))
            one_copy = [[sum(a[i] * a[j].conjugate() for a in assignments)
                         / (size * len(assignments)) for j in range(size)]
                        for i in range(size)]
            for i in range(size):
                for j in range(size):
                    assert abs(one_copy[i][j] - (1 / size if i == j else 0)) < TOL
            # A shared random global phase has zero individual means but does
            # not diagonalize a specimen. Independence across addresses matters.
            common = sum(root * root.conjugate() for root in roots) / (size * q)
            assert abs(common - 1 / size) < TOL
            assert abs(common) > 0.1
            # With one table reused, permutations of two distinct labels retain
            # coherence. Independently refreshed tables have no such coherence.
            persisted = sum((a[0] * a[1]) * (a[1] * a[0]).conjugate()
                            for a in assignments) / (size ** 2 * len(assignments))
            refreshed = one_copy[0][1] * one_copy[1][0]
            assert abs(persisted - 1 / size ** 2) < TOL
            assert abs(refreshed) < TOL
            cases += 1
    return {"phase_refresh_independence_cases": cases}


def main():
    report = {
        "status": "passed",
        "scope": "Finite analytical checks; not an asymptotic proof, priority certificate, or hardware experiment.",
        "arithmetic": "Exact fractions for combinatorics; complex floating point and small Jacobi eigensystems for state checks.",
    }
    for check in (check_twirls, check_extraction, check_classical_samples,
                  check_block_bounds_and_clock, check_phase_cells,
                  check_refresh_independence):
        report.update(check())
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
