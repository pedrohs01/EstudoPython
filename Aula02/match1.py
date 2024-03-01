print("Este programa analisa os valores digitado de 0 a 6 e diz o dia da semana")
digito = input("Entre com um número de 0 a 6\n")

match digito:
    case '0':
        print("domingo")        
match digito:
    case '1':
        print("segunda-feira")   
match digito:
    case '2':
        print("terceira-feira")             
match digito:
    case '3':
        print("quarta-feira")
match digito:
    case '4':
        print("quinta-feira")        
match digito:
    case '5':
        print("sexta-feira")      
match digito:
    case '6':
        print("sabado")     
    case _:
        print("Valor incorreto. Tente novamente")                     