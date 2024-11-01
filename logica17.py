import pandas as pd

# Criando um DataFrame com notas de estudantes em diferentes disciplinas
dados_notas = {
    'Estudante': ['Lucas', 'Mariana', 'Pedro', 'Ana', 'Júlia'],
    'Matematica': [8.5, 7.0, 9.0, 6.5, 8.0],
    'Historia': [9.0, 6.5, 7.5, 8.0, 7.0],
    'Ciencias': [7.5, 8.0, 8.5, 7.0, 9.0]
}

# Convertendo o dicionário para um DataFrame
df_notas = pd.DataFrame(dados_notas)

print("DataFrame com Notas dos Estudantes:")
print(df_notas)

# Calculando a média de notas por disciplina
media_matematica = df_notas['Matematica'].mean()
media_historia = df_notas['Historia'].mean()
media_ciencias = df_notas['Ciencias'].mean()

# Adicionando as médias ao DataFrame
medias = {
    'Disciplina': ['Matematica', 'Historia', 'Ciencias'],
    'Media': [media_matematica, media_historia, media_ciencias]
}
df_medias = pd.DataFrame(medias)

print("\nMédia de Notas por Disciplina:")
print(df_medias)

# Calculando a média geral das notas
media_geral = df_notas[['Matematica', 'Historia', 'Ciencias']].mean().mean()
print("\nMédia geral das notas:", round(media_geral, 2))
