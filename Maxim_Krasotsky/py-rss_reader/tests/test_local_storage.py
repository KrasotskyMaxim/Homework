"""checks the functions of the local_storage module"""
from rss_package import local_storage


header = ["url", "title", "link", "description", "pubdate", "image"]

months = {
        "1": "Jan",
        "2": "Feb",
        "3": "Mar",
        "4": "Apr",
        "5": "May",
        "6": "Jun",
        "7": "Jul",
        "8": "Aug",
        "9": "Sep",
        "10": "Oct",
        "11": "Nov",
        "12": "Dec"
    }


def test_create_test_local_storage():
    """check creates test local storage"""
    assert local_storage.create_local_storage("tests/test_local_storage.csv")


def test_write_in_local_storage():
    """check writes news to test local storage"""
    test_news = local_storage.read_from_local_storage("local_storage.scv")
    assert local_storage.write_in_local_storage("tests/test_local_storage.csv", test_news)


def test_read_from_local_storage():
    """check returns current news data from test local storage"""
    assert isinstance(local_storage.read_from_local_storage("tests/test_local_storage.csv"), list)


def test_create_current_news():
    """check converts data to current news for correct operation"""
    assert isinstance(local_storage.create_current_news("tests/test_local_storage.csv"), list)


def test_clear_local_storage():
    """check clears local storage of news"""
    assert local_storage.clear_local_storage("tests/test_local_storage.csv")


def test_true_header():
    """check test local storage header"""
    assert local_storage.header == header


def test_true_months():
    """check month variable"""
    assert local_storage.months == months