from selenium.webdriver.common.by import By

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
    lang = (browser.user_language if hasattr(browser, 'user_language') else 'en-gb')
    browser.get(f"https://selenium1py.pythonanywhere.com/{lang}/catalogue/coders-at-work_207/")
    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket") 
    button_value = button.get_attribute("value")
    assert button_value == expected_text[lang]
