import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

expected_text = {
    "ar": "أضف الى سلة التسوق",
    "ca": "Afegeix a la cistella",
    "cs": "Vložit do košíku",
    "da": "Læg i kurv",
    "de": "In Warenkorb legen",
    "en-gb": "Add to basket",
    "el": "Προσθήκη στο καλάθι",
    "es": "Añadir al carrito",
    "fr": "Ajouter au panier",
    "ru": "Добавить в корзину",
    "fi": "Lisää koriin" }

def test_button_add_to_basket(browser, request):
    user_language = request.config.getoption("--language")
    browser = webdriver.Chrome()
    browser.get(f"https://selenium1py.pythonanywhere.com/{user_language}/catalogue/coders-at-work_207/")
    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket") 
    button_value = button.get_attribute("value")
    assert button.get_attribute("value") == expected_text[user_language]

    browser.quit()
