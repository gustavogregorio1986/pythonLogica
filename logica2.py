nome = input("Digite o nome: ")
salario = float(input("Diogite o salario: "))
empresa = input("Digite o nome da empresa: ")

calculo = 0.0

if salario > 3400: 
    calculo = salario * 0.3
elif salario > 5000:
    calculo = salario * 0.5
elif salario > 6000:
    calculo = salario * 0.5
elif salario > 6000:
    calculo = salario * 0.6
elif salario > 8000:
    calculo = salario * 0.8
else:
    calculo = 0

calcularTotal = calculo + salario

print(f"O nome é: {nome}")
print(f"O salario é: {salario}")
print(f"O empresa é: {empresa}")

print(f"O calculo Total é: {calcularTotal}")