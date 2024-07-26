import pytest
from data import Url
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Firefox(options=options)
    elif request.param == 'chrome':
        options = Options()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options)
    driver.get(Url.STELLAR_BURGERS)
    yield driver
    driver.quit()
