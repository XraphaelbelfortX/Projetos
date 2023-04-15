""" 
EXERCÍCIO 
PEDIR PARA O USUARIO DIGITAR SEU NOME
PEDIR PARA DIGITAR IDADE
SE NOME E IDADE FOREM DIGITADOS
    EXIBIR:
        SEU NOME É {NOME}
        SEU NOME INVERTIDO É {NOME INVERTIDO}
        SEU NOME NÃO CONTEM OU CONTEM ESPAÇOS
        SEU NOME TEM {N} LETRAS
        A PRIMEIRA LETRA DO SEU NOME É {LETRA}
        A ULTIMA LETRA DO SEU NOME É {LETRA}
        
SE NADA FOR DIGITADO EM NOME OU IDADE :
    EXIBA:
        'DESCULPE VOCE DEIXOU OS CAMPOS VAZIOS'
"""
nome = input('Digite seu nome completo:')
idade = input('Digite sua idade:')

if nome and idade:
    print('Seu nome é',nome)
    print('Seu nome invertido é',nome[::-1])
    if ' ' in nome:
        print('Seu nome contém espaços!')
    else:
        print('Seu nome NÃO CONTÉM espaços!')
    print('A primeira letra do seu nome é',nome[0:1])
    print('Seu nome tem',len(nome),'carácteres')
    print('A ultima letra do seu nome é', nome[-1::])

else:
    print('Desculpe, você deixou os campos vazios')


