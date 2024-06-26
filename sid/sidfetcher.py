from typing import Callable

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import psutil
from globalvariable import readContext
import urllib.request
from selenium.webdriver import FirefoxOptions


getsid = Callable[[None], str]

def getsid3() -> str:
    driver = webdriver.Firefox()
    link = readContext().getVariable("SIDURL")
    driver.get(link)
    time.sleep(3)
    url = driver.current_url
    driver.quit()
    return sidextractor(url)


def sidextractor(url: str) -> str:
    try:
        return url.split("sid=")[1]
    except Exception as ex:
        print("Some exception while getting sid")
