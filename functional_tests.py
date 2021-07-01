from selenium import webdriver

browser = webdriver.Chrome("./chromedriver")
browser.get("http://localhost:8000")

assert ("worked" in browser.title), "page not found"