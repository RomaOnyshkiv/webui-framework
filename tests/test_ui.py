import pytest

from pages.home_page import GoogleHomePage
from pages.results_page import GoogleResultsPage


def test_search_in_google(browser):
    query = 'programming language'
    home_page = GoogleHomePage(browser)
    home_page.load()
    home_page.search(query)
    results_page = GoogleResultsPage(browser)
    assert results_page.link_divs_count() > 0
    assert results_page.search_input_value() == query


def test_search_another_word(browser):
    query = 'python language'
    home_page = GoogleHomePage(browser=browser)
    home_page.load()
    home_page.search(query)
    results_page = GoogleResultsPage(browser=browser)
    assert results_page.link_divs_count() > 0
    assert results_page.search_input_value() == query


@pytest.mark.parametrize('lang', ['Java language', 'C# language'])
def test_parametrized(browser, lang):
    home_page = GoogleHomePage(browser=browser)
    home_page.load()
    home_page.search(lang)
    results_page = GoogleResultsPage(browser=browser)
    assert results_page.link_divs_count() > 0
    assert results_page.search_input_value() == lang
