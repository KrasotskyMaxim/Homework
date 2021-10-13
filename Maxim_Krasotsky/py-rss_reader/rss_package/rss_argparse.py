"""contains functions of settings of parameters for operation of the program"""

import argparse
import sys
from .rss_version import print_version, version


def parse_args(args: list):
    """adds settings and returns these parameters"""
    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="RSS URL", nargs="?")
    parser.add_argument("--version", action="store_true", help="Print version info")
    parser.add_argument("--json", action="store_true", help="Print result as JSON in stdout")
    parser.add_argument("--verbose", action="store_true", help="Outputs verbose status messages")
    parser.add_argument("--limit", type=int, help="Limit news topics if this parameter provided")
    return parser.parse_args(args)


def set_args(args):
    """sets the settings for the program to work and returns a dictionary with settings"""
    return {
        "version": print_version() if args.version else version,
        "limit": args.limit if args.limit else None,
        "json": True if args.json else False,
        "verbose": True if args.verbose else False,
        "source": args.source if args.source
        else print("error: RSS URL is required", sys.exit()),
    }