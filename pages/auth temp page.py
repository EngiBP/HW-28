from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements


class AuthPageTemp(WebPage):
    def __init__(self, web_driver, url):
        super().__init__(web_driver, url)
    input_address = WebElement(id='address')
    button_get_code = WebElement(id="otp_get_code")
    input_code = WebElement(id="rt-code-0")
    button_go_lk = WebElement(xpath='//a[contains(text(), "Перейти")]')
    countdown = WebElement(css_selector='.otp-form__timeout')
    hint_enter_the_number = WebElement(xpath="//p[contains(text(),'Укажите почту или номер телефона')]")
    captcha = WebElement(css_selector=".rt-captcha__image")
    captcha_input = WebElement(id='captcha')
    button_lk = WebElement(id="lk-btn")
