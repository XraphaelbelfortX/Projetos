# CALCULADORA
# 1 ETAPA: PERGUNTA E RECONHECIMENTO DO SISTEMA
import time
inicio = input('Você quer realizar um cálculo? Sim ou Não?(Digite "Sim" em caso de querer continuar e "Não" ' 
    'para caso queira se desconectar do sistema) ')

if inicio == 'Sim':
    print('Você irá ser redirecionado à calculadora')
else:
    print('Você saiu do sistema')
sair = True

# 2 ETAPA: PEDIR NUMEROS E REALIZAR OPERAÇÃO

while inicio == 'Sim':
    numero = float(input('Digite um número: '))
    operacao = input('Digite o operador: ')
    numero2 = float(input('Digite outro número: '))
    operadores = '+-*/'
    op1 = (numero*numero2)
    op2 = (numero/numero2)
    op3 = (numero-numero2)
    op4 = (numero+numero2)
    op5 = (numero//numero2)
    op6 = (numero%numero2)
    op7 = (numero**numero2)

    if operacao not in operadores:
        print('Operador inválido')

    if operacao == '*':
        print(numero,'*',numero2,'é igual a',op1)
    if operacao == '/':
        print(numero,'/',numero2,'é igual a',op2)
    if operacao == '-':
        print(numero,'-',numero2,'é igual a',op3)
    if operacao == '+':
        print(numero,'+',numero2,'é igual a',op4)
    if operacao == '//':
        print(numero,'//',numero2,'é igual a',op5)
    if operacao == '%':
        print(numero,'%',numero2,'é igual a',op6)
    if operacao == '**':
        print(numero,'**',numero2,'é igual a',op7)

    perguntasair = input('Você quer [s]air? ')
    if perguntasair == 's':
        print('Você foi desconectado')
        break


    
    

