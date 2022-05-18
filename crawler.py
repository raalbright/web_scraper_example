import time
from bs4 import BeautifulSoup
import requests

from helpers import find_price, find_title
from search_result import SearchEntry

class BestBuySearchCrawler:
    __BASE_URL = 'https://www.bestbuy.com/'
    __SERCH_QUERY_PREFIX = 'site/searchpage.jsp?st='
    __HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'}

    def crawl(self, search_term, done):
        session = requests.session()
        session.headers.update(self.__HEADERS)

        try:
            page = session.get(self.__BASE_URL + self.__SERCH_QUERY_PREFIX + search_term, timeout=30)
        except requests.exceptions.RequestException as error:
            print("Request error: {0}".format(error))
        else:
            soup = BeautifulSoup(page.content, 'html.parser')
            results = []

            while True:
                search_results = soup.select('.sku-item')
                next_page_anchor = soup.select_one('.sku-list-page-next')

                for entry in search_results:
                    title = find_title(entry)
                    title = 'No title found' if title is None else title

                    price = find_price(entry)
                    price = 'No price found' if price is None else price

                    results.append(SearchEntry(title = title, price = price))

                if 'disabled' in next_page_anchor['class']:
                    break

                page = session.get(self.__BASE_URL + next_page_anchor.get('href'))
                soup = BeautifulSoup(page.content, 'html.parser')
                time.sleep(15)

            done(results)