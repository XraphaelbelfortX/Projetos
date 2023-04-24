"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""

while True:
    inicio = input('Você deseja continuar? [s]im ou [n]ão? ')
    if inicio == 's':
        numero_cpf = input('Digite o seu número do cpf: ')

        nove_digitos = numero_cpf[:9]

        contador_regressivo = 10

        resultado1 = 0

        for digito in nove_digitos:
            resultado1 += int(digito) * contador_regressivo
            contador_regressivo -= 1
    
        digito1 = (resultado1 * 10) % 11
        digito1 = digito1 if digito1 <= 9 else 0

        dez_digitos = nove_digitos + str(digito1)
        contador_regressivo2 = 11

        resultado2 = 0

        for digito in dez_digitos:
            resultado2 += int(digito) * contador_regressivo2
            contador_regressivo2 -= 1
            digito2 = (resultado2 * 10) % 11
            digito2 = digito2 if digito2 <= 9 else 0

        cpf_gerado = f'{nove_digitos}{digito1}{digito2}'

        if numero_cpf == cpf_gerado:
            print(numero_cpf,'é valido!')
        else:
            print(numero_cpf,'é inválido')
    elif inicio == 'n':
        print('Você foi desconectado')
        break
    
