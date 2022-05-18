from bs4 import BeautifulSoup

import helpers


def test_it_can_find_price():
    with open('data/price.html') as html:
        fragment = BeautifulSoup(html, 'html.parser')
        expected = '$129.99'
        actual = helpers.find_price(fragment)
        print(actual, expected)

        assert expected == actual

def test_it_can_find_price_with_save():
    with open('data/price_with_save.html') as html:
        fragment = BeautifulSoup(html, 'html.parser')
        expected = '$359.99'
        actual = helpers.find_price(fragment)
        print(actual, expected)

        assert expected == actual

def test_it_can_find_price_with_starting_at():
    with open('data/price_with_starting_at.html') as html:
        fragment = BeautifulSoup(html, 'html.parser')
        expected = 'Starting at $899.99 with activation today'
        actual = helpers.find_price(fragment)
        print(actual, expected)

        assert expected == actual

def test_find_price_returns_None_when_no_price_displayed():
    with open('data/no_price_displayed.html') as html:
        fragment = BeautifulSoup(html, 'html.parser')
        expected = None
        actual = helpers.find_price(fragment)
        print(actual, expected)

        assert expected == actual

def test_find_price_when_sold_out():
    with open('data/sold_out_with_price.html') as html:
        fragment = BeautifulSoup(html, 'html.parser')
        expected = '$299.99'
        actual = helpers.find_price(fragment)
        print(actual, expected)

        assert expected == actual

def test_it_can_find_price_with_subscription_info():
    with open('data/price_with_subscription.html') as html:
        fragment = BeautifulSoup(html, 'html.parser')
        expected = '$33.34/mo. for 36 months; 0% APR'
        actual = helpers.find_price(fragment)
        print(actual, expected)

        assert expected == actual