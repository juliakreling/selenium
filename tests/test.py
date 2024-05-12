"""Send form test case
"""

from selenium.webdriver import Chrome
from chromedriver_py import binary_path
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from functions import Functions
from selenium.webdriver.support.wait import WebDriverWait

URL = 'https://forms.gle/omzv1uSvEt7sWQ6dA'
NAME = 'Julia Gabriele Kreling'
BIRTH_DATE = '14111998'


class FormGoogleTest:

    def main():
        driver = Chrome(executable_path=binary_path)
        wait = WebDriverWait(driver, 10)
        functions = Functions()

        functions.open_browser(driver, wait, URL)
        sleep(2)
        functions.input_name(driver, wait, NAME)
        functions.select_experience(driver, wait)
        functions.select_technologies(driver, wait)
        functions.input_birth_date(driver, wait, BIRTH_DATE)
        sleep(2)
        functions.cick_send_button(driver, wait)

    if __name__ == '__main__':
        main()
