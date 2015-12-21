import pytest


@pytest.fixture(scope='session')
def sensitive_url(request, base_url):
    '''Override default fixture to ignore sensitivity'''
    return False

@pytest.fixture()
def main_page(selenium, base_url):
    from pages.main_page import MainPage
    return MainPage(base_url, selenium)
