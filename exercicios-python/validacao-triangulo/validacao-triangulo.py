while True:
    v1 = float(input('Digite o 1° valor: '))
    v2 = float(input('Digite o 2° valor: '))
    v3 = float(input('Digite o 3° valor: '))

    if v1 > 0 and v2 > 0 and v3 > 0:
        if v1 < v2 + v3 and v2 < v1 + v3 and v3 < v1 + v2 and v1 > abs(v2 - v3) and v2 > abs(v1 - v3) and v3 > abs(v1 - v2):
            if v1 > (v2 - v3) and v2 > (v1 - v3) and v3 > (v1 - v2):
                print('Os valores podem formar um triângulo.')
                if v1 == v2 == v3:
                    print('O triângulo formado é Equilátero.')
                elif v1 == v2 or v2 == v3 or v3 == v1:
                    print('O triângulo formado é Isósceles.')
                else:
                    print('O triângulo formado é Escaleno.')
                break
            else:
                print('Os valores não obedecem a condição de diferença do triângulo.')
        else:
            print('Os valores não obedecem a condição de soma do triângulo.')
    else:    
        print('Valores inválidos.')
