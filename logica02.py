numero = int(input("Digite o numero: "))

calculo = 0

contador = 1

for numero in range(1, 10): 
    contador += 1
    calculo = numero * contador
    print(f"{numero} X {contador} = {calculo}")

