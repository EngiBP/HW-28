import pytest
from pages.auth_temp_page import AuthPageTemp
from settings import verification_code, captcha, EMAIL, PHONE


def test_auth_temp_check_webelements(web_browser):
    page = AuthPageTemp(web_browser, url="https://my.rt.ru/")
    page.wait_page_loaded()

    assert page.hint_enter_the_number.is_visible()
    assert page.input_address.is_visible()
    assert page.button_get_code.is_visible()
    web_browser.quit()


@pytest.mark.parametrize('address', [EMAIL, PHONE])
def test_temp_authorisation_positive(web_browser, address):
    page = AuthPageTemp(web_browser, url='https://my.rt.ru/')
    page.wait_page_loaded()
    page.input_address.send_keys(address)
    while page.countdown.is_visible():
        page.message_for_test_in_page("Ждем пока система даст возможность получить второй код")
        page.wait_page_loaded(sleep_time=5)

    if page.captcha.is_presented():
        image_captcha = page.captcha.get_attribute('src')
        result_captcha = captcha(image_captcha)
        page.captcha_input.send_keys(result_captcha)

    page.button_get_code.click()
    page.input_code.send_keys(verification_code())

    if page.button_go_lk.is_visible():
        page.button_go_lk.click()

    page.wait_page_loaded()

    assert page.button_lk.is_visible()

    web_browser.quit()
