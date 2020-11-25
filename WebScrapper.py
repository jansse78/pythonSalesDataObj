from selenium import webdriver

PATH = "C:\\Users\wlb5626\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.wsj.com/market-data/stocks/us/movers")