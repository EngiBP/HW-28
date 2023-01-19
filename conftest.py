import pytest
import allure
import uuid

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture
def web_browser(request):
    options = Options()
    options.headless = False
    options.add_argument('--ignore-certificate-errors')
    browser = webdriver.Chrome(options=options)
    browser.set_window_size(1400, 1000)

    yield browser


    if request.node.rep_call.failed:
       try:
            browser.execute_script("document.body.bgColor = 'white';")

            browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')

            allure.attach(browser.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)

            print('URL: ', browser.current_url)
            print('Browser logs:')
            for log in browser.get_log('browser'):
                print(log)

       except:
          pass


@pytest.fixture(scope="class")
def web_browser_class():
    options = Options()
    options.headless = False
    options.add_argument('--ignore-certificate-errors')
    browser = webdriver.Chrome(options=options)
    browser.set_window_size(1400, 1000)

    yield browser


def get_test_case_docstring(item):

    full_name = ''

    if item._obj.__doc__:
        name = str(item._obj.__doc__.split('.')[0]).strip()
        full_name = ' '.join(name.split())

        if hasattr(item, 'callspec'):
            params = item.callspec.params

            res_keys = sorted([k for k in params])
            res = ['{0}_"{1}"'.format(k, params[k]) for k in res_keys]
            full_name += ' Parameters ' + str(', '.join(res))
            full_name = full_name.replace(':', '')

    return full_name


def pytest_itemcollected(item):

    if item._obj.__doc__:
        item._nodeid = get_test_case_docstring(item)


def pytest_collection_finish(session):

    if session.config.option.collectonly is True:
        for item in session.items:
           if item._obj.__doc__:
                full_name = get_test_case_docstring(item)
                print(full_name)

        pytest.exit('Done!')
