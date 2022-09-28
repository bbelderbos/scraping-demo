from datetime import date
import sys

from scraper import parse_articles
from translator import translate_text


def main(filter_date):
    articles = parse_articles(filter_date)
    if len(articles) == 0:
        print("Nothing new")
        return

    for entry_date, content in articles:
        print(entry_date)
        translated = translate_text(content)
        print(translated)
        print()

    # TODO: send this in an email :)


if __name__ == "__main__":
    # to keep it very simple, could add Typer and
    # also pass down args for translate_text's
    # headless and slow_mo options
    if len(sys.argv) == 4:
        try:
            year, month, day = sys.argv[1:]
            filter_date = date(
                int(year), int(month), int(day))
        except ValueError:
            print(f"Usage: {sys.argv[0]} year month day")
            sys.exit(1)
    else:
        filter_date = date.today()

    main(filter_date)
