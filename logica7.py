import pandas as pd

# Criando uma matriz (DataFrame) com nomes e e-mails
dados_contatos = {
    'Nome': ['Alice', 'Bruno', 'Carlos', 'Diana', 'Eduardo'],
    'Email': [
        'alice@example.com',
        'bruno@example.com',
        'carlos@example.com',
        'diana@example.com',
        'eduardo@example.com'
    ]
}

# Convertendo o dicionário para um DataFrame
df_contatos = pd.DataFrame(dados_contatos)

print("DataFrame com Nomes e E-mails:")
print(df_contatos)

# Exibindo somente os e-mails
emails = df_contatos['Email']
print("\nLista de E-mails:")
print(emails)

# Filtrando contatos com nomes que começam com a letra 'A'
contatos_com_a = df_contatos[df_contatos['Nome'].str.startswith('A')]
print("\nContatos com nomes que começam com 'A':")
print(contatos_com_a)
