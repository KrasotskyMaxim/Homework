"""contains the main function to run the program"""

from rss_package import parse_args, set_args, ReadRSS
from sys import argv

# urls = [
#     "https://news.yahoo.com/rss/",
#     "https://lenta.ru/rss",
#     "https://www.vesti.ru/vesti.rss",
#     "https://habr.com/ru/rss/all/all/",
#     "https://virtualbrest.ru/rss/",
#     "https://www.kommersant.ru/RSS/news.xml",
#     "https://people.onliner.by/feed",
#     "https://feeds.simplecast.com/54nAGcIl"
# ]


def main():
    """starts the settings and the program
    gets arguments for settings and creates an RSS feed news object
    """
    args = parse_args(argv[1:])
    settings = set_args(args)
    print(ReadRSS(settings["source"], settings))


if __name__ == "__main__":
    main()