import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Чекаємо поки ціна не знизиться до 100$
    price = WebDriverWait(browser, 12).\
             until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    button_book = browser.find_element(By.CSS_SELECTOR, "#book").click()

    num = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    res = calc(num)

    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(res)

    browser.find_element(By.CSS_SELECTOR, "[type = 'submit']").click()

    # Вытащить данные из модального окна с ответом
    alert = browser.switch_to.alert
    alert_text = alert.text
    send_to_clipboard = alert_text.split(': ')[-1]
    pyperclip.copy(send_to_clipboard)
    print(send_to_clipboard)
    alert.accept()
    # pyperclip.paste()

except:
    pass
finally:
    time.sleep(5)
    browser.quit()