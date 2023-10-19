import argparse
import sys

import Tedutil as u
from Tedlog import setup_logging


def arg_process():
    parser = argparse.ArgumentParser(description="Process VCS-compatible filelist")
    parser.add_argument("--log", type=str, default="ted.log")
    parser.add_argument(
        "--version", help="Desplay ted version", action="version", version="0.0.1"
    )
    parser.add_argument(
        "--monochrome", action="store_true", default=not sys.stdout.isatty()
    )

    subparser = parser.add_subparsers(help="sub-command")
    parser_util = subparser.add_parser("tools", help="some useful tools")

    parser_utilsub = parser_util.add_subparsers(help="filelist process")
    parser_filelist_pick = parser_utilsub.add_parser("filepick")
    parser_filelist_pick.add_argument(
        "-f", "--filelist", type=str, help="Path to the filelist"
    )
    parser_filelist_pick.add_argument(
        "-d",
        "--outputdir",
        type=str,
        default="./out",
        help="Path to the output directory",
    )
    parser_filelist_pick.add_argument("-r", "--relapath", type=str, default=None)
    parser_filelist_pick.set_defaults(func=u.filelistpick)

    return parser.parse_args()


if __name__ == "__main__":
    args = arg_process()
    logger = setup_logging(args.log)
    if not args:
        exit(0)

    logger.debug("Command line arguments: " + str(sys.argv))
    args.func(args, logger)
