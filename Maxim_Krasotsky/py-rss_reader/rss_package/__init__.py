"""includes modules:
application configuration (rss_argparse), application functions (ReadRSS), application version (rss_version)


imports the necessary functions from the application configuration modules and application functions to work

"""

from .rss_argparse import parse_args, set_args
from .readRSS import ReadRSS