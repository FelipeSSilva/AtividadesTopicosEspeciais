from selenium import webdriver
browser = webdriver.Chrome('chromedriver.exe')
browser.get('https://www.saraiva.com.br/')

input = browser.find_element_by_css_selector('#q')
input.send_keys('A dama oculta')

botaoBusca = browser.find_element_by_css_selector('#chaordic-search-button-img')
botaoBusca.click()

produto = browser.find_elements_by_class_name('nm-product-info')
print(produto[0].text)

browser.close()