login = [
    ('Pedro', 'sucesso'),
    ('Ana', 'falha'),
    ('Maria', 'sucesso'),
    ('Pedro', 'falha'),
]

for usuario, status_login in login:
    if status_login == 'sucesso':
        print('Usuários com o login bem-sucedido:\n', usuario)
    elif status_login == 'falha':
        print ('Usuários com o login mal-sucedido:\n', usuario)