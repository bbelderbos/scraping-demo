from pprint import pprint as pp
from datetime import date, datetime

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

    articles_by_date = {}
    for article in articles:
        date_str = article.find("h2").text
        article_date = dateparser.parse(date_str)
        if filter_date != article_date.date():
            continue

        content = article.find("div", {"class": "post-outer"}).text.strip().replace("\xa0", "")
        end_mark_index = content.find(END_MARK)
        content = content[:end_mark_index]

        articles_by_date[article_date] = content

    articles_by_date = sorted(articles_by_date.items(), reverse=True)
    return articles_by_date


if __name__ == "__main__":
    filter_date = date(2022, 9, 14)
    # filter_date = date.today()
    articles = parse_articles(filter_date)
    for date, content in articles:
        print(date)
        translated = translate_text(content)
        print(translated)
        print()




