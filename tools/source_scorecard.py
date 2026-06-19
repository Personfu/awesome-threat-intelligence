#!/usr/bin/env python3
"""Rank threat-intelligence sources for freshness, confidence, and usability."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def score(row: dict[str, Any]) -> dict[str, Any]:
    freshness = int(row.get('freshness', 0))
    confidence = int(row.get('confidence', 0))
    machine_readable = 15 if row.get('machine_readable') else 0
    clear_license = 10 if row.get('clear_license') else -10
    cost_fit = int(row.get('cost_fit', 0))
    operational_fit = int(row.get('operational_fit', 0))
    total = max(0, min(100, freshness + confidence + machine_readable + clear_license + cost_fit + operational_fit))
    return {**row, 'score': total, 'tier': 'S' if total >= 85 else 'A' if total >= 70 else 'B' if total >= 50 else 'C'}


def render(rows: list[dict[str, Any]]) -> str:
    ranked = sorted((score(row) for row in rows), key=lambda item: item['score'], reverse=True)
    lines = ['# Threat Intelligence Source Scorecard', '', '| Source | Tier | Score | Notes |', '|---|---:|---:|---|']
    for row in ranked:
        lines.append(f"| {row.get('name','unknown')} | {row['tier']} | {row['score']} | {row.get('notes','')} |")
    lines.append('\nSafety: use licensing-compliant feeds and avoid restricted, credentialed, or personal-data collection unless the contract explicitly permits it.\n')
    return '\n'.join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description='Build a source scorecard from JSON metadata.')
    parser.add_argument('input', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    raw = json.loads(args.input.read_text(encoding='utf-8'))
    rows = raw if isinstance(raw, list) else raw.get('sources', [])
    args.output.write_text(render(rows), encoding='utf-8')
    print(f'wrote {args.output}')


if __name__ == '__main__':
    main()
