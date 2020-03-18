def main():
    x = []
    val = 0
    tam = 0
    vetResp = []
    print("A matriz é quadrada, porém deve ser inicializada com o valor de j+1")
    tamI = int(input("Tamanho de i: "))
    tamJ = int(input("Tamanho de j: "))

    for i in range(tamI):
        y = []
        for j in range(tamJ):
            val = float(input(""))
            y.append(val)
        vetResp.append(y[j])
        del(y[j])
        x.append(y)

    print("---------Inicio---------")
    print("Matriz:")
    for i in range(tamI):
        print(x[i])
    print("Vetor Resposta:")
    print(vetResp)
    x, vetResp = gaussSimples(x, vetResp, tamI, tamJ)
    print("----------Gauss Simples-----------")
    print("Matriz:")
    for i in range(tamI):
        print(x[i])
    print("Vetor Resposta:")
    print(vetResp)
    retroSolucao(x, vetResp, tamI, tamJ)

def retroSolucao(x, vetResp, tamI, tamJ):
    Resp = []
    xResp = 0
    for i in range(len(vetResp)):
        Resp.append(0)
    for i in range(tamI-1, -1, -1):
        flag = 0
        if (i == tamI-1):
            xResp = (vetResp[i])/x[i][i]
            Resp[i] = xResp
        else:
            for j in range(i+1, tamI):
                flag = flag + x[i][j] * Resp[j]
            xResp = (vetResp[i] - flag)/x[i][i]
            Resp[i] = xResp
    print("-------------Retro Solucao-------------")
    print(Resp) 

def  gaussSimples(x, vetResp, tamI, tamJ):
    m = 0
    flag = 0
    for j in range(tamI):
        for i in range(tamI):
            if (i>j):
                x, vetResp = pivotParcial(x, vetResp, tamI, tamJ, flag)
                m = -(x[i][j]/x[j][j])
                print("m = ", m)
                for k in range(tamI):
                    x[i][k] = x[i][k] + (m*x[j][k])
                vetResp[i] = vetResp[i] + m*vetResp[j]
                flag += 1
    return x, vetResp

def pivotParcial(x, vetResp, tamI, tamJ, flag):
    aux = []
    aux2 = []
    indice = 0
    auxResp = 0
    for i in range(tamI):
        aux.append(x[i][0])
    for i in range(len(aux)):
        if (abs(aux[i]) > abs(aux[indice])):
            indice = i
    aux2 = x[indice]
    x[indice] = x[flag]
    x[flag] = aux2
    auxResp = vetResp[flag]
    vetResp[flag] = vetResp[indice]
    vetResp[indice] = auxResp
    print("-----------Pivoteamento Parcial---------------")
    print("Matriz:")
    for i in range(tamI):
        print(x[i])
    print("Vetor Resposta:")
    print(vetResp)
    return x, vetResp
    

main()