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
 
    print("vetResp:")
    print(vetResp)
    print("vetX:")
    print(x)
    x, vetResp = gaussSimples(x, vetResp, tamI, tamJ)
    print("Gauss Simples:")
    print(x)
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
    print("Retro Solucao: ")
    print(Resp)

def  gaussSimples(x, vetResp, tamI, tamJ):
    m = 0
    for j in range(tamI):
        for i in range(tamI):
            if (i>j):
                m = -(x[i][j]/x[j][j])
                print("m= ", m)
                for k in range(tamI):
                    x[i][k] = x[i][k] + (m*x[j][k])
                vetResp[i] = vetResp[i] + m*vetResp[j]
    return x, vetResp
                    
        

main()