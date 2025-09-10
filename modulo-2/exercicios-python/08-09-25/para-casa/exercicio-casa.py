frutas = {
    'Maça': 2.70, 'Pêssego': 4.90, 'Banana': 5
}

print(frutas)
print(frutas['Pêssego'])
for frutas, preco in frutas.items():
    print(f'Fruta: {frutas}, Preço: R${preco:.2f}')
print('-'*30)

dicionario = {}

dicionario['Fruta'] = 'Maça'
dicionario['Carro'] = 'Mustang'
dicionario['Cor'] = 'Vermelho'

print(dicionario)
print('-'*30)

paises = {
    'Brasil': 'Brasília',
    'Argentina': 'Buenos Aires',
    'Portugal': 'Lisboa'
}

pais = input('Digite o nome de um país: ')
erro = pais != 'Brasil', 'Argentina', 'Portugal'
if pais == 'Brasil':
    print('A capital do', pais, 'é', paises['Brasil'],'.')
elif pais == 'Argentina':
    print('A capital da', pais, 'é', paises['Argentina'],'.')
elif pais == 'Portugal':
    print('A capital de', pais, 'é', paises['Portugal'],'.')
elif pais.get(erro, 'País desconhecido'):
    print('País desconhecido')
    

