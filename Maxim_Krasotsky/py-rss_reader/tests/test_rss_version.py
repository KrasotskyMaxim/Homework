"""test file with checking the functions of the module rss_ver"""

from rss_package.rss_version import print_version, version
import pytest


@pytest.mark.parametrize("expected_result", [88, "1.1", 10.2, True])
def test_version_bad(expected_result):
    """checks the version value for different data types"""
    assert version != expected_result


def test_version_good():
    """checks the version value for correctness"""
    assert version == "4.0"


def test_print_version():
    """checks the print_version function to terminate the program after the result"""
    with pytest.raises(SystemExit):
        print_version()