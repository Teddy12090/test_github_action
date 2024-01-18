import sys


def main(argv):
    print(len(argv[0]))
    print(argv)


if __name__ == "__main__":
    main(sys.argv[1:])

