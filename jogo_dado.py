from random import randint
quantidade = int(input('digite a quantidade de dados: '))
tentativa = 1
valores = []
while tentativa <= quantidade:
    valor = randint(1, 6)
    print(valor)
    valores.append(valor)
    tentativa = tentativa + 1
print('total: ', sum (valores))
print('media: ', sum (valores) /quantidade) 
print('maior: ', max(valores))
print('menor: ', min(valores))   
print('fim do jogo')  







