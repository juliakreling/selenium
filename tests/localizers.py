"""The localizers of functions page
"""

from selenium.webdriver.common.by import By

INPUT_NAME = (By.XPATH,
              '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')

EXPERIENCE_ELEMENT = (By.XPATH, '//*[@id="i15"]/div[3]/div')

TECHNOLOGIES_QUESTION = (
    By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]')

TECHNOLOGIES = ['i30', 'i33', 'i39', 'i45', 'i48', 'i51']

BIRTH_ELEMENT = (
    By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')

SEND_BUTTON = (
    By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
