import pandas as pd

# Criando um DataFrame com nomes de alunos e suas notas
dados_alunos = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo'],
    'Nota1': [7.5, 8.0, 6.5, 9.0, 5.5],
    'Nota2': [8.5, 7.0, 9.0, 8.0, 6.0]
}

# Convertendo o dicionário para um DataFrame
df_alunos = pd.DataFrame(dados_alunos)

# Calculando a média de cada aluno
df_alunos['Media'] = df_alunos[['Nota1', 'Nota2']].mean(axis=1)

print("DataFrame com Alunos e suas Médias:")
print(df_alunos)

# Calculando a média geral da turma
media_geral = df_alunos['Media'].mean()
print("\nMédia geral da turma:", media_geral)
