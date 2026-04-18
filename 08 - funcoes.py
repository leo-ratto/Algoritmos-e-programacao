import random
# Exercício 1
def par_ou_impar(n):
    if n % 2 != 0:
        return "Impar"
    
    else:
        return "Par"  
# Exercício 2
def tabuada(n: int) -> str:
    i = 1

    print(f'Tabuada do {n}:\n')

    while i < 11:

        print(f'{n} X {i} = {n*i}')

        i += 1
# Exercício 3
def soma_n(n: int):
    soma = 0

    i = 1 

    while i <= n:
        soma += i

        i += 1

    return soma
# Exercício 4
def fatorial(n):
    fatorial = 1

    for i in range(1, n+1, 1):
        fatorial *= i

    return fatorial
# Exercício 5
def eh_primo(n):
    
    for i in range(1, n, 1):
        if (n % i == 0) and i != 1:
            return False

    return True
# Exercício 6
def maior_digito(n):
    n = str(n)

    maior = 0

    for i in n:
        if int(i) > maior:
            maior = int(i)

    return maior
# Exercício 7
def inverter_numero(n):
    n = str(n)

    invertido = int(n[::-1])

    return invertido
# Exercício 8
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    
    soma = 2
    anterior = 1

    for i in range(n-3):
        soma += anterior
        anterior = soma - anterior
        
    return soma
# Exercício 9
def  contagem_regressiva(n):
    for i in range(n, -1, -1):
        print(i)
        
    print('FIM!')
# Exercício 10
def jogo_adivinhacao():
    num = random.randint(1, 100)
    
    tentativa = int(input('Insira um número de 1 a 100: '))
    
    while tentativa != num:
        
        if tentativa > 100 or tentativa < 1:
            print('\nNúmero inválido')
            
        elif num < tentativa:
            print(f'\nO número secreto é menor que {tentativa}')
            
        elif num > tentativa:
            print(f'\nO número secreto é maior que {tentativa}')
            
        tentativa = int(input('\nInsira um número de 1 a 100: '))
        
    print(f'\nParabéns! O número secreto é {tentativa}!')
     