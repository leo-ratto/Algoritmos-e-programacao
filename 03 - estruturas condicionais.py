# 01) Escreva um programa que determine se um dado número inteiro n é par ou ímpar.
'''
n = int(input("Digite um número inteiro: "))

if n % 2 == 0:
    print(f"O número {n} é par.")
else:
    print(f"O número {n} é ímpar.") 
'''
# 02) Faça um programa que receba dois números e mostre qual deles é o maior.
'''
num1 = float(input("Digite o primeiro número: "))

num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    print(f"O número {num1} é maior que {num2}.")
elif num2 > num1:
    print(f"O número {num2} é maior que {num1}.")
else:
    print("Os dois números são iguais.")
'''
# 03) Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20% do salário imprima: "Empréstimo não concedido", caso contrário imprima: "Empréstimo concedido".
'''
salario = float(input("Digite o salário do trabalhador: "))

prestacao = float(input("Digite o valor da prestação do empréstimo: "))

if prestacao > 0.2 * salario:
    print("Empréstimo não concedido.")
else:
    print("Empréstimo concedido.")
'''
# 04) Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando as seguintes fórmulas (onde h corresponde a altura):
# - Homens: (72.7 ∗ h) − 58
# - Mulheres: (62.1 ∗ h) − 44.7
'''
altura = float(input("Digite a altura da pessoa (em metros): "))

sexo = input("Digite o sexo da pessoa (M para masculino, F para feminino): ").upper()

if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58
    print(f"O peso ideal para um homem com altura {altura}m é: {peso_ideal:.2f} kg.")

elif sexo == 'F':
    peso_ideal = (62.1 * altura) - 44.7
    print(f"O peso ideal para uma mulher com altura {altura}m é: {peso_ideal:.2f} kg.")

else:
    print("Sexo inválido. Por favor, digite 'M' para masculino ou 'F' para feminino.")
'''
# 05) Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar. As condições para aposentadoria são:
# - Ter pelo menos 65 anos,
# - Ou ter trabalhado pelo menos 30 anos,
# - Ou ter pelo menos 60 anos e ter trabalhado pelo menos 25 anos.
'''
idade = int(input("Digite a idade do trabalhador: "))

tempo_servico = int(input("Digite o tempo de serviço do trabalhador (em anos): "))

if idade >= 65 or tempo_servico >= 30 or (idade >= 60 and tempo_servico >= 25):
    print("O trabalhador pode se aposentar.")

else:
    print("O trabalhador não pode se aposentar.")  
'''
# 06) Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estadopossui uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%).Faça um programa em que o usuário entre com o valor e o estado destino do produto e oprograma retorne o preço final do produto acrescido do imposto do estado em que ele serávendido. Se o estado digitado não for válido, mostrar uma mensagem de erro.
'''
valor_produto = float(input("Digite o valor do produto: "))

estado = input("Digite o estado destino do produto (MG, SP, RJ, MS): ").upper()

if estado == 'MG':
    imposto = 0.07

elif estado == 'SP':
    imposto = 0.12

elif estado == 'RJ':
    imposto = 0.15

elif estado == 'MS':
    imposto = 0.08

else:
    print("Estado inválido. Por favor, digite MG, SP, RJ ou MS.")
    imposto = 0

if imposto != 0:
    preco_final = valor_produto + (valor_produto * imposto)
    print(f"O preço final do produto no estado {estado} é: R${preco_final:.2f}")
'''
# 07) Faça um programa que leia a idade de uma pessoa e mostre a mensagem de maioridade ou não.
'''
idade = int(input("Digite a idade da pessoa: "))

if idade >= 18:
    print("A pessoa é maior de idade.")

else:
    print("A pessoa é menor de idade.")
'''
# 08) Escreva um programa que, dada a idade de um nadador, classifique-o em uma das seguintes categorias:
'''
idade = int(input("Digite a idade do nadador: "))

if idade < 5:
    print("Nadador muito jovem para competir.")

elif 5 <= idade <= 7:
    print("Categoria: Infantil A.")

elif 8 <= idade <= 10:
    print("Categoria: Infantil B.")

elif 11 <= idade <= 13:
    print("Categoria: Juvenil A.")

elif 14 <= idade <= 17:
    print("Categoria: Juvenil B.")

else:
    print("Categoria: Sênior.")
'''
# 09) Crie um algoritmo que leia o peso e a altura de uma pessoa e calcule o IMC (índice de massa corpórea) de acordo com a fórmula: IMC = peso / altura**2.
'''
peso = float(input("Digite o peso da pessoa (em kg): "))

altura = float(input("Digite a altura da pessoa (em metros): "))

imc = peso / altura**2

print(f"O IMC da pessoa é: {imc:.2f}")

if imc <= 19:
    print("Classificação: Muito magro.")
elif 20 <= imc <= 25:
    print("Classificação: Normal.")
elif 26 <= imc <= 30:
    print("Classificação: Sobrepeso.")
elif 31 <= imc <= 40:
    print("Classificação: Obeso.")
else:
    print("Classificação: Obesidade Grave.")
'''
# 10) Escrever um algoritmo que leia o nome e as três notas obtidas por um aluno durante o semestre. Calcular a sua média (aritmética), informar o nome e sua menção aprovado (média >= 7), Reprovado (média <= 5) e Recuperação (média entre 5.1 a 6.9).
'''
nome = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))

nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"A média do aluno {nome} é: {media:.2f}")

if media >= 7:
    print(f"O aluno {nome} foi aprovado.")

elif media <= 5:
    print(f"O aluno {nome} foi reprovado.")

else:
    print(f"O aluno {nome} ficou de recuperação.")
'''
# 11) Dados três valores X, Y e Z, verificar se eles podem ser os comprimentos dos lados de um triângulo e, caso positivo, verificar se é um triângulo equilátero, isósceles e escaleno. Se eles não formarem um triângulo, o programa deve imprimir uma mensagem adequada. Considere as seguintes propriedades:
# - O comprimento de cada lado em um triângulo é menor que a soma dos outros dois lados;
# - Equilátero: tem os comprimentos dos três lados iguais;
# - Isósceles: tem os comprimentos de dois lados iguais;
# - Escaleno: tem os comprimentos dos três lados diferentes.
'''
lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

if (lado1 < lado2 + lado3) and (lado2 < lado1 + lado3) and (lado3 < lado1 + lado2):
    if lado1 == lado2 == lado3:
        print("Os lados formam um triângulo equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Os lados formam um triângulo isósceles.")
    else:
        print("Os lados formam um triângulo escaleno.")
else:
    print("Os lados não formam um triângulo.")
'''
# 12) Escrever um programa que lê um valor em reais e calcule qual o menor número possível de notas de 100, 50, 10, 5 e 1 em que o valor lido pode ser decomposto. Escrever o valor lido e a relação de notas necessárias.
# Por exemplo: valor = R$ 238,00
# notas de 100: 2
# notas de 50: 0
# notas de 10: 3
# notas de 5: 1
# notas de 1: 3
'''
valor = int(input("Digite um valor em reais: "))

notas_100 = valor // 100
valor = valor % 100
notas_50 = valor // 50
valor = valor % 50
notas_10 = valor // 10
valor = valor % 10
notas_5 = valor // 5
valor = valor % 5
notas_1 = valor // 1

print(f"Valor lido: R$ {notas_100 * 100 + notas_50 * 50 + notas_10 * 10 + notas_5 * 5 + notas_1 * 1}")
print(f"Notas de 100: {notas_100}")
print(f"Notas de 50: {notas_50}")
print(f"Notas de 10: {notas_10}")
print(f"Notas de 5: {notas_5}")
print(f"Notas de 1: {notas_1}")
'''
# 13) Num determinado Estado, para transferências de veículos, o DETRAN cobra uma taxa ;de 1% para carros fabricados antes de 1990 e uma taxa de 1.5% para os fabricados de 1990 em diante, a taxa está incidindo sobre o valor de tabela do carro. Escreva um programa que leia o ano e o preço do carro e a seguir calcula e imprime imposto a ser pago
'''
ano = int(input("Digite o ano de fabricação do carro: "))

preco = float(input("Digite o preço do carro: "))

if ano < 1990:
    taxa = 0.01

elif ano >= 1990:
    taxa = 0.015

imposto = preco * taxa

print(f"O imposto a ser pago é: R$ {imposto:.2f}")
'''