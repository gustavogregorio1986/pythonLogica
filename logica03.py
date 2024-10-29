nome = input("Digite o nome: ")
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

calculo = (nota1 + nota2)/2

if calculo >= 7.0:
    print(f"{nome} é aprovado!")
elif calculo < 7 or calculo > 3:
    print(f"{nome} é recuperação!")
else:
    print(f"{nome} é reprovado!")