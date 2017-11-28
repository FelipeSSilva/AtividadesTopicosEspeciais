import time
from selenium import webdriver


print('Os indicadores disponíveis: \npopulacao \nmatriculas \nrenda \nidh \narea \n\n')
indicador = input('Digite o indicador desejado : ')
estados = [str(x) for x in input('Digite o nome do(s) Estado(s): ').split(',')]

browser = webdriver.Chrome('chromedriver.exe')
browser.get('https://cidades.ibge.gov.br/')

indicadoresEstados = {}

for estado in estados:
    inputBuscaEstado = browser.find_element_by_css_selector('.busca__input')
    inputBuscaEstado.send_keys(estado)

    time.sleep(2)

    resultado = browser.find_element_by_class_name('busca__auto-completar__resultado__item')

    resultado.click()

    time.sleep(2)

    if indicador == 'populacao':
        indicadorValor = browser.find_element_by_xpath('//*[@id="detalhes"]/panorama-temas/panorama-painel[1]/div/div[1]/panorama-card[1]/div/div[2]')
        indicadorValor = indicadorValor.text
        indicadorValor = indicadorValor.replace(' pessoas', '')
        indicadorValor = int(indicadorValor.replace('.', ''))
        indicadoresEstados[estado] = indicadorValor

    if indicador == 'matriculas':
        indicadorValor = browser.find_element_by_xpath('//*[@id="detalhes"]/panorama-temas/panorama-painel[2]/div/div[1]/panorama-card/div/div[2]')
        indicadorValor = indicadorValor.text
        indicadorValor = indicadorValor.replace(' matrículas', '')
        indicadorValor = int(indicadorValor.replace('.', ''))
        indicadoresEstados[estado] = indicadorValor

    if indicador == 'renda':
        indicadorValor = browser.find_element_by_xpath('//*[@id="detalhes"]/panorama-temas/panorama-painel[3]/div/div[1]/panorama-card[1]/div/div[2]')
        indicadorValor = indicadorValor.text
        indicadorValor = indicadorValor.replace(' R$', '')
        indicadorValor = int(indicadorValor.replace('.', ''))
        indicadoresEstados[estado] = indicadorValor

    if indicador == 'idh':
        indicadorValor = browser.find_element_by_xpath('//*[@id="detalhes"]/panorama-temas/panorama-painel[5]/div/div[1]/panorama-card[1]/div/div[2]')
        indicadorValor = indicadorValor.text
        indicadorValor = float(indicadorValor.replace(',', '.'))
        indicadoresEstados[estado] = indicadorValor

    if indicador == 'area':
        indicadorValor = browser.find_element_by_xpath('//*[@id="detalhes"]/panorama-temas/panorama-painel[6]/div/div[1]/panorama-card/div/div[2]')
        indicadorValor = indicadorValor.text
        indicadorValor = indicadorValor.replace(' km²', '')
        indicadorValor = int(indicadorValor.replace('.', ''))
        indicadoresEstados[estado] = indicadorValor

print('##########################################')
print(indicadoresEstados)
print('Ordenando ... \n\n')

for indicadores in sorted(indicadoresEstados, key = indicadoresEstados.get,reverse=True):
    print(indicadores,indicadoresEstados[indicadores])

browser.close()