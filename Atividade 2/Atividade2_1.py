from bs4 import BeautifulSoup
from crawler import download

url = 'https://www.rottentomatoes.com/browse/tv-list-1'
html = download(url)
soup = BeautifulSoup(html, 'html5lib')

series = {}
campoSeries = soup.find(class_='tv_list')
serie_nomes = campoSeries.find_all(class_='middle_col')
serie_pontuacoes = campoSeries.find_all(class_='tMeterScore')


for i in range(len(serie_pontuacoes)):
    series[serie_nomes[i].text] = serie_pontuacoes[i].text

print(series)
