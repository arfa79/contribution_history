#!/usr/bin/env python3

import json
import os
import re
import urllib.parse
import urllib.request
from pathlib import Path

API_URL = "https://api.github.com/search/issues"
AUTHOR = "arfa79"
README_PATH = Path(__file__).resolve().parents[1] / "README.md"
START_MARKER = "<!-- vector-prs:start -->"
END_MARKER = "<!-- vector-prs:end -->"


def github_request(url: str) -> tuple[dict, str | None]:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "contribution-history-updater",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=30) as response:
        links = response.headers.get("Link")
        return json.load(response), next_link(links)


def next_link(links: str | None) -> str | None:
    if not links:
        return None
    for link in links.split(","):
        match = re.match(r'\s*<([^>]+)>; rel="([^"]+)"', link)
        if match and match.group(2) == "next":
            return match.group(1)
    return None


def fetch_pull_requests() -> list[dict]:
    pull_requests = []
    query = urllib.parse.urlencode(
        {"q": f"repo:vectordotdev/vector is:pr author:{AUTHOR}", "per_page": 100}
    )
    url = f"{API_URL}?{query}"
    while url:
        page, url = github_request(url)
        pull_requests.extend(page["items"])
    return sorted(pull_requests, key=lambda pr: pr["number"], reverse=True)


def contribution_type(title: str) -> str:
    prefix = title.split("(", 1)[0].split(":", 1)[0].strip().lower()
    return {
        "feat": "Feature",
        "feature": "Feature",
        "enhancement": "Feature",
        "fix": "Fix",
        "chore": "Maintenance",
        "docs": "Documentation",
        "test": "Testing",
        "refactor": "Refactor",
    }.get(prefix, "Contribution")


def date_only(value: str | None) -> str:
    return value[:10] if value else "—"


def status(pr: dict) -> tuple[str, str]:
    if pr.get("pull_request", {}).get("merged_at"):
        return "Merged", date_only(pr["pull_request"]["merged_at"])
    if pr["state"] == "open":
        return "Open", "—"
    return "Closed", date_only(pr["closed_at"])


def render_table(pull_requests: list[dict]) -> str:
    rows = [
        START_MARKER,
        "| PR | Type | Status | Created | Completed |",
        "| :--- | :--- | :--- | :--- | :--- |",
    ]
    for pr in pull_requests:
        pr_status, completed = status(pr)
        rows.append(
            f'| [#{pr["number"]} — {pr["title"]}]({pr["html_url"]}) '
            f'| {contribution_type(pr["title"])} | {pr_status} '
            f'| {date_only(pr["created_at"])} | {completed} |'
        )
    rows.append(END_MARKER)
    return "\n".join(rows)


def update_summary(readme: str, pull_requests: list[dict]) -> str:
    merged = sum(pr.get("pull_request", {}).get("merged_at") is not None for pr in pull_requests)
    opened = sum(pr["state"] == "open" for pr in pull_requests)
    summary = (
        "Current totals:\n\n"
        f"- **{len(pull_requests)} pull requests** submitted\n"
        f"- **{merged} merged pull requests**\n"
        f"- **{opened} open pull requests**"
    )
    return re.sub(
        r"(?:As of .*?|Current totals):\n\n- \*\*\d+ pull requests\*\* submitted\n"
        r"- \*\*\d+ merged pull requests\*\*\n"
        r"- \*\*\d+ open pull requests\*\*",
        summary,
        readme,
        count=1,
    )


def main() -> None:
    pull_requests = fetch_pull_requests()
    readme = README_PATH.read_text()
    pattern = re.compile(
        re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER), re.DOTALL
    )
    updated = pattern.sub(render_table(pull_requests), readme, count=1)
    updated = update_summary(updated, pull_requests)
    README_PATH.write_text(updated)


if __name__ == "__main__":
    main()
