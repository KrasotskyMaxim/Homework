"""contains functions for working with local storage in the form of csv format"""
import csv
from rss_package import log

"""specifies the name of the headers in the repository"""
header = ["url", "title", "link", "description", "pubdate", "image"]
""" """
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


def news_by_date(settings):
    """to receive news by date

    parameters:
    settings -- program settings

    accesses the local store and receives news data from it by a given date (by link, by limit, etc.)

    returns a list of received news data
    """

    if settings["verbose"]:
        """print additional information via logging"""
        log.logger.addHandler(log.log_stream)

    """will be filled with the necessary news"""
    date_news = []

    """give the requested date to two types for working with news"""
    date = str(settings["date"])
    year = date[:4]
    month = date[4:6]
    day = date[6:]
    date = [year, month, day]
    """first type"""
    one_date = '-'.join(date)
    """second type"""
    two_date = date
    two_date[1] = months[two_date[1]]
    two_date.reverse()
    two_date = ' '.join(date)

    """receive news from the storage"""
    current_news = create_current_news("local_storage.scv")

    limit = settings["limit"] if settings["limit"] else -1

    for news in current_news:
        """check by limit"""
        if limit == 0:
            return date_news
        """check by pubdate"""
        if news["pubdate"].find(one_date) != -1 or news["pubdate"].find(two_date) != -1:
            """check by source"""
            if settings["source"] and news["url"] == settings["source"]:
                date_news.append(news)
                limit -= 1
            elif not settings["source"]:
                date_news.append(news)
                limit -= 1

    return date_news


def create_local_storage(path):
    """creates local storage

    parameters:
    path -- path -- path to local storage
    """
    with open(path, "w", encoding="utf-8") as storage_file:
        """creating a local storage"""
        writer = csv.DictWriter(storage_file, fieldnames=header)
        writer.writeheader()

    return True


def write_in_local_storage(path, raw_news):
    """writes news to local storage, excluding recurring news

    parameters:
    path -- path to local storage
    raw_news -- news data received from RSS feed
    """
    # noinspection PyBroadException
    try:
        """check for storage"""
        with open(path):
            pass
    except Exception:
        create_local_storage(path)

    """current news stored in local storage"""
    current_news = create_current_news(path)
    with open(path, "a", encoding="utf-8") as storage_file:
        """adding NEW news to local storage"""
        writer = csv.DictWriter(storage_file, fieldnames=header)
        for news in raw_news:
            if news not in current_news:
                writer.writerow(news)

    return True


def read_from_local_storage(path):
    """returns current news data from local storage

    parameters:
    path -- path to local storage
    """
    raw_current_news = []
    with open(path, "r", encoding="utf-8") as storage_file:
        reader = csv.DictReader(storage_file)
        for line in reader:
            raw_current_news.append(dict(line))
    return raw_current_news


def create_current_news(path):
    """converts data to current news for correct operation

    parameters:
    path -- path to local storage


    returns ready-made current news
    """
    current_news = read_from_local_storage(path)
    for news in current_news:
        for key, value in news.items():
            if value == '':
                news[key] = None
    return current_news


def clear_local_storage(path):
    """clears local storage of news"""
    create_local_storage(path)
    print("local storage cleared!")
    return True