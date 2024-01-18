import sys

import requests


def main(argv):
    token = argv[0]
    requests.get()
    print(len(argv[0]))
    print(argv)


if __name__ == "__main__":
    main(sys.argv[1:])

