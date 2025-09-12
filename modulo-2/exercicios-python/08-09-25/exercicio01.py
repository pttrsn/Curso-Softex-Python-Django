#Análise de Dados de Cliente
clientes = [
    {'Nome': 'Ana', 'Idade':25, 'Cidade':'São Paulo'},
    {'Nome': 'Bruno', 'Idade':30, 'Cidade':'Rio de Janeiro'},
    {'Nome': 'Carlos', 'Idade':25, 'Cidade':'São Paulo'},
    {'Nome': 'Diana', 'Idade':30, 'Cidade':'Belo Horizonte'},
    {'Nome': 'Eduardo', 'Idade':40, 'Cidade':'Rio de Janeiro'}
]

for cliente in clientes:
    nome = cliente['Nome']
    idade = cliente['Idade']
    print(f'Nome: {nome}, Idade: {idade}')

soma_idades = 0
total_clientes = 0

for cliente in clientes:
    soma_idades += cliente["idade"]

total_clientes = len(clientes)
idade_media = soma_idades / total_clientes
print(f"\nIdade média dos clientes: {idade_media:.2f} anos")

clientes_por_cidade = {}

for cliente in clientes:
    cidade = cliente["cidade"]
    if cidade in clientes_por_cidade:
        clientes_por_cidade[cidade] += 1
    else:
        clientes_por_cidade[cidade] = 1

print("\n--- Clientes por Cidade ---")
print(clientes_por_cidade)