import pandas as pd

# Criando um DataFrame com notas de alunos em diferentes provas
dados_notas = {
    'Aluno': ['Thiago', 'Marcos', 'Lúcia', 'Fernanda', 'Juliano'],
    'Prova1': [85, 90, 78, 92, 88],
    'Prova2': [82, 88, 85, 80, 91],
    'Prova3': [89, 92, 76, 84, 87]
}

# Convertendo o dicionário para um DataFrame
df_notas = pd.DataFrame(dados_notas)

print("DataFrame com Notas dos Alunos:")
print(df_notas)

# Calculando a média de notas por prova
media_prova1 = df_notas['Prova1'].mean()
media_prova2 = df_notas['Prova2'].mean()
media_prova3 = df_notas['Prova3'].mean()

# Adicionando as médias ao DataFrame
medias = {
    'Prova': ['Prova 1', 'Prova 2', 'Prova 3'],
    'Média': [media_prova1, media_prova2, media_prova3]
}
df_medias = pd.DataFrame(medias)

print("\nMédia de Notas por Prova:")
print(df_medias)

# Calculando a média geral das notas dos alunos
media_geral = df_notas[['Prova1', 'Prova2', 'Prova3']].mean().mean()
print("\nMédia geral das notas dos alunos:", round(media_geral, 2))
