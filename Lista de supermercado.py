"""
FAZER UMA LISTA DE COMPRAS COM LISTAS
O USUARIO DEVE TER A POSSIBILIDADE DE INSERIR
APAGAR E LISTAR VALORES EM SUA LISTA
NÃO PERMITA QUE O PRORAMA QUEBRE COM
ERROS DE INDICES INEXISTENTES NA LISTA:
"""

import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ') 
        
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Não foi possível apagar esse índice')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
            

    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l')


