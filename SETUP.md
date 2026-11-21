# Profile setup

Upload these files to the root of `TheRealCSol/TheRealCSol`, keeping the folder paths:

```text
README.md
assets/chess-stats.svg
scripts/update_chess_stats.py
.github/workflows/update-chess-stats.yml
```

## First run

1. Commit the files to `main`.
2. Open the repository's **Actions** tab.
3. Select **Update Chess.com stats**.
4. Choose **Run workflow**.

The workflow also runs every 12 hours. It uses Chess.com's public, read-only player stats endpoint. No Chess.com password, token, or secret is required.

GitHub Actions must be enabled, and the workflow needs permission to write repository contents.

## Notes

- The card shows Rapid, Blitz and Bullet current ratings, peak ratings, and records when Chess.com publishes them.
- The Chess section links to the actual Chess.com profile.
- GitHub's native achievement badges are displayed by GitHub on the profile page. They are not recreated with a third-party badge service.
- GitHub stats and activity images are external services and can occasionally be unavailable.
- Language percentages are based on code GitHub can detect in public repositories. A small number of repositories can make the chart look unrepresentative.
