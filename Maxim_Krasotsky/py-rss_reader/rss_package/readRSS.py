"""contains a class for parsing RSS feeds"""

import sys
import requests
from bs4 import BeautifulSoup
import re
import json


class ReadRSS:

    """Contains methods for processing RSS feeds depending on the settings passed"""

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
                """print the status of the request"""
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

    def _news_in_json(self, path: str):
        """writes the received news of the RSS feed to a file

        parameters:
        path -- let the file to write the data

        """
        # noinspection PyBroadException
        try:
            with open(path, "w", encoding="utf-8") as file:
                """open the file to record the data and display the message from the successful record"""
                json.dump(self.raw_news, file, indent=4, ensure_ascii=False)
        except Exception:
            """print an explanatory error message and the error itself"""
            print("Couldn`t write in file!")
            print(Exception)

    @staticmethod
    def _news_to_text(news: dict):
        """generates news in a readable form

        parameters:
        news -- dictionary with news data

        returns a list of news data in a readable form

        """
        title = news["title"] if news["title"] else "No title"
        link = news["link"]
        description = (news["description"] if news["description"] else "No description")
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

    @staticmethod
    def _create_news(item):
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
            "title": item.title,
            "description": item.description,
            "pubdate": item.pubDate,
            "image": img,
            "link": item.link
        }

    def __str__(self):
        """sets the number of news received depending on the --limit setting

        return the result of the program in the form of readable text
        or writes to a json file in the form of a list of dictionaries
        """
        news_count = self.settings["limit"]

        """create a list of news RSS-feed"""
        self.raw_news = [self._create_news(item) for item in self.items[0:news_count]]
        if self.settings["json"]:
            """write the created news list to a json file"""
            self._news_in_json("all_news.json")
            return "\nData is written!\n"
        else:
            """create a list of readable news"""
            readable_text = [self._news_to_text(news) for news in self.raw_news]
            return f"{self.channel_title}\n\n" + "\n".join(readable_text)