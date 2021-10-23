"""includes modules:
application configuration (rss_argparse), application functions (ReadRSS), application version (rss_version),
application logging (log), local storage, convert to (json, html, pdf)


imports the necessary functions from the application configuration modules and application functions to work

"""

from .rss_argparse import parse_args, set_args
from .readRSS import ReadRSS
from .log import *
from .local_storage import *
from .rss_json import news_in_json
from .to_html import convert_to_html
from .to_pdf import PDF