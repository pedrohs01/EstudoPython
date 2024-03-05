def montar_tabuada(numero=0):
    print("O programa pede um numero para fazer a tabuada")
    arq = open("tabuada.txt","a")
    for i in range(1,11):
        arq.write(numero + " x " + i + " = " + (numero*i)+"\n" )
    