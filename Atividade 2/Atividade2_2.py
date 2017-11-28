from bs4 import BeautifulSoup
from crawler import download
import csv

url = 'http://www.imdb.com/chart/boxoffice'
html = download(url)
soup = BeautifulSoup(html, 'html5lib')

filmes = {}
valoresSemanal = []
valoresAcumulado = []


campoFilmes = soup.find(id='boxoffice')
nomesFilme = soup.find_all(class_='titleColumn')
valoresFilme = soup.find_all(class_='ratingColumn')
semanasFilme = soup.find_all(class_='weeksColumn')

for i in range(len(valoresFilme)):
    if int(i) % 2 == 0:
        valoresSemanal.append(valoresFilme[i].text)
    else:
        valoresAcumulado.append(valoresFilme[i].text)

listaParaGerarCsv = []
for x in range(len(valoresAcumulado)):
    listaInterna = []
    listaInterna.append(nomesFilme[x].text)
    listaInterna.append(valoresSemanal[x])
    listaInterna.append(valoresAcumulado[x])
    listaInterna.append(semanasFilme[x].text)

    listaParaGerarCsv.append(listaInterna)

with open('arquivoOutput.csv', 'w') as csvfile:
    listaFilme = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    listaFilme.writerow(["Nome","ValorSemanal","ValorAcumulado","Semanas"])
    for linha in listaParaGerarCsv:
        listaFilme.writerow(linha)

print('Salvo')
