'''
 _____            _
| ____|__ _ _   _(_)_ __   ___   _
|  _| / _` | | | | | '_ \ / _ \ (_)
| |__| (_| | |_| | | |_) |  __/  _
|_____\__, |\__,_|_| .__/ \___| (_)
         |_|       |_|

     _                     ____      _   _      _
    | | ___   __ _  ___   |  _ \    | \ | | ___| |_ ___
 _  | |/ _ \ / _` |/ _ \  | |_) |   |  \| |/ _ \ __/ _ \
| |_| | (_) | (_| | (_) | |  _ < _  | |\  |  __/ || (_) |
 \___/ \___/ \__,_|\___/  |_| \_(_) |_| \_|\___|\__\___/

__     ___       _      _              ____           _       _
\ \   / (_)_ __ (_) ___(_)_   _ ___   / ___|__ _ _ __| | ___ | |_ ___
 \ \ / /| | '_ \| |/ __| | | | / __| | |   / _` | '__| |/ _ \| __/ _ \
  \ V / | | | | | | (__| | |_| \__ \ | |__| (_| | |  | | (_) | || (_) |
   \_/  |_|_| |_|_|\___|_|\__,_|___/  \____\__,_|_|  |_|\___/ \__\___/


  ____       _ _ _                                __  __      _ _
 / ___|_   _(_) | |__   ___ _ __ _ __ ___   ___  |  \/  | ___| | | ___
| |  _| | | | | | '_ \ / _ \ '__| '_ ` _ \ / _ \ | |\/| |/ _ \ | |/ _ \
| |_| | |_| | | | | | |  __/ |  | | | | | |  __/ | |  | |  __/ | | (_) |
 \____|\__,_|_|_|_| |_|\___|_|  |_| |_| |_|\___| |_|  |_|\___|_|_|\___/


'''


#Dado um caractere pertencente ao alfabeto, retorna a coluna
#correspondente na matriz de adjacencia
def get_column(c):

    if c >= 'a' and c <= 'z':
        return 0
    elif c >= '0' and c <= '9':
        return 1
    elif c == '.':
        return 2
    elif c == '\'':
        return 3
    elif c == ',':
        return 4
    elif c == ':':
        return 5
    elif c == ')':
        return 6
    elif c == '=':
        return 7
    elif c == '*':
        return 8
    elif c == '[':
        return 9
    elif c == ']':
        return 10
    elif c == '{':
        return 11
    elif c == '}':
        return 12
    elif c == '<':
        return 13
    elif c == '>':
        return 14
    elif c == '(':
        return 15
    elif c == '+':
        return 16
    elif c == '-':
        return 17
    else:
        return -1

#Dado um estado do automato, onde o estado inicial eh 0,
#Retorna 1 caso o estado seja final, caso contrario retorna 0
def is_final(state):
    if state == 0:
        return 0
    elif state == 14:
        return 0
    else:
        return 1

#Dado o estado, retorna o seu token, que eh a string referente
#a sua identificacao, ou retorna "" (string vazia) caso o estado
#nao exista ou nao tenha um token definido
def get_token(state):
    if state == 2 or state == 3:
        return "Numeral positivo"
    elif state == 4:
        return "Ponto simples"
    elif state == 5:
        return "Ponto duplo"
    elif state == 6:
        return "Dois pontos"
    elif state == 7:
        return "Atribuicao"
    elif state == 8:
        return "Maior que"
    elif state == 9:
        return "Maior ou igual que"
    elif state == 10:
        return "Menor que"
    elif state == 11:
        return "Menor ou igual que"
    elif state == 12:
        return "Parenteses_esq"
    elif state == 15:
        return "Comentario_fecho"
    elif state == 17:
        return "Parenteses_dir"
    elif state == 18:
        return "Varios (Tratar aqui)"
    elif state == 19 or state == 20:
        return "Numeral negativo"
    elif state == 21 or state == 22:
        return "Numeral positivo"
    else:
        return ""


#   a-z, 0-9, . , ' , , , : , ) , = , * , [ , ] , { , } , < , > , ( ,  + , -

states = [
    [1 , 2  , 4 , 18, 18, 6, 17, 18, 18, 18, 18, 18, 18, 10, 8 , 12 , 21, 19], #Estado 0 states[0][j]
    [1 , 1  , -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #Estado 1
    [-1, 2  , 3 , -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #Estado 2
    [-1, 3  , -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #Estado 3
    [-1, -1 , 5 , -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #Estado 4
    [-1, -1 , -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #Estado 5
    [-1, -1 , -1 , -1, -1, -1, -1, 7, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #Estado 6
    [-1, -1 , -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #Estado 7
    [-1, -1 , -1, -1, -1, -1, -1, 9 , -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #Estado 8
    [-1, -1 , -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #Estado 9
    [-1, -1 , -1, -1, -1, -1, -1, 11, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #Estado 10
    [-1, -1 , -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #Estado 11
    [-1, -1 , -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #Estado 12
    [-1, -1 , -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #Estado 13
    [-1, -1 , -1, -1, -1, -1, 15, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #Estado 14
    [-1, -1 , -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #Estado 15
    [-1, -1 , -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #Estado 16
    [-1, -1 , -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #Estado 17
    [-1, -1 , -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #Estado 18
    [-1, 19 , 20, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #Estado 19
    [-1, 20 , -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #Estado 20
    [-1, 21 , 22, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #Estado 21
    [-1, 22 , -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #Estado 22
]
print("Analisador Lexico\nPara sair, digite \'exit()\'\n\n\n")
line = input("Digite sua entrada de dados: ")
while line != '' :
    if line == "exit()":
        break
    next = 0
    current = 0
    last_final = 0
    i = 0
    cm = 0
    for j in range(len(line)):
        c = line[j]

        column = get_column(c)
        #Se o simbolo lido pertencer ao alfabeto
        if column > -1:
            next = states[current][column]
            #Se o caractere lido leva a um proximo estado
            if next > -1:
                current = next
                #Se o proximo estado eh um estado final, confirmamos a leitura lida ate aqui
                if is_final(next):
                    last_final = current
                    curent = i
                    #Se chegou no final da linha
                    if j == len(line) - 1:
                        print("Token lido: " + get_token(last_final))
                        i = cm
                        current = 0
                        last_final = 0
                        next = 0
            #Se o caractere lido nao leva a um proximo estado
            else:
                #Se o caractere lido nao leva a um proximo estado e o automato esta no estado inicial
                #entao o char nao existe no alfabeto da linguagem, ou seja, erro lexico
                if current == 0:
                    print("ERRO")
                    cm = i
                    current = 0
                    last_final = 0
                    next = 0
                #Se o caractere nao leva a um proximo estado, mas tb o automato nao esta no estado
                #inicial, ainda pode ser aceito pela linguagem
                else:
                    i = cm
                    print("Token lido: " + get_token(last_final))
                    current = 0
                    next = 0
                    last_final = 0
        #Se o simbolo lido nao pertence ao alfabeto
        else:
            #Se o simbolo lido for espaco, nao ha erro lexico, apenas imprimimos o token lido
            #ate aqui, e resetamos o automato
            if c == ' ':
                print("Token lido: " + get_token(last_final))
                i = cm
                current = 0
                last_final = 0
                next = 0
            else:
                print("Erro lexico")


    line = input("Digite sua entrada de dados: ")
