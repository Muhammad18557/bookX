"""This module is the entry point for the application. It is used to run the application in development mode."""

import argparse
from sys import argv, exit, stderr

from bookX import app

HOST = "0.0.0.0"  # Listen on all network interfaces


def main(port):
    try:
        app.run(HOST, port=port)
    except Exception as ex:
        print(f"An error occurred: {ex}", file=stderr)
        exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Peer-to-Peer Book Exchange Platform.", allow_abbrev=False
    )
    parser.add_argument("port", help="the port at which the server should listen")
    args = parser.parse_args()

    try:
        port = int(args.port)
    except ValueError:
        print("The port must be an integer.", file=stderr)
        exit(1)

    main(args.port)
