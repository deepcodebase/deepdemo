import argparse

from server.app import app


def launch_api_server(args):
    app.run(host="0.0.0.0", port=args.port)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="The core script of experiment management."
    )
    subparsers = parser.add_subparsers(dest="command")

    parser_s = subparsers.add_parser("launch_server", description="Launch api server.")
    parser_s.add_argument("--port", default=9000, type=int, help="Filter configs.")

    args = parser.parse_args()

    if args.command == "launch_server":
        launch_api_server(args)
