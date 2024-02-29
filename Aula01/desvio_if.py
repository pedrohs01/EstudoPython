# pede um numero e verrifica se é par ou inpar
numero = input("digite um número: ")
# e necessario realizar a conversão de texto para
# número, pois a função input sempre retorna o valor
# em formato texto, então, utilizamos a função
# int para converte a variável numero em valor
# numerico inteiro e assim realizar os cálculos
# necessários
numero = int(numero)

if(numero % 2 == 0):
    print("o numero digitado e par")
else:
    print("o numero digitado e impar")    