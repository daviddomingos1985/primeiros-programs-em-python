def fatorial(numero):
    print('numero recebido', numero)
    if numero == 0:
        return 0
    return numero * fatorial(numero -1)

retorno = fatorial (10)

print (retorno)
