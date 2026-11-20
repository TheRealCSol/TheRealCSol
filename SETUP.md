# CSol GitHub profile

This folder contains the profile README and a small GitHub Actions workflow that updates public Chess.com ratings.

## Publish it

1. Create a **public** repository named exactly `TheRealCSol`.
2. Add these files to its root, keeping the folder structure.
3. Open **Actions** and allow workflows if GitHub asks.
4. Run **Update Chess.com stats** once from the Actions tab. It will also run every 12 hours.
5. Check the profile page: https://github.com/TheRealCSol

The Chess.com data comes from its public, read-only Published-Data API. No Chess.com password or token is used.

The GitHub stat cards, activity graph and trophy image are rendered by third-party services. They can occasionally be unavailable or rate-limited; the profile still works without them.

## Files

- `README.md` — profile layout
- `scripts/update_chess_stats.py` — fetches public ratings and writes an SVG
- `.github/workflows/update-chess-stats.yml` — refreshes the SVG twice daily
- `assets/chess-stats.svg` — initial placeholder, replaced after the first run
