import pytest
from pages.key_press_page import KeyPressPage

def test_key_q(main_page):
    '''Tests Key Press Page for the key press: Q'''
    main_page.open()
    key_page = main_page.open_key_presses_page()
    key_page.type("q")
    assert key_page.result == "You entered: Q"
