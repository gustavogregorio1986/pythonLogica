import pandas as pd

# Criando um DataFrame com nomes das equipes e seus pontos em quatro partidas
dados_equipes = {
    'Equipe': ['Time A', 'Time B', 'Time C', 'Time D'],
    'Partida1': [3, 1, 0, 2],
    'Partida2': [1, 3, 2, 0],
    'Partida3': [0, 2, 1, 3],
    'Partida4': [2, 1, 3, 1]
}

# Convertendo o dicionário para um DataFrame
df_equipes = pd.DataFrame(dados_equipes)

print("DataFrame com Resultados das Equipes:")
print(df_equipes)

# Calculando a média de pontos de cada equipe
df_equipes['Media_Pontos'] = df_equipes[['Partida1', 'Partida2', 'Partida3', 'Partida4']].mean(axis=1)

print("\nDataFrame com Médias de Pontos:")
print(df_equipes)

# Calculando a média geral dos pontos
media_geral_pontos = df_equipes['Media_Pontos'].mean()
print("\nMédia geral dos pontos:", round(media_geral_pontos, 2))
