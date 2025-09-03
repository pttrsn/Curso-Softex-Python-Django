estoque_pri = set([
    ('Camiseta', 101),
    ('Calça', 102),
    ('Boné', 103),
    ('Tênis', 104)
])

estoque_vir = set([
    ('Boné', 103),
    ('Camisa Polo', 105),
    ('Calça', 102),
    ('Chinelo', 106)
])

#Ou criar uma nova variável para set(), exemplo:
'''estoque_pri: [(...)]

set_pri = set(estoque_pri)
'''

disponivel_privir = estoque_pri.intersection(estoque_vir)
disponivel_pri = estoque_pri.difference(estoque_vir)
disponivel_vir = estoque_vir.difference(estoque_pri)

print('Produtos disponíveis na loja e no site:\n', disponivel_privir)
print('Produtos disponíveis apenas na loja:\n', disponivel_pri)
print('Produtos disponíveis apenas no site:\n', disponivel_privir)