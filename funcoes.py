# meu_nome = input('digite seu nome: ')



# #def meu_nome_func():
#     # var_controle = False
#     meu_nome = input('digite seu nome: ')
#     if meu_nome == 'david':
#         var_controle = True
#     print('ola mundo, meu nome é: ', meu_nome)
#     return var_controle

# retorno = meu_nome_func()
# if retorno:
#     print ('nome valido')
# else:
#     print ('nome invalido')



def soma_dois_numeros (x, y):
    return x + y

def soma_numeros(*args):
    soma = 0
    for numero in args:
        soma = soma + numero
    return soma


resultado_da_soma = soma_dois_numeros (1,2)
print(resultado_da_soma)
soma_varios_num = soma_numeros(1,2,3,4,5)
print (soma_varios_num)

def descricao_livro(titulo, autor ='desconhecido'):
    print('o livro: {} autor : {}'.format (titulo, autor))

descricao_livro ( ' O menino maluquinho', 'antonio')
descricao_livro ( titulo=' O menino maluquinho')

def descricao_livro2(**kwargs):
    for chave in kwargs:
        print(chave + ' : ' + kwargs[chave])


