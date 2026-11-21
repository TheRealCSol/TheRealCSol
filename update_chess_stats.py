#!/usr/bin/env python3
"""Build an SVG from Chess.com's public player stats endpoint."""
from __future__ import annotations
import json
import urllib.request
from pathlib import Path
from xml.sax.saxutils import escape

USERNAME = "TheRalCSol"
API = f"https://api.chess.com/pub/player/{USERNAME}/stats"
OUTPUT = Path("assets/chess-stats.svg")
MODES = (("RAPID", "chess_rapid"), ("BLITZ", "chess_blitz"), ("BULLET", "chess_bullet"))


def number(value: object) -> str:
    return f"{value:,}" if isinstance(value, (int, float)) else "—"


def mode_values(stats: dict, key: str) -> tuple[str, str, str]:
    section = stats.get(key) or {}
    last, best, record = section.get("last") or {}, section.get("best") or {}, section.get("record") or {}
    current, peak = number(last.get("rating")), number(best.get("rating"))
    wins, losses, draws = (record.get(k, 0) for k in ("win", "loss", "draw"))
    result = f"{number(wins)}W  {number(losses)}L  {number(draws)}D" if all(isinstance(x, (int, float)) for x in (wins, losses, draws)) else "Record unavailable"
    return current, peak, result


def build_svg(stats: dict) -> str:
    cards = []
    for index, (label, key) in enumerate(MODES):
        current, peak, record = mode_values(stats, key)
        x = 18 + index * 214
        cards.append(f'''<g transform="translate({x},28)">
<rect width="198" height="112" rx="12" fill="#161b22" stroke="#30363d"/>
<text x="16" y="25" fill="#8b949e" font-size="11" font-family="Arial, sans-serif" letter-spacing="1.5">{label}</text>
<text x="16" y="62" fill="#e6edf3" font-size="29" font-weight="700" font-family="Arial, sans-serif">{escape(current)}</text>
<text x="16" y="84" fill="#8b949e" font-size="11" font-family="Arial, sans-serif">peak  {escape(peak)}</text>
<text x="16" y="101" fill="#8b949e" font-size="10" font-family="Arial, sans-serif">{escape(record)}</text>
</g>''')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="660" height="160" viewBox="0 0 660 160" role="img" aria-label="Chess.com ratings for {USERNAME}">
<rect width="660" height="160" rx="16" fill="#0d1117"/>
<text x="18" y="17" fill="#8b949e" font-size="9" font-family="Arial, sans-serif">CHESS.COM · {USERNAME}</text>
{''.join(cards)}
<text x="18" y="153" fill="#6e7681" font-size="9" font-family="Arial, sans-serif">Public profile data · refreshed by GitHub Actions</text>
</svg>
'''


def main() -> None:
    request = urllib.request.Request(API, headers={"User-Agent": "csol-profile/2.0 (https://github.com/TheRealCSol)"})
    with urllib.request.urlopen(request, timeout=20) as response:
        stats = json.load(response)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(build_svg(stats), encoding="utf-8")
    print(f"Updated {OUTPUT}")


if __name__ == "__main__":
    main()
