import pandas as pd

# Criando um DataFrame com dados fictícios de vendas mensais
dados_vendas = {
    'Mes': ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
    'Vendas': [2000, 2500, 3000, 4000, 3500, 3800, 4200, 4600, 4800, 5000, 5200, 6000]
}

# Convertendo para DataFrame
df = pd.DataFrame(dados_vendas)

# Encontrando o mês com o maior valor de vendas
melhor_mes = df[df['Vendas'] == df['Vendas'].max()]
print("Mês com o maior valor de vendas:")
print(melhor_mes)

# Calculando o crescimento percentual mês a mês
df['Crescimento_%'] = df['Vendas'].pct_change() * 100
print("\nDataFrame com crescimento percentual mês a mês:")
print(df[['Mes', 'Vendas', 'Crescimento_%']])

# Identificando os meses com crescimento acima da média
media_crescimento = df['Crescimento_%'].mean()
meses_crescimento_acima_media = df[df['Crescimento_%'] > media_crescimento]
print("\nMeses com crescimento acima da média:")
print(meses_crescimento_acima_media[['Mes', 'Vendas', 'Crescimento_%']])

# Calculando a média anual de vendas
media_vendas = df['Vendas'].mean()
print("\nMédia anual de vendas:", media_vendas)
