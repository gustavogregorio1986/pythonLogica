import pandas as pd

# Criando um DataFrame com dados fictícios de horas trabalhadas por funcionários
dados_funcionarios = {
    'Funcionario': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo'],
    'Horas_Segunda': [8, 9, 7, 8, 10],
    'Horas_Terca': [8, 8, 8, 8, 9],
    'Horas_Quarta': [8, 10, 6, 8, 8],
    'Horas_Quinta': [7, 8, 8, 8, 10],
    'Horas_Sexta': [8, 9, 8, 8, 8]
}

# Convertendo para DataFrame
df = pd.DataFrame(dados_funcionarios)

# Calculando o total de horas trabalhadas por semana para cada funcionário
df['Total_Horas'] = df.iloc[:, 1:].sum(axis=1)
print("DataFrame com o total de horas trabalhadas por funcionário:")
print(df[['Funcionario', 'Total_Horas']])

# Definindo carga horária semanal (por exemplo, 40 horas)
carga_horaria = 40

# Calculando horas extras (considerando horas acima da carga horária)
df['Horas_Extras'] = df['Total_Horas'] - carga_horaria
df['Horas_Extras'] = df['Horas_Extras'].apply(lambda x: x if x > 0 else 0)
print("\nDataFrame com horas extras de cada funcionário:")
print(df[['Funcionario', 'Total_Horas', 'Horas_Extras']])

# Identificando funcionários que fizeram horas extras
funcionarios_com_horas_extras = df[df['Horas_Extras'] > 0]
print("\nFuncionários que fizeram horas extras:")
print(funcionarios_com_horas_extras[['Funcionario', 'Horas_Extras']])

# Calculando a média de horas trabalhadas na semana por todos os funcionários
media_horas = df['Total_Horas'].mean()
print("\nMédia de horas trabalhadas na semana:", media_horas)
