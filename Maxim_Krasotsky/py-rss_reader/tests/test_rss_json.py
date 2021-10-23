def read_all_news_file():
    """returns data written to a json file after parsing"""
    with open("news_data/all_news.json", "r", encoding="utf-8") as news_file:
        return news_file.read()


def create_testfile():
    """creates a test file with the data of the log to check the correctness of writing data to the json file"""
    with open("tests/testfile.json", "w", encoding="utf-8") as testfile:
        with open("news_data/all_news.json", "r", encoding="utf-8") as news_file:
            news_data = read_all_news_file()
        testfile.write(news_data)


def read_testfile():
    """returns data from a test file"""
    with open("tests/testfile.json", "r", encoding="utf-8") as testfile:
        return testfile.read()


def test_news_in_json():
    """checks the correctness of the data received from the RSS feed and written to the json file"""
    create_testfile()
    test_data = read_testfile()
    assert test_data == read_all_news_file()