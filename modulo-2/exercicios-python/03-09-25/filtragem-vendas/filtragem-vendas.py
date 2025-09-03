vendas = [('Teclado', 70, 2), ('Mouse', 25.99, 4), ('Webcam', 90, 1), ('Fone', 50, 1)]

for produto, valor, quantidade in vendas:
    filtro_vendas = [(valor * quantidade) >= 100]
    produtos = {produto}
    
print('Vendas filtradas:\n', [(vendas == filtro_vendas)])
print('Produtos únicos:\n', produtos)
