import sys

import requests


def main(api_url, repository, ref, token):
    # https://docs.github.com/en/rest/pulls/review-requests?apiVersion=2022-11-28#get-all-requested-reviewers-for-a-pull-request
    # token = argv[0]

    get_requested_reviewers_url = f"{api_url}/repos/{repository}/pulls/{ref}/requested_reviewers"
    print(get_requested_reviewers_url)
    # requests.get(reviewers)
    # print(len(api_url[0]))
    # print(api_url)


if __name__ == "__main__":
    api_url = sys.argv[1]
    repository = sys.argv[2]
    ref = sys.argv[3]
    github_token = sys.argv[4]

    if ref.endswith("/merge"):
        ref = ref[len("/refs"):-len("/merge")]
    main(api_url, repository, ref, github_token)

