import math

def main():
    while True:
        print("----------- Entre com o intervalo A->B ----------")
        a = float(input("a="))
        b = float(input("b="))
        fa = func(a)
        fb = func(b)
        print("F(a) = {}".format(fa))
        print("F(b) = {}".format(fb))
        if (fa*fb <= 0):
            break
    if (fa*fb == 0):
        print("---------- Raiz encontrada {} ou {}".format(a,b))
    else:
        iterador = int(input("---------- Entre com o numero de iterações: "))
        i = 1
        raiz = 1
        while ((i != iterador) and ( raiz == 1)):
            i += 1
            c = (a + b)/2
            fa = func(a)
            fc = func(c)
            if ((fa*fc) < 0):
                b = c
            elif ((fa*fc) > 0):
                a = c
            elif ((fa*f) == 0):
                raiz = 0
            print("---------- Iteração {}".format(i))
            if (raiz == 0):
                print("---------- A raiz é {}".format(c))
            else:
                print("----------A raiz está entre {} e {}".format(a, b))
                print("---------- F(c) = {}".format(fc))

def func(x):
    fx = math.exp(x) - math.sin(x) - 2
    return fx





main()
