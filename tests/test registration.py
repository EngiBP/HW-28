import pytest
from selenium.webdriver import Keys
from settings import EMAIL
from pages.registration import RegistrationPage

@pytest.fixture(name="page_reg", scope="class")
def load_forms_to_registration(web_browser_class, url="https://lk.rt.ru/"):
    page_reg = RegistrationPage(web_browser_class, url)
    page_reg.wait_page_loaded()
    assert page_reg.title.get_text() == "Авторизация"

    page_reg.from_auth_to_registration.click()
    page_reg.wait_page_loaded()
    assert page_reg.title.get_text() == "Регистрация"
    page_reg.message_for_test_in_page("Проверяется валидация полей регистрации")
    yield page_reg
    web_browser_class.quit()


def test_registration_check_webelements(web_browser, url="https://lk.rt.ru/"):
    page_reg = RegistrationPage(web_browser, url)
    page_reg.wait_page_loaded()
    assert page_reg.title.get_text() == "Авторизация"

    page_reg.from_auth_to_registration.click()
    page_reg.wait_page_loaded()
    assert page_reg.title.get_text() == "Регистрация"

    assert page_reg.input_first_name.is_visible()
    assert page_reg.input_last_name.is_visible()
    assert page_reg.input_email_or_phone.is_visible()
    assert page_reg.input_password.is_visible()
    assert page_reg.input_password_confirm.is_visible()
    assert page_reg.button_registration.is_visible()
    web_browser.quit()


class TestRegistration:
    @pytest.mark.xfail
    def test_check_first_name_for_dash(self, page_reg):
        page_reg.input_first_name.send_keys("-Д" + Keys.TAB)
        assert not page_reg.sm_first_or_lastname_valid_format.is_visible()

    def test_check_first_name_for_not_valid_name(self, page_reg):
        page_reg.input_first_name.send_keys(Keys.CONTROL + "a" + Keys.DELETE)
        page_reg.input_first_name.send_keys("Больше двадцати символов сообщение об ошибке" + Keys.TAB)
        assert page_reg.sm_first_or_lastname_valid_format.is_visible()

    def test_check_first_name_for_valid_name(self, page_reg):
        page_reg.input_first_name.send_keys(Keys.CONTROL + "a" + Keys.DELETE)
        page_reg.input_first_name.send_keys("Дмитрий" + Keys.TAB)
        assert not page_reg.sm_first_or_lastname_valid_format.is_visible()

    @pytest.mark.xfail
    def test_check_last_name_for_dash(self, page_reg):
        page_reg.input_last_name.send_keys("-M" + Keys.TAB)
        assert not page_reg.sm_first_or_lastname_valid_format.is_visible()

    def test_check_last_name_for_not_valid_name(self, page_reg):
        page_reg.input_last_name.send_keys(Keys.CONTROL + "a" + Keys.DELETE)
        page_reg.input_last_name.send_keys("Больше двадцати символов сообщение об ошибке" + Keys.TAB)
        assert page_reg.sm_first_or_lastname_valid_format.is_visible()

    def test_check_last_name_for_valid_name(self, page_reg):
        page_reg.input_last_name.send_keys(Keys.CONTROL + "a" + Keys.DELETE)
        page_reg.input_last_name.send_keys("Никитченко" + Keys.TAB)
        assert not page_reg.sm_first_or_lastname_valid_format.is_visible()

    def test_input_email_or_phone_negative_phone(self, page_reg):
        page_reg.input_first_name.click()
        page_reg.input_email_or_phone.send_keys(Keys.CONTROL + "a" + Keys.DELETE)
        page_reg.input_email_or_phone.send_keys("+7" + Keys.TAB)
        assert page_reg.sm_required_valid_format.is_visible()

    def test_input_email_or_phone_negative_email(self, page_reg):
        page_reg.input_email_or_phone.send_keys(Keys.CONTROL + "a" + Keys.DELETE)
        page_reg.input_email_or_phone.send_keys("mail@mail" + Keys.TAB)
        assert page_reg.sm_required_valid_format.is_visible()
    
    def test_input_email_or_phone_valid_email(self, page_reg):
        page_reg.input_email_or_phone.send_keys(Keys.CONTROL + "a" + Keys.DELETE)
        page_reg.input_email_or_phone.send_keys(EMAIL + Keys.TAB)
        assert not page_reg.sm_required_valid_format.is_visible()
    
    def test_pass_must_be_at_least_8_characters_long(self, web_browser_class, page_reg):
        page_reg.input_password.send_keys("1" + Keys.TAB)
        assert page_reg.pass_must_be_at_least_8_characters_long.is_visible()

    def test_pass_must_be_no_more_than_20_characters_long(self, page_reg):
        page_reg.input_password.send_keys(Keys.CONTROL + "a" + Keys.DELETE)
        page_reg.input_password.send_keys("123456789012345678901" + Keys.TAB)
        assert page_reg.pass_must_be_no_more_than_20_characters_long.is_visible()

    def test_pass_must_contain_at_least_one_capital_letter(self, page_reg):
        page_reg.input_password.send_keys(Keys.CONTROL + "a" + Keys.DELETE)
        page_reg.input_password.send_keys("alllowerletter1!" + Keys.TAB)
        assert page_reg.pass_must_contain_at_least_one_capital_letter.is_visible()

    def test_pass_must_contain_at_least_1_special_character_or_at_least_one_digit(self, page_reg):
        page_reg.input_password.send_keys(Keys.CONTROL + "a" + Keys.DELETE)
        page_reg.input_password.send_keys("Alllowerletter" + Keys.TAB)
        assert page_reg.pass_must_contain_at_least_1_special_character_or_at_least_one_digit.is_visible()

    def test_passwords_don_t_match(self, page_reg):
        page_reg.input_password.send_keys(Keys.CONTROL + "a" + Keys.DELETE)
        page_reg.input_password.send_keys("Validpassword1!" + Keys.TAB)
        page_reg.input_password_confirm.send_keys("Mistakedpassword1!" + Keys.ENTER)
        assert page_reg.passwords_don_t_match.is_visible()

    def test_register(self, page_reg):
        page_reg.input_password_confirm.send_keys(Keys.CONTROL + "a" + Keys.DELETE)
        page_reg.input_password_confirm.send_keys("Validpassword1!" + Keys.ENTER)
        assert page_reg.title_modal.is_visible()
