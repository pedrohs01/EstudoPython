n1 = input("digite a primeira nota do aluno: ")
n2 = input("digite a segunda nota do aluno: ")
n3 = input("digite a terceira nota do aluno: ")
n4 = input("digite a quarta nota do aluno: ")
rs = ( int(n1)+int(n2)+int(n3)+int(n4) ) / 4
# se o aluno tiver uma media acima ou igual a 7,
# então estará aprovado. senão se a media
#  for abaixo ou igual a 4, então eatará reprovado
# caso o contrario, eatará em recuperação
print("A sua media e "+str(rs)+", então vc esta: ")

if( rs >= 7):
    print("Aprovado")
elif( rs <= 4 ):
    print("Reprovado")
else:
    print("Recuperação")     
   

