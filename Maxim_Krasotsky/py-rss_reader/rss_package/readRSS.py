"""contains a class for parsing RSS feeds"""

from rss_package import local_storage, log
import requests
from bs4 import BeautifulSoup
import re


class ReadRSS:

    """Contains methods for processing RSS feeds depending on the settings passed"""

    @log.log_decorator
    def __init__(self, url, settings: dict):
        """Class object initializer

        arguments:
        url -- feed URL
        settings -- program settings


        Gets the url of the RSS feed and settings for work.
        """
        self.url = url
        self.settings = settings

        # noinspection PyBroadException
        try:
            """get html code of RSS-feed"""
            self.r = requests.get(url)
            if self.settings["verbose"]:
                """print the status of the request and additional information via logging"""
                print(f"\nCode status: {self.r.status_code}\n\n")
        except Exception:
            """print an explanatory error message and the error itself"""
            print("Error fetching the URL: ", url)
            print(Exception)

        # noinspection PyBroadException
        try:
            """
            create a BeautifulSoup class object and "xml" parameter from the content of the RSS feed for further work
            """
            self.soup = BeautifulSoup(self.r.content, "xml")
        except Exception:
            """print an explanatory error message and the error itself"""
            print("Couldn`t parse the xml: ", self.url)
            print(Exception)

        """find the header of the RSS feed"""
        self.channel_title = self.soup.find("title").text

        """find news RSS-feed"""
        self.items = self.soup.findAll("item")

        """number of recorded news"""
        news_count = self.settings["limit"]

        """create a list of news RSS-feed"""
        self.raw_news = [self._create_news(item) for item in self.items[0:news_count]]

        """write news to local storage"""
        local_storage.write_in_local_storage("local_storage.scv", self.raw_news)

    def _create_news(self, item):
        """creates news from the received data of the RSS-feed

        parameters:
        item -- data of the RSS-feed

        Has a list of possible tags to store the news image.
        Checks this part of the RSS feed for data to generate news.


        returns the generated news in the form of a dictionary

        """
        img_keys = ["content", "thumbnail", "enclosure"]
        img = None

        if item.title:
            """
            create a BeautifulSoup class object with "lxml" parameter to obtain data,
            convert data to read CDATA fields,
            get the text of the data
            """
            item.title = BeautifulSoup(''.join(item.title), "lxml")
            item.title.find(text=re.compile("CDATA"))
            item.title = item.title.text

        if item.link:
            """get the text of the data"""
            item.link = item.link.text

        if item.description:
            """
            create a BeautifulSoup class object with "lxml" parameter to obtain data,
            convert data to read CDATA fields,
            get the text of the data
            """
            item.description = BeautifulSoup(''.join(item.description), "lxml")
            item.description.find(text=re.compile("CDATA"))
            if item.description:
                """Check for the image in the description section"""
                # noinspection PyBroadException
                try:
                    """get a link to the image"""
                    img = item.description.a.img["src"]
                except Exception:
                    """if there is no image then skip"""
                    pass
            item.description = item.description.text

        if item.pubDate:
            """get the text of the data"""
            item.pubDate = item.pubDate.text

        if img is None:
            for img_key in img_keys:
                """If the image is not found in the description, then look for it in possible tags from the list"""
                if item.find(img_key) is not None:
                    """If the image is found get a link to the image"""
                    img = item.find(img_key)["url"]

        return {
            "url": self.url,
            "title": item.title,
            "link": item.link,
            "description": item.description,
            "pubdate": item.pubDate,
            "image": img
        }

    def __str__(self):
        """returns RSS-feed news data"""
        return self.raw_news