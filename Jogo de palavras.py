"""
JOGO PARA O USUARIO ADVINHAR QUAL A PALAVRA SECRETA 
EU PROPONHO A PALAVRA SECRETA E DOU A POSSIBILIDADE DO USUARIO DIGITAR APENAS UMA LETRA
CONFERIR SE A LETRA DIGITADA PELO USUARIO ESTA NA PALAVRA SECRETA
SE LETRA TIVER NA PALAVRA SECRETA, EXIBA LETRA
ELSE EXIBA *
FAÇA A CONTAGEM DE TENTATIVAS DO USUARIO
"""

palavra_secreta = 'FLAMENGO'
letras_acertadas = ''
tentativas = 0


while True:
    letra_digitada = input('Digite uma letra: ').upper()
    tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''    
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else: 
            palavra_formada += '*'

    print('Palavra formada: ',palavra_formada)
        
    if palavra_formada == palavra_secreta:
        print('VOCÊ GANHOU! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas: ', tentativas)
        break
print('Acabou')

