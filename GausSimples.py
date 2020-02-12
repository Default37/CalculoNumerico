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
    gausSimples(x, vetResp, tamI, tamJ)


def gausSimples(x, vetResp, tamI, tamJ):
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
    print(Resp)



main()