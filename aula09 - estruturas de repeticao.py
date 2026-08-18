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
'''
n = int(input('Insira o valor dos lados do quadrado (entre 1 e 20): '))

while n < 1 or n > 20:
    print('\nValor inválido. Insira um valor entre 1 e 20')

    n = int(input('\nInsira o valor dos lados do quadrado (entre 1 e 20): '))

for i in range(n):
    
    for r in range(n):
        
        if i == 0 or i == (n-1):
            if r == (n-1):
                print('*')
                
            else:
                print('*', end='')
            
        else:
            
            if r == 0:
                print('*', end='')
                
            elif r == (n-1):
                print('*')
                
            else:
                print(' ', end='')
'''          
# Exercício 4
'''
n = int(input('Insira o valor da altura do triângulo: '))

for i in range(1, n+1):
    print('*' * i)
'''
# Exercício 5
'''
n = int(input('Insira o valor de n: '))

fatorial = 1

soma = 1

for i in range(1, n+1):
    
    fatorial *= i
    
    soma += (1/fatorial)
    
print(f'O valor de E é {soma}')
'''
# Exercício 6
'''
x = int(input('Insira o valor de x: '))

soma = x**25

inverso = 24

for i in range(2, 26):
    
    if i % 2 != 0:   
        soma += (x**inverso)/(i)
        
    else:
        soma -= (x**inverso)/(i)
        
    inverso -= 1       
            
print(f'O valor da somatória é {soma}')
'''
# Exercício 7
'''
soma = 0

for i in range(1, 51):
    
    soma += ((2 * i) - 1) / i

print(f'Soma: {soma}')
'''