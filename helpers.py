import csv
import json
from typing import Optional

from bs4 import Tag

from search_result import SearchEntry


def find_title(fragment: Tag) -> Optional[str]:
    title = fragment.select_one('.sku-title a')
    return title.text.strip()
    

def find_price(fragment: Tag) -> Optional[str]:
    price_fragment = fragment.select_one('.priceView-hero-price.priceView-customer-price')
    price = price_fragment.select_one('span[aria-hidden=true]:first-child') if price_fragment is not None else None
    price_prefix = fragment.select_one('.priceView-price-prefix')
    subscription_unit = price_fragment.select_one('.priceView-subscription-units') if price_fragment is not None else None
    price_disclaimer = fragment.select_one('.priceView-price-disclaimer > span.priceView-price-disclaimer__activation')

    display_price = ""

    if price is None:
        return None

    if price is not None:
        display_price = display_price + price.text.strip()
    if price_prefix is not None:
        display_price = price_prefix.text.strip() + ' ' + display_price
    if subscription_unit is not None:
        display_price = display_price + subscription_unit.text.strip()
    if price_disclaimer is not None:
        display_price = display_price + ' ' + price_disclaimer.text.strip()

    return display_price

def is_sold_out(fragment: Tag) -> bool:
    s = fragment.select_one('.fulfillment-fulfillment-summary strong')
    print("is sold out", fragment)

    return s.text.strip().lower() == "sold out"

def _write_json(data: list[SearchEntry], filename: str) -> None:
    with open(filename, 'w') as f:
        json.dump(data, f, default=lambda o: o.__dict__, indent=2)

def _write_csv(data: list[SearchEntry], filename: str) -> None:
    with open(filename, 'w', newline='') as f:
        field_names = ['title', 'price']
        writer = csv.DictWriter(f, fieldnames=field_names)

        writer.writeheader()
        for row in data:
            writer.writerow(row.__dict__)

def write_file(data: list[SearchEntry], filename: str, format: str):
        if format == 'json':
            _write_json(data, filename)
        else:
            _write_csv(data, filename)