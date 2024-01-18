import re
import sys

import requests


def main(api_url, repository, pr_number, token):
    resp = requests.get(
        f"{api_url}/repos/{repository}/pulls/{pr_number}/requested_reviewers",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    resp.raise_for_status()
    reviewers = [user["login"] for user in resp.json()["users"]]
    print(reviewers)


if __name__ == "__main__":
    api_url = sys.argv[1]
    repository = sys.argv[2]
    ref = sys.argv[3]
    github_token = sys.argv[4]

    if match := re.match(r"^refs/pull/(\d+)/merge$", ref):
        pr_number = match.group(1)
    else:
        sys.exit(0)  # not a pull request

    main(api_url, repository, pr_number, github_token)
