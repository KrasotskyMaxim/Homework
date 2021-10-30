"""contains the main function to run the program"""

from rss_package import parse_args, set_args, ReadRSS, news_in_json
from rss_package import local_storage, log
from sys import argv
from rss_package import convert_to_html
from rss_package.to_pdf import PDF

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


@log.log_decorator
def news_to_text(news: dict):
    """generates news in a readable form

    parameters:
    news -- dictionary with news data

    returns a list of news data in a readable form

    """
    title = news["title"] if news["title"] else "No title"
    link = news["link"]
    description = news["description"] if news["description"] else "No description"
    pubdate = news["pubdate"] if news["pubdate"] else "Unknown pubdate"
    image = news["image"] if news["image"] else "No images"
    return "".join(
        [
            f"Title: {title}\n"
            f"Description: {description}\n"
            f"Published: {pubdate}\n"
            f"Images: {image}\n"
            f"Read more: {link}\n\n"
        ]
    )


@log.log_decorator
def print_readable_text(text, channel_title=None):
    """print news in a format for user"""
    print(f"{channel_title}\n\n" + "\n".join(text))


def write_news_in_json_file(path, news):
    """write different news in json"""
    news_in_json(path, news)


@log.log_decorator
def main():
    """starts the settings and the program
    gets arguments for settings and creates an RSS feed news object
    """
    args = parse_args(argv[1:])
    settings = set_args(args)

    if settings["date"]:
        """receive news from the local storage by date and bring it into a readable form"""
        if settings["verbose"]:
            log.logger.addHandler(log.log_stream)
        news = local_storage.news_by_date(settings)
        readable_text = [news_to_text(n) for n in news]
        if settings["verbose"]:
            pass
        else:
            print_readable_text(readable_text, "\nSaved news:\n")
        json_path = "news_data/all_news_by_date.json"
        html_path = "rss_news_by_date.html"
        pdf_path = "news_data/news_by_date.pdf"
    else:
        """receive news from the RSS-feed and bring it into a readable form"""
        if settings["verbose"]:
            log.logger.addHandler(log.log_stream)
        read_news = ReadRSS(settings["source"], settings)
        feed_title = read_news.channel_title
        news = read_news.raw_news
        readable_text = [news_to_text(news) for news in read_news.raw_news]
        if settings["verbose"]:
            pass
        else:
            print_readable_text(readable_text, read_news.channel_title)
        html_path = "rss_news.html"
        json_path = "news_data/all_news.json"
        pdf_path = "news_data/news.pdf"

    """write to json file"""
    if settings["json"]:
        write_news_in_json_file(json_path, news)

    """convert to html file"""
    if settings["to-html"]:
        convert_to_html(news, settings, html_path)

    """convert to pdf file"""
    if settings["to-pdf"]:
        pdf = PDF(news, pdf_path, feed_title)
        pdf.create_pdf()


if __name__ == "__main__":
    main()