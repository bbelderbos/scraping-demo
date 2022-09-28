from datetime import date

import requests
import dateparser
from bs4 import BeautifulSoup

from translator import translate_text

BLOG_URL = "https://blogrecursoseducatiusmarian.blogspot.com/"
END_MARK = "Publicado por"


def parse_articles(filter_date: date, url=BLOG_URL):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("div", {"class": "date-outer"})

    for article in articles:
        date_str = article.find("h2").text
        article_date = dateparser.parse(date_str)
        if filter_date != article_date.date():
            continue

        content = article.find(
            "div", {"class": "post-outer"}
        ).text.strip().replace("\xa0", "")

        end_mark_index = content.find(END_MARK)
        content = content[:end_mark_index]

        # given the history of the blog, I think we can
        # safely assume there will be max one post a day
        return content
