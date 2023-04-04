from random import randint

numero = randint (1 ,10)

chute = int(input ('digite seu chute: '))

if chute == numero:
    print('parabéns você acertou!')

else:
    print('você errou !!!! o numero era:' , numero)

print('FIM DO PROGRAMA')
