moeda5 = 0.05
moeda10 = 0.10
moeda25 = 0.25
moeda50 = 0.50
moeda1 = 1.00

quantidade5 = float(input('digite a quantidade de moedas de 5 centavos: '))
quantidade10 = float(input('digite a quantidade de moedas de 10 centavos: '))
quantidade25 = float(input('digite a quantidade de moedas de 25 centavos: '))
quanatidade50 = float(input('digite a quantidade de moedas de 50 centavos: '))
quantidade1 = float(input('digite a quantidade de moedas de 1 real: '))

resultado1 = (moeda5 * quantidade5)
resultado2 = (moeda10 * quantidade10)
resultado3 = (moeda25 * quantidade25)
resultado4 = (moeda50 * quanatidade50)
resultado5 = (moeda1 * quantidade1)


print('valor em moedas de 5 centavos é de: ', resultado1)
print('valor em moedas em moedas de 10 centavos é de: ', resultado2)
print('valor em moedas de 25 centavos é de: ', resultado3)
print('valor em moedas de 50 centavos é de: ', resultado4)
print('valor em moedas de 1 real é de: ', resultado1)

resultado_final = (resultado1 + resultado2 + resultado3 + resultado4 + resultado5)

print ('o valor total em moedas é de',resultado_final,'reais.')





