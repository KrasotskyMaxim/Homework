"""checks the functions of the to_html module"""
from rss_package import to_html


def test_convert_to_html():
    """checks the conversion of data to html file"""
    assert to_html.convert_to_html