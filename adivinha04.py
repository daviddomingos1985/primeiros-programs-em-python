from random import randint
numero = randint (1, 50)
tentativas = 5
while tentativas > 0:
    chute = int(input('digite seu chute: '))
    if chute == numero:
        print('parabéns você acertou!')
        break
    elif chute < numero: 
        print ('você errou o numero era maior!')
    else:
        print('você errou !!!! o numero era menor !!!')
    tentativas = tentativas -1
print('FIM DO PROGRAMA')



