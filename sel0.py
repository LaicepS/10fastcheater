from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()
browser.get("https://10fastfingers.com/typing-test/french")
wordlist = browser.find_elements_by_css_selector("[wordnr]")
words = map(lambda x: x.text, wordlist)
input = browser.find_element_by_id("inputfield")

for w in words:
    for c in w:
        input.send_keys(c)
        sleep(0.05)
    from selenium.webdriver.common.keys import Keys
    input.send_keys(Keys.SPACE)
