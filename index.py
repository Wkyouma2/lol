resultado = set()

with open('valores_tde.txt', "r") as txt:
    
    arq = int(txt.readline())

    for i in range(arq):
        operacao = txt.readline().strip()

        conjunto1 = set(txt.readline().strip().split(","))
        conjunto2 = set(txt.readline().strip().split(","))

        if operacao == "U":
            resultado = conjunto1 | conjunto2 
            print(f'Uniao: conjunto {i + 1} {conjunto1}, conjunto {i + 2} {conjunto2}. Resultado: {resultado}')
        elif operacao == "D":
                resultado = conjunto1-conjunto2
                print(f'Diferenca: conjunto {i + 1} {conjunto1}, conjunto {i + 2} {conjunto2}. Resultado: {resultado}')
        elif operacao == "I":
            resultado = conjunto1 & conjunto2
            print(f'Intersecao: conjunto {i + 1} {conjunto1}, conjunto {i + 2} {conjunto2}. Resultado: {resultado}')
       
