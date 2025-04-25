from weakref import ProxyType
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


browser = webdriver.Edge()
browser.get("https://cybearshield.uk")
browser.maximize_window()
browser.implicitly_wait(20)
wait = WebDriverWait(browser, 10)
element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Github")))  # Note the casing
element.click()


windows = browser.window_handles
browser.switch_to.window(windows[-1])

print(browser.title)

repos = wait.until(EC.presence_of_all_elements_located(
    (By.CSS_SELECTOR, 'li.pinned-item-list-item')
))


if len(repos) >= 2:
    link = repos[1].find_element(By.CSS_SELECTOR, 'span.repo')
    link.click()
else:
    print("Less than 2 pinned repos found.")



time.sleep(150)