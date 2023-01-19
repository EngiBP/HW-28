import pytest
from settings import captcha, verification_code, PHONE, EMAIL
from selenium.webdriver import Keys
from pages.auth_page import AuthPage


@pytest.fixture(name="page", scope="class")
def load_forms_to_recovery_pass(web_browser_class, url="https://lk.rt.ru/"):
    page = AuthPage(web_browser_class, url)
    page.wait_page_loaded()
    page.button_forgot_password.click()
    page.wait_page_loaded()

    assert page.title_password_recovery.is_presented()
    count = 1
    while True:
        page.message_for_test_in_page("Решается каптча, через автосервис", count)
        image_captcha = page.captcha.get_attribute('src')
        result_captcha = captcha(image_captcha)

        page.tab_email.click()
        page.user_name.send_keys(EMAIL)
        page.captcha_input.send_keys(result_captcha)
        page.button_continue_form_1.click()
        page.wait_page_loaded()
        count += 1
        if not page.message_from_system_invalid_username_or_captcha.is_presented():
            break

    assert page.radio_btn_phone.is_presented()
    assert page.radio_btn_email.is_presented()

    page.radio_btn_email.click()
    page.button_continue_form_2.click()
    page.wait_page_loaded()
    count = 1
    while True:
        page.message_for_test_in_page("Ищем подходящий код на почте", count)
        page.input_code.send_keys(verification_code())
        count += 1
        if not page.message_from_system_invalid_username_or_captcha.is_presented():
            break

    yield page

    web_browser_class.quit()


def test_password_recovery_check_webelements(web_browser, url="https://lk.rt.ru/"):

    page = AuthPage(web_browser, url)
    page.wait_page_loaded()
    page.button_forgot_password.click()
    page.message_for_test_in_page("Идет проверка нахождения всех элементов на странице, в соответствии с требованиями")
    page.wait_page_loaded(sleep_time=1)
    assert page.captcha.is_presented()
    assert page.user_name.is_presented()
    assert page.button_continue_form_1.is_presented()
    assert page.button_back.is_presented()
    assert page.tab_phone.is_presented()
    assert page.tab_login.is_presented()
    assert page.tab_email.is_presented()
    assert page.tab_l_s.is_presented()

    web_browser.quit()


def test_password_recovery_check_radio_button(web_browser, url="https://lk.rt.ru/"):
    page = AuthPage(web_browser, url)
    page.wait_page_loaded()
    page.button_forgot_password.click()
    page.wait_page_loaded()

    assert page.title_password_recovery.is_presented()
    count = 1
    while True:
        page.message_for_test_in_page("Решается каптча, через автосервис", count)
        image_captcha = page.captcha.get_attribute('src')
        result_captcha = captcha(image_captcha)

        page.tab_phone.click()
        page.user_name.send_keys(PHONE)
        page.captcha_input.send_keys(result_captcha)
        page.button_continue_form_1.click()
        page.wait_page_loaded()
        count += 1
        if not page.message_from_system_invalid_username_or_captcha.is_presented():
            break
    page.message_for_test_in_page("Идет проверка нахождения radio-button на странице")
    page.wait_page_loaded(sleep_time=1)
    assert page.radio_btn_phone.is_presented()
    assert page.radio_btn_email.is_presented()

    web_browser.quit()


class TestPasswordValid:
    def test_pass_must_be_at_least_8_characters_long(self, web_browser_class, page):
        page.message_for_test_in_page("Проверяем валидацию пароля в соответствии с парольной политикой")
        page.password_new.send_keys("1" + Keys.TAB)
        assert page.pass_must_be_at_least_8_characters_long.is_visible()

    def test_pass_must_be_no_more_than_20_characters_long(self, page):
        page.password_new.send_keys(Keys.CONTROL + "a" + Keys.DELETE)
        page.password_new.send_keys("123456789012345678901" + Keys.TAB)
        assert page.pass_must_be_no_more_than_20_characters_long.is_visible()

    def test_pass_must_contain_at_least_one_capital_letter(self, page):
        page.password_new.send_keys(Keys.CONTROL + "a" + Keys.DELETE)
        page.password_new.send_keys("alllowerletter1!" + Keys.TAB)
        assert page.pass_must_contain_at_least_one_capital_letter.is_visible()

    def test_pass_must_contain_at_least_1_special_character_or_at_least_one_digit(self, page):
        page.password_new.send_keys(Keys.CONTROL + "a" + Keys.DELETE)
        page.password_new.send_keys("Alllowerletter" + Keys.TAB)
        assert page.pass_must_contain_at_least_1_special_character_or_at_least_one_digit.is_visible()

    def test_passwords_don_t_match(self, page):
        page.password_new.send_keys(Keys.CONTROL + "a" + Keys.DELETE)
        page.password_new.send_keys("Validpassword1!" + Keys.TAB)
        page.password_confirm.send_keys("Mistakedpassword1!" + Keys.ENTER)
        assert page.passwords_don_t_match.is_visible()
