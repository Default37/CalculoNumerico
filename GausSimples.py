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
      val = int(input(""))
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
  flag = 0
  for i in range(tamI-1, -1, -1):
    if (i == tamI-1):
      xResp = vetResp[i] / x[i][i]
      Resp.append(xResp)
    elif (i == tamI-2):
      xResp = (vetResp[i] - (x[i][i+1])*Resp[flag-1]) / x[i][i]
      Resp.append(xResp)
    elif (i == tamI-3):
      xResp = ((vetResp[i] - (x[i][i+1])*Resp[flag-1]) - (x[i][i+2]*Resp[flag-2]))/ x[i][i]
      Resp.append(xResp)
    flag += 1

  print(Resp)



main()