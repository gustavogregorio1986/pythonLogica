import pandas as pd

# Criando um DataFrame com horas trabalhadas por funcionários em diferentes projetos
dados_horas = {
    'Funcionário': ['Carlos', 'Mariana', 'João', 'Ana', 'Rafael'],
    'Projeto_A': [10, 12, 8, 15, 9],
    'Projeto_B': [5, 8, 12, 10, 7],
    'Projeto_C': [4, 6, 5, 7, 8]
}

# Convertendo o dicionário para um DataFrame
df_horas = pd.DataFrame(dados_horas)

print("DataFrame com Horas Trabalhadas por Funcionários:")
print(df_horas)

# Calculando a média de horas trabalhadas por funcionário
df_horas['Media_Horas'] = df_horas[['Projeto_A', 'Projeto_B', 'Projeto_C']].mean(axis=1)

print("\nDataFrame com Médias de Horas Trabalhadas por Funcionário:")
print(df_horas)

# Calculando a média geral de horas trabalhadas por projeto
media_geral_horas = df_horas[['Projeto_A', 'Projeto_B', 'Projeto_C']].mean()
print("\nMédia geral de horas trabalhadas por projeto:")
print(media_geral_horas.round(2))
