import pandas as pd

# Criando um DataFrame com nomes de funcionários, departamentos e salários
dados_funcionarios = {
    'Nome': ['Alice', 'Bruno', 'Carlos', 'Diana', 'Eduardo', 'Fernanda', 'Gabriel'],
    'Departamento': ['Financeiro', 'TI', 'Marketing', 'Financeiro', 'TI', 'Marketing', 'Financeiro'],
    'Salario': [5000, 6000, 4500, 5500, 6200, 4800, 7000]
}

# Convertendo o dicionário para um DataFrame
df_funcionarios = pd.DataFrame(dados_funcionarios)

print("DataFrame de Funcionários:")
print(df_funcionarios)

# Calculando a média de salários por departamento
media_salarios_departamento = df_funcionarios.groupby('Departamento')['Salario'].mean()

print("\nMédia de Salários por Departamento:")
print(media_salarios_departamento)
