from selenium import webdriver
from selenium.webdriver.common.by import By

# <div class="d-flex ai-center jc-end w-100"><span class="text-h4 ml-1 color-800">۲,۰۱۰,۰۰۰</span></div>

driver = webdriver.Chrome()

driver.get(
    "https://www.digikala.com/product/dkp-8511012/%D8%A7%D8%AA%D9%88-%D8%A8%D8%AE%D8%A7%D8%B1-%D9%81%DB%8C%D9%84%DB%8C%D9%BE%D8%B3-%D9%85%D8%AF%D9%84-dst5010/")
driver.implicitly_wait(10)
price_char = driver.find_element(by=By.CSS_SELECTOR,
                                value="div.d-flex.ai-center.jc-end.w-100 "
                                      "> span.text-h4.ml-1.color-800")

print_int = int(price_char.text.split(" ")[0].replace(",", ""))
print(print_int)

# text_box = driver.find_element(by=By.NAME, value="my-text")
# price = driver.find_element(by=By.CSS_SELECTOR, value="d-flex ai-center jc-end w-100")
# print(price)

driver.quit()
