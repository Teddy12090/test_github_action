import sys

import requests


def main(argv):
    # https://docs.github.com/en/rest/pulls/review-requests?apiVersion=2022-11-28#get-all-requested-reviewers-for-a-pull-request
    token = argv[0]
    # requests.get()
    print(len(argv[0]))
    print(argv)


if __name__ == "__main__":
    main(sys.argv[1:])

