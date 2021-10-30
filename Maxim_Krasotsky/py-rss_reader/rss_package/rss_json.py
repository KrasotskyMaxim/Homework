import json


def news_in_json(path, news):
    """writes the received news of the RSS feed to a file

    parameters:
    path -- let the file to write the data
    news -- recorded news
    """
    # noinspection PyBroadException
    try:
        with open(path, "w", encoding="utf-8") as file:
            """open the file to record the data and display the message from the successful record"""
            json.dump(news, file, indent=4, ensure_ascii=False)
            print("\n\nData is written!\n\n")
    except Exception:
        """print an explanatory error message and the error itself"""
        print("Couldn`t write in file!")
        print(Exception)
