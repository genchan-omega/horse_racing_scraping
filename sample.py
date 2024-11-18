from selenium import webdriver

cService = webdriver.ChromeService(executable_path="/Users/genchan_omega/Downloads/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service = cService)
driver.implicitly_wait(10)
driver.get('https://www.jra.go.jp/datafile/seiseki/replay/2024/jyusyo.html')

e1 = driver.find_element_by_class_name('result')
print(e1)