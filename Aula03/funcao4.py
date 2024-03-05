def montar_tabuada(numero=0):
    print("O programa pede um numero para fazer a tabuada")
    arq = open("tabuada.txt","a")
    for i in range(1,11):
        arq.write(str(numero) + " x " + str(i) + " = " + str(numero*i)+"\n" )
    arq.close()

n = input("Digite um numero: ")
montar_tabuada(int(n))        
    

 

