def main():
    mat = []
    vetResp = []
    ordem = 0
    preenchimento = 0
    soma = 0
    matMult = []
    ordem = int(input("Digite a Ordem do Sistema:"))
    print("Entre com os termos da matriz:")
    for i in range(ordem):
        matAux = []
        for j in range(ordem):
            preenchimento = float(input("linha {} coluna {}: ".format(i, j)))
            matAux.append(preenchimento)
        mat.append(matAux)
    print("Entre com os termos do vetor resposta:")
    for i in range(ordem):
        preenchimento = float(input("linha {}: ".format(i)))
        vetResp.append(preenchimento)
    print("----------Matriz Original----------")
    for i in range(ordem):
        print(mat[i])
    print("----------Vetor Resposta Inicial----------")
    print(vetResp)
    print("----------Entre com o Chute----------")
    vetChute = []
    for i in range(ordem):
        preenchimento = float(input("chute {}: ".format(i)))
        vetChute.append(preenchimento)
    iterate = int(input("Entre com o Número de Iterações:"))
    resp = []
    for i in range(ordem):
        resp.append(0)
        matMult.append(0)
    for k in range(iterate):
        print("--------------------Iteração {}---------------------".format(k+1))
        for i in range(ordem):
            soma = 0
            for j in range(ordem):
                if (i != j):
                    soma = soma + mat[i][j] * vetChute[j]
            resp[i] = (vetResp[i] - soma) / mat[i][i]
        for i in range(ordem):
            matMult[i] = 0
            for j in range(ordem):
                matMult[i] += (mat[i][j] * resp[j])
        erro = 0
        for i in range(ordem):
            erro += ((vetResp[i] - matMult[i]) ** 2)
        erro1 = erro **0.5
        print("----------Vetor Resposta----------")
        print(resp)
        print("----------Erro----------")
        print(erro1)
        for i in range(ordem):
            vetChute[i] = resp[i]


main()