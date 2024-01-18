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
    print(resp)
    print(resp.text)
    # https://docs.github.com/en/rest/pulls/review-requests?apiVersion=2022-11-28#get-all-requested-reviewers-for-a-pull-request
    # print(len(api_url[0]))
    # print(api_url)


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
