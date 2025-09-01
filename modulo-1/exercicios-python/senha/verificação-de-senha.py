t = 0 #Variável de tentativas

print('Verificação de Senha'.center(100,'-')) #Título

while t < 3:
    senha = input('Digite uma senha para verificação: ') #Comando

    maiuscula = any(c.isupper() for c in senha) #Variáveis
    minuscula = any(c.islower() for c in senha)
    numero = any(c.isdigit() for c in senha)
    caracter = any(not c.isalnum() for c in senha)
    tamanho = len(senha) == 8

    if maiuscula and minuscula and numero and caracter and tamanho: #Condição de conclusão
        print('A senha é válida.'.center(100))
        break

    if maiuscula == False: #Condições de erro
        print('A senha deve conter ao menos uma letra maiúscula.')
    if minuscula == False:
        print('A senha deve conter ao menos uma letra minúscula.')
    if numero == False:
        print('A senha deve conter ao menos um número.')
    if caracter == False:
        print('A senha deve conter ao menos um caracter especial.')
    if tamanho == False:
        print('A senha deve conter 8 elementos.')

    t += 1 #Uma tentativa por erro

else: #Se o número de tentativas for excedido, ELSE torna-se verdadeiro
    print('O número máximo de tentativas foi atingido.'.center(100))
