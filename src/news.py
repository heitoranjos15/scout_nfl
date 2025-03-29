from src.utils import get_content


def run() -> list:
    url = "https://www.nfl.com/news/"
    soup = get_content(url)
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
