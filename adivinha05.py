from random import randint
numero = randint (1, 50)
tentativas = 5
while tentativas > 0:
    chute = int(input('digite seu chute: '))
    diferenca = numero - chute
    if diferenca == 0:
        print('parabéns você acertou!')
        break
    elif diferenca <= 5 and diferenca >= -5: 
        print ('você errou mas esta quente!')
    elif diferenca > 0:
        print ('você errou o numero era maior')
    else:
        print('você errou !!!! o numero era menor !!!')
    tentativas = tentativas -1
print('FIM DO PROGRAMA o numero era', numero)

