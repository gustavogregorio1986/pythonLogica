import pandas as pd

# Criando um DataFrame
dados = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Diana'],
    'Idade': [23, 35, 30, 25],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Curitiba', 'Salvador']
}

df = pd.DataFrame(dados)

# Exibindo o DataFrame
print("DataFrame Original:")
print(df)

# Filtrando pessoas com mais de 25 anos
maiores_de_25 = df[df['Idade'] > 25]
print("\nPessoas com mais de 25 anos:")
print(maiores_de_25)

# Adicionando uma nova coluna
df['Salário'] = [3000, 4500, 5000, 3800]
print("\nDataFrame com nova coluna de Salário:")
print(df)

# Calculando a média de idade
media_idade = df['Idade'].mean()
print("\nMédia de idade:", media_idade)
