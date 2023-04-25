import random


while True:
    inicio = input('Você deseja continuar? [s]im ou [n]ão? ')
    if inicio == 's':
        nove_digitos = ''
        for i in range(0, 9):
            nove_digitos += str(random.randint(0, 9))
        
        
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
        print(cpf_gerado)   
    elif inicio == 'n':
        print('Você foi desconectado')
        break