import pytest
from pages.main_page import MainPage

def test_base_url(base_url, main_page):
    assert main_page.url == base_url

#def test_page_open(selenium, base_url, variables):
#    my_page = MainPage(selenium, base_url, variables)
#    my_page.open_key_presses_page()