"""checks the functions of the readRSS module"""

from rss_package.readRSS import ReadRSS


def create_object():
    """returns an object for tests"""
    objct = ReadRSS('https://virtualbrest.ru/rss/', {
        "version": None,
        "limit": 10,
        "json": True,
        "verbose": True,
        "source": "https://virtualbrest.ru/rss/"
    })
    return objct


"""an object for tests is created"""
obj = create_object()


def get_news():
    """verifies receipt of news"""
    print(obj.__str__())


def test_obj_url():
    """checks the link to the RSS feed"""
    assert obj.url == 'https://virtualbrest.ru/rss/'


def test_obj_settings():
    """checks the received settings"""
    assert obj.settings == {
        "version": None,
        "limit": 10,
        "json": True,
        "verbose": True,
        "source": "https://virtualbrest.ru/rss/"
    }


def test_connection():
    """checks the data connection via the link"""
    assert obj.r


def test_obj_status_code():
    """checks the correctness of the current connection status code"""
    assert obj.r.status_code == 200
    assert obj.r.status_code != 404


def test_obj_items():
    """verifies receipt of news data"""
    assert obj.items


"""receipt of news"""
get_news()


def test_news_count():
    """checks the received number of news"""
    assert len(obj.raw_news) == 10