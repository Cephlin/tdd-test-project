from selenium import webdriver


browser = webdriver.Chrome("C:\\Users\\DICK BUTT\\Projects\\Programming\\tdd\\tdd\\tests\\chromedriver.exe")
browser.get('http://localhost:8000')
assert 'Django' in browser.title

browser.quit()
