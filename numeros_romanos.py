def convercao(numero):
    lista = ['I', 'V,', 'X']
    if numero <= 3:
        return 'I'*numero
    elif numero == 4:
        return 'IV'
    elif numero == 5:
        return 'V'
    elif numero % 10 == 0 and int(numero/10) <= 3:
        repetir = int(numero/10)
        return str(lista[2] * repetir)





numero = int(input('Digite o numero: '))

numero_romano = convercao(numero)
print('numero em romano: ', numero_romano)