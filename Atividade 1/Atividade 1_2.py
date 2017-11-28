from selenium import webdriver
browser = webdriver.Chrome('chromedriver.exe')

browser.get('https://www.saraiva.com.br/')

inputBuscaSaraiva = browser.find_element_by_css_selector('#q')
inputBuscaSaraiva.send_keys('A dama oculta')

botaoBuscaSaraiva = browser.find_element_by_css_selector('#chaordic-search-button-img')
botaoBuscaSaraiva.click()

livroSaraiva = browser.find_elements_by_class_name('nm-product-info')
precoSaraiva = livroSaraiva[0].find_element_by_class_name('nm-price-container')

precoSaraiva = precoSaraiva.text
precoSaraivaFloat = precoSaraiva.replace('R$ ', '')
precoSaraivaFloat = float(precoSaraivaFloat.replace(',', '.'))


browser.get('https://www.travessa.com.br/')

inputBuscaTravessa = browser.find_element_by_css_selector('#txtBusca')
inputBuscaTravessa.send_keys('A dama oculta')

botaoBuscaTravessa = browser.find_element_by_css_selector('#btnBuscar')
botaoBuscaTravessa.click()

precoTravessa = browser.find_element_by_class_name('preco')
precoTravessa = precoTravessa.text
precoTravessaFloat = precoTravessa.replace('R$ ', '')
precoTravessaFloat = float(precoTravessaFloat.replace(',', '.'))

print('Produto pesquisado: A dama oculta')
print('Preço na loja Saraiva:' + precoSaraiva)
print('Preço na loja Travessa:' + precoTravessa)

browser.close()