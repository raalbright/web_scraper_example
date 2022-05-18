import argparse
from crawler import BestBuySearchCrawler

from helpers import write_file

def main(args):
    crawler = BestBuySearchCrawler()
    crawler.crawl(args.search_term, done=lambda results: write_file(results, args.filename, args.format))
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Scrape the BestBuy search page and write results to a file.')
    parser.add_argument('search_term', help='The term to search for.')
    parser.add_argument('--format', '-f', dest='format', choices=['json', 'csv'], default='json', help='The format of the file to be outputted. Can be either json or csv.')
    parser.add_argument('--filename', '-n', dest='filename', help='The name of the file to be outputted.')

    args = parser.parse_args()
    main(args)
