# Exercício 1
'''
n = int(input('Insira o valor de n (entre 1 e 20): '))

while n < 1 or n > 20:
    print('\nValor inválido. Insira um valor entre 1 e 20')

    n = int(input('\nInsira o valor de n (entre 1 e 20): '))

termos = [1]

adicao = 3

for i in range(1, n+2):
    termos.append(termos[i-1] + adicao)

    adicao += 2

for i in termos:
    print(f'{i}', end=' ')
'''
# Exercício 2
'''
n = int(input('Insira o valor de n (entre 0 e 15): '))

while n < 0 or n > 15:
    print('\nValor inválido. Insira um valor entre 0 e 15')

    n = int(input('Insira o valor de n (entre 0 e 15): '))

mult = 1

fatorial = [1, 1]

for i in range(2, n+1):

    fatorial.append(fatorial[i-1] * i)

print(fatorial[n])
'''
# Exercício 3

n = int(input('Insira o valor dos lados do quadrado (entre 1 e 20): '))

while n < 1 or n > 20:
    print('\nValor inválido. Insira um valor entre 1 e 20')

    n = int(input('Insira o valor dos lados do quadrado (entre 1 e 20): '))

for i in range(n):
    if i == 0 or i == n-1:
        print('*' * n)

    else:
        print('*', ' ' * (n-4), '*')
