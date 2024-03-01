print("Este programa analisa final de placas de carros e fala qual placa e proibida usar no dia")
digito = input("Entre com um número de 0 a 9      ")

match digito:
    case '1' | '2':
        print("Placas com final 1 e 2 não podem rodar na segunda-feira")
match digito:
    case '3' | '4':
        print("Placas com final 3 e 4 não podem rodar na terça-feira")   
match digito:
    case '5' | '6':
        print("Placas com final 5 e 6 não podem rodar na quarta-feira")     
match digito:
    case '7' | '8':
        print("Placas com final 7 e 8 não podem rodar na quinta-feira")       
match digito:
    case '9' | '0':
        print("Placas com final 9 e 0 não podem rodar na sexta-feira")                  