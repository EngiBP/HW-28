from pages.base import WebPage
from pages.elements import WebElement


class RegistrationPage(WebPage):

    def __init__(self, web_driver, url):
        super().__init__(web_driver, url)

    title = WebElement(css_selector=".card-container__title")
    title_modal = WebElement(css_selector='.card-modal__title')
    from_auth_to_registration = WebElement(id="kc-register")
    input_first_name = WebElement(name="firstName")
    input_last_name = WebElement(name="lastName")
    input_region = WebElement(css_selector='.rt-input__input--rounded rt-input__input--orange')
    input_email_or_phone = WebElement(id="address")
    input_password = WebElement(id="password")
    input_password_confirm = WebElement(id="password-confirm")
    button_registration = WebElement(name="register")
    sm_first_or_lastname_valid_format = WebElement(xpath="//span[contains(text(), 'Необходимо заполнить поле "
                                                         "кириллицей. От 2 до 30 символов.')]")
    sm_required_valid_format = WebElement(xpath="//span[contains(text(), 'Введите телефон в формате +7ХХХХХХХХХХ или "
                                                "+375XXXXXXXXX, или email в формате example@email.ru')]")
    pass_must_be_at_least_8_characters_long = WebElement(xpath="//span[contains(text(), 'Длина пароля должна быть "
                                                               "не менее 8 символов')]")
    pass_must_be_no_more_than_20_characters_long = WebElement(xpath="//span[contains(text(), 'Длина пароля должна "
                                                                    "быть не более 20 символов')]")
    pass_must_contain_at_least_one_capital_letter = WebElement(xpath="//span[contains(text(), 'Пароль должен "
                                                                     "содержать хотя бы одну заглавную букву')]")
    pass_must_contain_at_least_1_special_character_or_at_least_one_digit = WebElement(xpath="//span[contains(text(), "
                                                                                            "'Пароль должен содержать"
                                                                                            " хотя бы 1 спецсимвол "
                                                                                            "или хотя бы одну цифру')]")
    passwords_don_t_match = WebElement(xpath="//span[contains(text(),'Пароли не совпадают')]")