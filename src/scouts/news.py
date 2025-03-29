import os
import logging
from dotenv import load_dotenv
from src.utils import get_soup


def run() -> list:
    scope = "nfl_news"
    FORMAT = f'%(asctime)-15s [{scope}] %(message)s'
    logging.basicConfig(format=FORMAT, level=logging.INFO)
    load_dotenv()
    url = os.getenv("URL_NEWS")
    soup = get_soup(url)
    contents = list()

    newsList = soup.select("div[class='d3-l-col__col-4']")
    for news in newsList:
        link = news.select_one("a").get("href").strip()
        title = news.select_one("a").get("title").strip()
        date = news.select_one(".d3-o-media-object__date")

        if date is not None:
            date_text = news.text.strip()
            contents.append({
                "date": date_text,
                "title": title,
                "link": f"{url}/{link}"
            })

    return contents
