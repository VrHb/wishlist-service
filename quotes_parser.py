import argparse
import os
from typing import NamedTuple
import json

import requests
from bs4 import BeautifulSoup
from loguru import logger


class Argument(NamedTuple):
    start_page: int
    end_page: int
    json_path: str


def get_arguments() -> Argument:
    parser = argparse.ArgumentParser(
        description="Парсер цитат"
    )
    parser.add_argument(
        "--start_page",
        default=1,
        help="Стартовая страница"
    )
    parser.add_argument(
        "--end_page",
        default=5,
        help="Конечная страница"
    )
    parser.add_argument(
        "--json_path",
        default=".",
        help="Путь для сохранения json с цитатами"
    )
    args = parser.parse_args()
    return Argument(
        start_page=args.start_page,
        end_page=args.end_page,
        json_path=args.json_path
    )


def parse_quotes_on_page(url: str) -> list[dict[str, str]]:
    headers = {
        "User-Agent": "Mozilla/5.0 Chrome/119.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "lxml")
    quotes_on_page = soup.find_all(class_="quote-text")
    parsed_quotes = [
        {
            "text": quote.find("p").getText(), 
            "author": quote.find("a").getText()
        } for quote in quotes_on_page
    ]
    return parsed_quotes


def main() -> None:
    arguments = get_arguments()
    page_ids = range(int(arguments.start_page), int(arguments.end_page))
    os.makedirs(arguments.json_path, exist_ok=True)
    json_path = os.path.join(arguments.json_path, "quotes.json")
    for page_id in page_ids:
        try:
            url = f"https://quote-citation.com/topic/podarok/page/{page_id}/"
            parsed_quotes_on_page = parse_quotes_on_page(url)    
            with open(json_path, "w") as file_path:
                json.dump(
                    parsed_quotes_on_page,
                    file_path,
                    indent=4,
                    ensure_ascii=False
                )
            logger.info(parsed_quotes_on_page)
        except requests.HTTPError:
            logger.exception("Такой страницы нет!")
        except requests.ConnectionError:
            logger.exception("Нет соединения с хостом!")


if __name__ == "__main__":
    main()
