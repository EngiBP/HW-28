import base64
import imaplib
import quopri
import email

from email.header import decode_header
from bs4 import BeautifulSoup
from time import sleep
from twocaptcha import TwoCaptcha

LOGIN = 'rtkid_1674132587690'
PHONE = '79232417245'
EMAIL = 'EngiBP@mail.ru'
PASSWORD = "Gblfnjh128500!"


def captcha(url_image):
    solver = TwoCaptcha('68c2e78aa88257e7197955850f257c24')
    result = solver.normal(url_image)
    return result['code']


def verification_code():
    imap_server = "imap.mail.ru"
    your_email = EMAIL
    password = "BEBJhkMp70bX0SbSueEn"
    count_find_email = 0

    while count_find_email <= 10:
        imap = imaplib.IMAP4_SSL(imap_server)
        imap.login(your_email, password)
        imap.select("INBOX")
        message = imap.search(None, "UNSEEN")
        _, message = message
        message = message[0]
        message_list = [int(i) for i in message.decode('UTF-8').split()]
        if len(message_list) == 0:
            count_find_email += 1
            sleep(1)
            continue
        for item in reversed(message_list):
            res, msg = imap.fetch(bytes(str(item), "utf-8"), '(RFC822)')
            msg = email.message_from_bytes(msg[0][1])
            letter_from = msg["Return-path"]
            if 'skillofftest@gmail.com' in letter_from:
                for part in msg.walk():
                    if part.get_content_maintype() == 'text' and part.get_content_subtype() == 'plain':
                        code = base64.b64decode(part.get_payload()).decode()
                        if ('Входящее - Rostelecom' and 'Соообщение: Ваш код:') in code:
                            code = "   " + code[code.find('Ваш код:') + 9: code.find('. Не')] + "   "
                            return code.strip(" ")
            if decode_header(msg["Subject"])[0][0].decode() == 'Восстановление доступа' or 'Код авторизации в личном ' \
                                                                                           'кабинете':
                for part in msg.walk():
                    if part.get_content_maintype() == 'text' and part.get_content_subtype() == 'plain':
                        code = base64.b64decode(part.get_payload()).decode()
                        code = "   " + code[code.find('Ваш код:') + 9: code.find('. Не')] + "   "
                        return code.strip(" ")
                    elif part.get_content_maintype() == 'text' and part.get_content_subtype() == 'html':
                        text = BeautifulSoup(part.get_payload(), features="html.parser")
                        text = text.p.get_text()
                        code = quopri.decodestring(text).decode('Utf-8')
                        code = "   " + code[code.find('Ваш код:') + 9: code.find('. Не')] + "   "
                        return code.strip(" ")
        count_find_email += 1
        sleep(1)
    return -1
