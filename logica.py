num1 = int(input('Digite o num 1: '))
num2 = int(input('Digite o num 2: '))

numero1 = int(input('Digite o numero 1: '))
numero2 = int(input('Digite o numero 2: '))

n1 = int(input('Digite o n 1: '))
n2 = int(input('Digite o n 2: '))

valor1 = int(input('Digite o valor 1: '))
valor2 = int(input('Digite o valor 2: '))

soma = num1 + num2

print(f"A soma é ", soma)

subtracao = numero1 - numero2

print(f"A subtração é ", subtracao)

multiplicacao = n1 * n2

print(f"A multiplicação é ", multiplicacao)

if valor2 == 0:
    print("Erro: Não pode dividir por zero.")
else:
    # Coloque aqui o código para executar se valor2 não for zero
    resultado = valor1 / valor2
    print("O resultado é:", resultado)

