import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from models.post import Post
from instabot.bot.bot_photo import upload_photo

chrome = webdriver.Chrome("G:/ChromeDriver/chromedriver.exe")
chrome.get("https://www.instagram.com")

username = WebDriverWait(chrome, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))

password = WebDriverWait(chrome, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.clear()
password.clear()

user_text = input("Enter username")
pass_text = input("Enter password")

username.send_keys(user_text)
password.send_keys(pass_text)


button = WebDriverWait(chrome, 2).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "button[type='submit']"))).click()

not_now = WebDriverWait(chrome, 10).until(EC.element_to_be_clickable(
    (By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
not_now2 = WebDriverWait(chrome, 10).until(EC.element_to_be_clickable(
    (By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

create_btn = WebDriverWait(chrome, 10).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="mount_0_0_6Q"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/div/a'))).click()

select_btn = WebDriverWait(chrome, 10).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="mount_0_0_6Q"]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/button'))).click()
