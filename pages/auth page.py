from pages.base import WebPage
from pages.elements import WebElement


class AuthPage(WebPage):
    def __init__(self, web_driver, url):
        super().__init__(web_driver, url)
    title_authorization = WebElement(xpath="//h1[contains(text(),'Авторизация')]")
    user_name = WebElement(id='username')
    password = WebElement(id='password')
    tab_phone = WebElement(id="t-btn-tab-phone")
    tab_email = WebElement(id="t-btn-tab-mail")
    tab_login = WebElement(id="t-btn-tab-login")
    tab_l_s = WebElement(id="t-btn-tab-ls")

    button_enter = WebElement(id="kc-login")
    button_enter_with_password = WebElement(id="standard_auth_btn")
    button_enter_for_key_rt = WebElement(xpath="//a[contains(text(),'Войти')]")

    span_incorrect_phone_format = WebElement(xpath="//span[contains(text(),'Неверный формат телефона')]")
    span_invalid_username_or_password = WebElement(xpath="//span[contains(text(),'Неверный логин или пароль')]")
    message_from_system_invalid_username_or_captcha = WebElement(id="form-error-message")

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

    captcha = WebElement(css_selector=".rt-captcha__image")
    captcha_input = WebElement(id='captcha')

    button_reset_password = WebElement(id="t-btn-reset-pass")
    button_forgot_password = WebElement(id="forgot_password")
    button_continue_form_1 = WebElement(id="reset")
    button_continue_form_2 = WebElement(css_selector=".reset-choice-form__reset-btn")
    button_back = WebElement(id="reset-back")
    input_code = WebElement(id="rt-code-0")

    title_password_recovery = WebElement(xpath="//h1[contains(text(),'Восстановление пароля')]")
    password_new = WebElement(id="password-new")
    password_confirm = WebElement(id="password-confirm")

    radio_btn_phone = WebElement(xpath='//input[@value="sms"]//ancestor::label//span[@class="rt-radio__circle"]')

    radio_btn_email = WebElement(xpath='//input[@value="email"]//ancestor::label//span[@class="rt-radio__circle"]')
