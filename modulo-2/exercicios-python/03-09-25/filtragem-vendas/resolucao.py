vendas = [
    ('Teclado', 70, 2), 
    ('Mouse', 25.99, 4), 
    ('Webcam', 90, 1), 
    ('Fone', 50, 1)
]

filtro_vendas = []
produtos_unicos = set()

for produto, valor, quantidade in vendas:
    valor_total = valor * quantidade
    if valor_total >= 100:
        filtro_vendas.append((produto, valor, quantidade))

    produtos_unicos.add(produto)

print('Vendas filtradas:\n', filtro_vendas)
print('Produtos únicos:\n', produtos_unicos)
