from rss_package import log
import pytest


@pytest.mark.parametrize("expected_result", [88, 10.12, True, "1.1"])
def test_log_bad_formatt(expected_result):
    """check log formatt with bad results"""
    assert log.formatt != expected_result


def test_log_good_formatt():
    """check log formatt with good result"""
    assert log.formatt == "%(asctime)s: %(levelname)s: %(message)s"