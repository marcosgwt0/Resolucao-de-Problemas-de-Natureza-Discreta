with open('teste1.txt','r') as l:
    listaArquivo = []
    for line in l:
        listaArquivo.append(line.strip())
x = int(listaArquivo.pop(0))
n = 3
listas =[listaArquivo[i:i + n] for i in range(0, len(listaArquivo), n)]
for i in listas:
    matriz = []
    conjunto1 = i[1]
    conjunto2 = i[2]
    conjunto1 = conjunto1.split(",")
    conjunto2 = conjunto2.split(",")
    if i[0] == "U":
        conjuntofinal = list(conjunto1) 
        conjuntofinal.extend(x for x in conjunto2 if x not in conjuntofinal)
        print("União: Conjunto 1 = {}, Conjunto 2 = {}, Resultado = {}".format(conjunto1, conjunto2, conjuntofinal))
    elif i[0] == "I":
        conjuntofinal = []
        conjuntofinal.extend(x for x in conjunto2 if x in conjunto1 and x in conjunto2)
        print("Interseção: Conjunto 1 = {}, Conjunto 2 = {}, Resultado = {}".format(conjunto1, conjunto2, conjuntofinal))
    elif i[0] == "D":
        conjuntofinal = []
        conjuntofinal.extend(x for x in conjunto1 if x in conjunto1 and x not in conjunto2)
        print("Diferença: Conjunto 1 = {}, Conjunto 2 = {}, Resultado = {}".format(conjunto1, conjunto2, conjuntofinal))
    elif i[0] == "C":
        cartesiano = [(x,y) for x in conjunto1 for y in conjunto2]
        print("Produto Cartesiano: Conjunto 1 = {}, Conjunto 2 = {}, Resultado = {}".format(conjunto1, conjunto2, cartesiano))