#!/usr/bin/env python3
"""Check learning-route structure and retrieval links, not teaching correctness."""

from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
FIELDS = (
    "Phase",
    "Central question",
    "Understanding target",
    "Dependencies and story role",
    "Conceptual connection",
    "Source pointers",
)
PHASES = {
    "Background / preliminaries": 12,
    "Narrative / innovation": 18,
}
MILESTONE_HEADING = re.compile(r"^###\s+(M\d{2})\s+[—–-]\s+(.+)$", re.MULTILINE)
FIELD = re.compile(r"^\s*[-*]\s+\*\*([^*]+):\*\*\s*(.*)$", re.MULTILINE)
LINK = re.compile(r"\[[^\]\n]+\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)")
PRIVATE_MARKERS = re.compile(
    r"\b(?:Arthur|Merlin|Gwen|Camelot|learner_status|current_milestone|quiz_history)\b"
    r"|Created\s*[—-]\s*authorize|\bpermission contract\b",
    re.IGNORECASE,
)


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def local_target(document, target):
    target = target.strip("<>")
    parts = urlsplit(target)
    if parts.scheme or parts.netloc or not parts.path:
        return None
    return (document.parent / unquote(parts.path)).resolve()


def heading_anchors(document):
    """GitHub-style slugs for the plain Markdown headings in this route."""
    anchors = set()
    occurrences = {}
    for match in re.finditer(r"^#{1,6}\s+(.+?)\s*#*\s*$", document.read_text(), re.MULTILINE):
        heading = match.group(1).strip().lower()
        slug = "".join(ch for ch in heading
                       if ch.isalnum() or ch in "_- " or unicodedata.category(ch).startswith("M"))
        slug = slug.replace(" ", "-")
        number = occurrences.get(slug, 0)
        occurrences[slug] = number + 1
        anchors.add(slug if not number else f"{slug}-{number}")
    return anchors


def main():
    milestone_file = ROOT / "learning/MILESTONES.md"
    bridge_file = ROOT / "learning/WATROUS_BRIDGE.md"
    example_file = ROOT / "learning/WORKED_EXAMPLE.md"
    required = [ROOT / "README.md", ROOT / "llms.txt", milestone_file,
                bridge_file, example_file]
    for path in required:
        require(path.is_file(), f"Missing learning-route file: {path.relative_to(ROOT)}")

    text = milestone_file.read_text()
    headings = list(MILESTONE_HEADING.finditer(text))
    actual_ids = [match.group(1) for match in headings]
    expected_ids = [f"M{i:02}" for i in range(1, 31)]
    require(actual_ids == expected_ids,
            "Milestone headings must contain M01–M30 exactly once and in that order")
    phase_counts = dict.fromkeys(PHASES, 0)
    dependency_edges = 0
    source_link_count = 0
    titles = []
    for index, heading in enumerate(headings):
        milestone_id, title = heading.groups()
        titles.append(title.strip().casefold())
        end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        body = text[heading.end():end]
        fields = list(FIELD.finditer(body))
        labels = [field.group(1) for field in fields]
        require(labels == list(FIELDS), f"{milestone_id}: expected the six named fields in order")
        values = {}
        for pos, field in enumerate(fields):
            field_end = fields[pos + 1].start() if pos + 1 < len(fields) else len(body)
            value = (field.group(2) + body[field.end():field_end]).strip()
            require(bool(value), f"{milestone_id}: empty {field.group(1)}")
            values[field.group(1)] = value
        phase = values["Phase"].strip(" .")
        require(phase in PHASES, f"{milestone_id}: unknown phase {phase!r}")
        expected_phase = list(PHASES)[0 if index < 12 else 1]
        require(phase == expected_phase, f"{milestone_id}: wrong side of the 12/18 phase partition")
        phase_counts[phase] += 1
        dependency_text = values["Dependencies and story role"]
        dependencies = set(re.findall(r"\bM\d{2}\b", dependency_text))
        for first, last in re.findall(r"\b(M\d{2})\s*[–-]\s*(M\d{2})\b", dependency_text):
            require(int(first[1:]) <= int(last[1:]), f"{milestone_id}: reversed dependency range")
            dependencies.update(f"M{i:02}" for i in range(int(first[1:]), int(last[1:]) + 1))
        for dependency in dependencies:
            require(dependency in expected_ids[:index],
                    f"{milestone_id}: dependency {dependency} must be an earlier milestone")
        dependency_edges += len(dependencies)
        pointers = LINK.findall(values["Source pointers"])
        require(bool(pointers), f"{milestone_id}: Source pointers needs an inspectable link")
        require(any(local_target(milestone_file, pointer) is not None for pointer in pointers),
                f"{milestone_id}: Source pointers needs a local authoritative route")
        source_link_count += len(pointers)
    require(len(set(titles)) == 30, "Milestone titles must be unique")
    require(phase_counts == PHASES, "Milestone phase totals differ from 12 background and 18 narrative")

    bridge = bridge_file.read_text()
    require("Watrous" in bridge and "The Theory of Quantum Information" in bridge and "2018" in bridge,
            "The selected anchor must identify Watrous, book title and 2018 version")
    selected_lines = [line for line in bridge.splitlines()
                      if re.search(r"(?:selected|single|sole)\s+(?:educational\s+)?anchor", line,
                                   re.IGNORECASE)]
    require(bool(selected_lines), "Bridge must state its selected educational anchor explicitly")
    require(all("Watrous" in line for line in selected_lines),
            "A selected-anchor declaration does not identify Watrous")
    require(any(url in bridge for url in ("https://jhwatrous.github.io/TQI.pdf",
                                          "https://cs.uwaterloo.ca/~watrous/TQI/")),
            "Bridge must link the inspected author-hosted Watrous manuscript")

    learning_files = sorted((ROOT / "learning").glob("*.md"))
    documents = [ROOT / "README.md", ROOT / "llms.txt"] + learning_files
    local_links = external_links = heading_fragments = 0
    for document in documents:
        content = document.read_text()
        if document.parent.name == "learning":
            require(PRIVATE_MARKERS.search(content) is None,
                    f"Possible private coaching/authorization marker in {document.relative_to(ROOT)}")
        for target in LINK.findall(content):
            path = local_target(document, target)
            if path is None:
                external_links += 1
                continue
            require(path.is_relative_to(ROOT),
                    f"Link escapes repository: {document.relative_to(ROOT)} -> {target}")
            require(path.is_file(), f"Broken file link: {document.relative_to(ROOT)} -> {target}")
            fragment = unquote(urlsplit(target.strip("<>")).fragment)
            if fragment and path.suffix == ".md":
                require(fragment in heading_anchors(path),
                        f"Broken heading fragment: {document.relative_to(ROOT)} -> {target}")
                heading_fragments += 1
            local_links += 1
    readme = (ROOT / "README.md").read_text()
    require(any("learning/" in target for target in LINK.findall(readme)),
            "Root README must link the learning route")
    llms = (ROOT / "llms.txt").read_text()
    for path in (milestone_file, bridge_file, example_file):
        require(path.relative_to(ROOT).as_posix() in llms,
                f"LLM navigation missing {path.relative_to(ROOT)}")
    plain_paths = re.findall(r"(?:learning|science|references|verification)/[\w./-]+\.(?:md|py|bib|txt)", llms)
    for path in plain_paths:
        require((ROOT / path).is_file(), f"Broken plain LLM route: {path}")

    all_learning = "\n".join(path.read_text() for path in learning_files)
    # Inventory only: these words do not establish that the qualifiers are
    # stated correctly. A separate human reading must check their meaning.
    marker_patterns = {
        "fixed_order_or_alphabet": r"fixed[^\n]{0,70}(?:order|alphabet|q)|(?:order|alphabet)[^\n]{0,70}fixed",
        "exact_known_blocks": r"exact(?:ly)?[^\n]{0,70}(?:block|cop|call)|known[^\n]{0,70}(?:block|boundar)",
        "unconditional_output": r"unconditional",
        "source_preparation_cost": r"(?:source|state)[^\n]{0,70}prepar|prepar[^\n]{0,70}(?:source|cost)",
        "phase_cell_arc": r"eta|η|phase.cell|phase cell",
    }
    markers = {name: bool(re.search(pattern, all_learning, re.IGNORECASE))
               for name, pattern in marker_patterns.items()}
    print(json.dumps({
        "status": "passed",
        "milestones": actual_ids,
        "phase_counts": phase_counts,
        "dependency_edges": dependency_edges,
        "source_pointer_links": source_link_count,
        "selected_anchor": "John Watrous, The Theory of Quantum Information (2018)",
        "learning_documents": [path.relative_to(ROOT).as_posix() for path in learning_files],
        "valid_local_file_links": local_links,
        "valid_local_heading_fragments": heading_fragments,
        "external_links_present_not_network_tested": external_links,
        "plain_llm_paths": len(plain_paths),
        "qualifier_marker_inventory_only": markers,
        "scope": "Structure, anchor identity, earlier dependencies and file navigation only; mathematical meaning, teaching adequacy, book pointers and visible rendering need separate review.",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
