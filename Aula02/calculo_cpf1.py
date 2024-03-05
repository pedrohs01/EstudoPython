print("\nPrograma para verificar se o CPF digitado é válido\n")
 
cpf_usu = input("Digite o seu CPF: ")   # Variável que guarda o CPF do usuário
cpf_calc = ""                           # Variável que guarda o CPF que está calculando
peso10 = 10                             # Variável que serve para calcular o peso de 10 até 2
peso11 = 11
rs = 0                                  # Variável que guarda a soma das multiplicações entre os dígitos de CPF e os pesos
 
for i in range(0,9):                    # Para obter os 9 primeiros dígitos do CPF foi usado "for" com uma contagem de 0 até 9
    print(cpf_usu[i])                   # Exibe um dígito do CPF por vez
                                        # Adiciona a variável "cpf_calc" os nove primeiros dígitos do CPF e adiciona o primeiro dígito verificador adiante
    print(int(cpf_usu[i])*peso10)
    rs+=(int(cpf_usu[i])*peso10)        # Para calcular um dígito por vez com o peso, se converteu cada dígito em "int", depois, os resultados
    cpf_calc += cpf_usu[i]                                    #foram somados e armazenados na variável "rs"
    peso10-=1                           # Sempre que o loop "for" rodar, será subtraído o valor 1 da variável "peso10"
 
print(rs)                               # Exibição do resultado encontrado
resto = rs % 11                         # Variável que guarda o resto da divisão
 
if( resto < 2):
    print("Primerio Digito é 0")
    cpf_calc+="0"
else:
    print("Primeiro Digito é "+str(11-resto))  
    cpf_calc+=(11-resto)
 
resultado = 0
for i in range(0,10):
    resultado+=int(cpf_calc[i]*peso11)

resto = resultado % 11
if(resto < 2):
    cpf_calc+="0"
else:
    cpf_calc+=str(resto-11)   

#   Validar se o cpf do usuario e igual ao cpf calculado
if(cpf_usuario==cpf_calc):
    print("CPF É valido")
else:
    print("CPF invalido")      