"""contains the current version number of the program and the function of obtaining the version"""

import sys
from rss_package import log

"""stores the current version number of the program"""
version = "4.0"


@log.log_decorator
def print_version():
    """prints the latest version of the program"""
    print("Version", version)
    sys.exit()