def par_ou_impar (**kwargs):
    return()


numero = int(input('"me diga um numero: '))
resultado = numero % 2
if resultado == 0:
    print (' o numero {} é par'.format(numero))
else:
    print('o numero {} é impar'. format(numero))
    
par_ou_impar()

#################################################################################

def par_impar(**kwargs):
    numero = kwargs.get('numero')
    if numero % 2 == 0:
        print("Par")
    else:
        print("Impar")

par_impar(numero=6)