"""Functions for test page
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import localizers


class Functions:
    """Functions for test page"""

    def open_browser(self, driver, wait, url: str):
        """Open the Chrome Browser

        Args:
            url (str): URL text
        """
        driver.get(url)
        driver.maximize_window()

    def input_name(self, driver, wait, name: str):
        """Input the name on the field

        Args:
            name (str): Name
        """
        input_name = wait.until(
            EC.presence_of_element_located(localizers.INPUT_NAME))
        input_name.click()
        input_name.send_keys(name)

    def select_experience(self, driver, wait):
        """Click button to select years of experience
        """
        experience = wait.until(
            EC.presence_of_element_located(localizers.EXPERIENCE_ELEMENT))
        experience.click()

    def select_technologies(self, driver, wait):
        """Click button to select the technologies
        """
        wait.until(EC.presence_of_element_located(
            localizers.TECHNOLOGIES_QUESTION))
        for elemento_id in localizers.TECHNOLOGIES:
            driver.find_element(By.ID, elemento_id).click()

    def input_birth_date(self, driver, wait, date: str):
        """Input the date of birth into the field

        Args:
            date (str): Date of birth
        """
        datanasc = wait.until(
            EC.presence_of_element_located(localizers.BIRTH_ELEMENT))
        datanasc.send_keys(date)

    def cick_send_button(self, driver, wait):
        """Click button to send form
        """
        wait.until(EC.element_to_be_clickable(
            localizers.SEND_BUTTON)).click()
