from selenium import webdriver

chrome_driver = "E:\Chrome_driver\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver)
web_link = "https://tiki.vn/su-cam-do-cuoi-cung-tai-ban-2019-p25733162.html?itm_campaign=CTP_YPD_TKA_PLA_UNK_ALL_UNK_UNK_UNK_UNK_X.27987_Y.210987_Z.573752_CN.Su-Cam-Do-Cuoi-Cung-%2528Tai-Ban-2019%2529&itm_medium=CPC&itm_source=tiki-ads&spid=39754378"

#access web_page
driver.get(web_link)
book_title = driver.find_element_by_css_selector("div.header h1.title")
print(book_title.text)

#close tab
# driver.close()
#quit browser
# driver.quit()