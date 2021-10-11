"""contains the current version number of the program and the function of obtaining the version"""

import sys

"""stores the current version number of the program"""
version = "1.0"


def print_version():
    """prints the latest version of the program"""
    print("Version", version)
    sys.exit()