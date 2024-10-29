numero = int(input("Digite o numero: "))

for numero in range(1,50):
    if numero % 2 == 0:
        print(f'O numero par é: {numero}')
    else:
        print(f'O numero impar é: {numero}')