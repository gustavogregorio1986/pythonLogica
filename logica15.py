import pandas as pd

# Criando um DataFrame com nomes, idades e alturas
dados_pessoas = {
    'Nome': ['Alice', 'Bruno', 'Carla', 'Daniel', 'Eva'],
    'Idade': [24, 30, 22, 35, 28],
    'Altura': [1.65, 1.80, 1.55, 1.75, 1.60]  # Altura em metros
}

# Convertendo o dicionário para um DataFrame
df_pessoas = pd.DataFrame(dados_pessoas)

print("DataFrame com Idades e Alturas:")
print(df_pessoas)

# Calculando a média de idade
media_idade = df_pessoas['Idade'].mean()

# Calculando a média de altura
media_altura = df_pessoas['Altura'].mean()

print("\nMédia de Idade:", round(media_idade, 2))
print("Média de Altura:", round(media_altura, 2))
