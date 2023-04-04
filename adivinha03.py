from random import randint

numero = randint (1 ,10)
tentativas =5
while tentativa > 0:

    chute = int(input ('digite seu chute: '))

if chute == numero:
    print('parabéns você acertou!')
elif chute < numero: 
    print ('você errou o numero era maior!')

else:
    print('você errou !!!! o numero era menor !!!' , numero)

print('FIM DO PROGRAMA')

