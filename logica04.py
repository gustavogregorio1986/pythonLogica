import pandas as pd

# Criando um DataFrame com dados fictícios de vendas
dados_vendas = {
    'Produto': ['Notebook', 'Celular', 'Tablet', 'Notebook', 'Celular', 'Tablet'],
    'Quantidade': [2, 5, 3, 4, 6, 2],
    'Preço': [3000, 1500, 1200, 3000, 1500, 1200],
    'Vendedor': ['João', 'Maria', 'João', 'Maria', 'Carlos', 'João']
}

df = pd.DataFrame(dados_vendas)

# Calculando o valor total de cada venda
df['Valor Total'] = df['Quantidade'] * df['Preço']
print("DataFrame com coluna de Valor Total:")
print(df)

# Agrupando por Produto e calculando o total de vendas por produto
vendas_por_produto = df.groupby('Produto')['Valor Total'].sum()
print("\nTotal de Vendas por Produto:")
print(vendas_por_produto)

# Agrupando por Vendedor e calculando o total de vendas por vendedor
vendas_por_vendedor = df.groupby('Vendedor')['Valor Total'].sum()
print("\nTotal de Vendas por Vendedor:")
print(vendas_por_vendedor)

# Encontrando o produto mais vendido em quantidade
produto_mais_vendido = df.groupby('Produto')['Quantidade'].sum().idxmax()
print("\nProduto mais vendido em quantidade:", produto_mais_vendido)
