from bs4 import BeautifulSoup
from crawler import download
import time

calculo = {}
contPais = 1

while True:
    url = 'http://example.webscraping.com/places/default/view/' + str(contPais)
    html = download(url)
    soup = BeautifulSoup(html, 'html5lib')
    corpo = soup.find(['body'])
    if corpo.text != 'Invalid record':

        campoArea = soup.find(id='places_area__row')
        areaPais = campoArea.find(class_='w2p_fw')
        areaPais = areaPais.text.replace(' square kilometres', '')
        areaPais = int(areaPais.replace(',', ''))

        campoPopulacao = soup.find(id='places_population__row')
        populacaoPais = campoPopulacao.find(class_='w2p_fw')
        populacaoPais = int(populacaoPais.text.replace(',', ''))


        campoNome = soup.find(id='places_currency_name__row')
        nomePais = campoNome.find(class_='w2p_fw')

        calculo[nomePais.text] = populacaoPais / areaPais

        print(calculo[nomePais.text])
        time.sleep(10)
        contPais = contPais + 1
    else:
        print(calculo)
        break

