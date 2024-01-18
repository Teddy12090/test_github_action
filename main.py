import re
import sys


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

    if match := re.match(r"refs/(pull/\d+)/merge", ref):
        ref = match.group(1)
    else:
        sys.exit(0)  # not a pull request
    main(api_url, repository, ref, github_token)
