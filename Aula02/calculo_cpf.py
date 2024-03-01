print("Programa que verifica se o CPF é válido")
# Variável que gurda o cpf digitado pelo usuário.
cpf_usuario = input("Digite o seu cpf: ")
# Essa variável foi criada para calcular o pesso de 10 até 2.
peso10 = 10
# A variável resultado guarda a soma das multiplicações entre os digitos do cpf e os pesos.
resultado = 0
# Para obter os 9 primeiros digitos do cpf foi nescessário usar uma estrutura for com uma contagem de 0 até 9.
for i in range(0,9):
    # exibindo um digito do cpf por vez em tela.
    print(cpf_usuario[i])
    print(int(cpf_usuario[i])*peso10)
    # Para calcular um digito por vez com peso foi necessário converter cada dogito em número inteiro
    # depois, somamos os resultado obtidos armazenando na variável resultado.
    resultado+=int(cpf_usuario[i])*peso10
    # Todas as vezes que o laço for rodar, será subtraido o valor 1 da variavel peso10
    peso10-=1
# Exibindo o resultado encontrado 
print(resultado)    
# A variavel resto, guarda o resto da divisão
resto = resultado % 11
# Se o resto da divisão for menor que 2, entao o primeiro digito sera 0(zero); Caso contrario o
# devemos subtrair 11 pelo valor encontrado
if( resto < 2):
    print("Primerio Digito é 0")
else:
    print("Primeiro Digito é "+str(11-resto))    