from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()

porco1 = [1, 1, 0]
porco2 = [1, 1, 0]
porco3 = [1, 1, 0]
cachorro1 = [1, 1, 1]
cachorro2 = [0, 1, 1]
cachorro3 = [0, 1, 1]
cachorro4 = [0 ,0, 1]

dados = [porco1, porco2, porco3,
cachorro1, cachorro2, cachorro3,cachorro4]

marcacoes = [1, 1, 1, -1, -1, -1,-1]

misterioso1 = [1, 1, 1]
misterioso2 = [1, 0, 0]

modelo.fit(dados, marcacoes)
# print(modelo.predict([misterioso1]))

animais = []
animais.append([0,0,0])
animais.append([1,1,0])
animais.append([1,0,0])
animais.append([0,1,0])
animais.append([0,0,1])
animais.append([0,0,1])
animais.append([0,1,1])
animais.append([1,1,1])
animais.append([1,0,1])

gabarito = [1,1,1,1,-1,-1,-1,-1,-1]
cont = 0
acertos = 0
erros = 0

for animal in animais:
    if gabarito[cont] == modelo.predict([animal]):
        acertos = acertos + 1
    else:
        erros = erros + 1

    cont = cont + 1

taxaDeAcerto = (acertos * 100) / (acertos + erros)

print('Taxa de acerto igual a ' + str(taxaDeAcerto) + '%')