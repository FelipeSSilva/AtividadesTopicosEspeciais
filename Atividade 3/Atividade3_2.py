from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()

# Tem asas? Possui veneno? Consegue cuspir fogo? Tem quatro patas?
dragaoComum = [1, 1, 1, 1]
dragaoOriental = [0, 0, 1, 1]
dragaoFicao = [1, 0, 1, 1]
wyernComum = [1, 1, 0, 0]
wyernOcidental = [1, 0, 0, 0]
wyernFicao = [1, 0, 1, 0]


dados = [dragaoComum, dragaoOriental, dragaoFicao,wyernComum, wyernOcidental, wyernFicao]
marcacoes = [1, 1, 1, -1, -1, -1]

modelo.fit(dados, marcacoes)


lendas = []
lendas.append([0,0,0,0]) #Wyvern
lendas.append([0,0,1,0]) #Wyvern
lendas.append([0,1,1,0]) #Wyvern
lendas.append([1,1,1,0]) #Wyvern
lendas.append([1,1,0,0]) #Wyvern
lendas.append([1,0,0,0]) #Wyvern
lendas.append([0,0,0,1]) #Dragão
lendas.append([0,0,1,1]) #Dragão
lendas.append([0,1,1,1]) #Dragão
lendas.append([1,1,1,1]) #Dragão
lendas.append([1,1,0,1]) #Dragão
lendas.append([1,0,0,1]) #Dragão
lendas.append([0,0,0,1]) #Dragão

gabarito = [-1,-1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1]
cont = 0
acertos = 0
erros = 0

for lenda in lendas:
    if gabarito[cont] == modelo.predict([lenda]):
        acertos = acertos + 1
    else:
        erros = erros + 1

    cont = cont + 1

taxaDeAcerto = (acertos * 100) / (acertos + erros)

print('Taxa de acerto igual a ' + str(taxaDeAcerto) + '%')