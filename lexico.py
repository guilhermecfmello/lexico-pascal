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


from symbols import SymbolsTab

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
    elif state > 24 or state < 0:
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
    elif state == 23:
        return "Mais"
    elif state == 24:
        return "Menos"
    else:
        return ""

#Quando o automato termina no estado 18, deve-se saber qual eh o simbolo
#lido e entao imprimir seu Token
def get_special_token(c):
    if c == ';':
        return "Ponto e virgula"
    elif c == ',':
        return "Virgula"
    elif c == '=':
        return "Igual"
    elif c == '*':
        return "Asterisco"
    elif c == '[':
        return "Colchete_esq"
    elif c == ']':
        return "Colchete_dir"
    elif c == '{':
        return "Chave_esq"
    elif c == '}':
        return "Chave_dir"

#Se o caractere passado estiver em [a,b], retorna 1
#Retorna 0, caso contrario
def is_char(c):
    if c >= 'a' and c <= 'z':
        return 1
    else:
        return 0

#Trata identificadores
def identifiers(dic, string, str_final):
    cond_dic = dic.instalar_id(id)
    #Se for uma palavra-chave
    if cond_dic > 1:
        str_final = str_final + id.upper()
        # print("7:Token lido: " + id.upper())
    elif cond_dic == 1:
        # print("8:Token lido: Identificador("+ id.upper() + ") encontrado")
        str_final = str_final + "Identificador(" + id.upper() + ") encontrado"
    elif cond_dic == 0:
        # print("9:Token lido: Identificador("+ id.upper() + ") armazenado")
        str_final = str_final + "Identificador(" + id.upper() + ") armazenado"

    str_final = str_final + "\n"
    return str_final
#   a-z, 0-9, . , ' , , , : , ) , = , * , [ , ] , { , } , < , > , ( ,  + , -

states = [
    [1 , 2  , 4 , 18, 18, 6, 17, 18, 18, 18, 18, 18, 18, 10, 8 , 12 , 23, 24], #Estado 0
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
    [-1, 21 , -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #Estado 23
    [-1, 19 , -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]  #Estado 24
]
print("Analisador Lexico\nPara sair, digite \'exit()\'\n\n\n")
line = input("Digite sua entrada de dados: ")

#Inicializando tabela de palavras-chave/identificadores
dic = SymbolsTab()
while line != '' :
    if line == "exit()":
        break
    str_final = ""
    cond_error = 0
    next = 0
    current = 0
    last_final = 0
    cm = 0
    j = 0
    start_char = 0
    end_char = 0
    while(j < len(line)):
    #for j in range(len(line)):
        c = line[j]
        #Verifica se comecou a reconhecer uma palavra-chave/identificador
        if is_char(c) and current == 0:
            start_char = j


        j = j + 1
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
                    cm = j
                    #Se chegou no final da linha
                    if j == len(line):
                        # print("TESTE STR_FINAL: " + str_final)

                        #Se nao for um dos caracteres especiais, podera imprimir o token
                        #do ultimo estado final, caso contrario, deve-se verificar qual
                        #eh o token lido
                        if last_final == 1:
                            #Se terminar no estado 1 do automato, devera haver uma verificacao
                            #na tabela de simbolos
                            id = line[start_char:j]
                            str_final = identifiers(dic, id, str_final)
                            current = 0
                            last_final = 0
                            next = 0
                            cm = j
                        else:
                            if last_final != 18:
                                # print("1:Token lido: " + get_token(last_final)
                                str_final = str_final + get_token(last_final) + "\n"
                                # print(str_final)
                                j = cm
                                current = 0
                                last_final = 0
                                next = 0
                            else:
                                # print("4:Token lido: " + get_special_token(c))
                                str_final = str_final + get_special_token(c) + "\n"

            #Se o caractere lido nao leva a um proximo estado
            else:
                #Se o caractere lido nao leva a um proximo estado e o automato esta no estado inicial
                #entao o char nao existe no alfabeto da linguagem, ou seja, erro lexico
                if current == 0:
                    # print("ERRO")
                    cm = j
                    current = 0
                    last_final = 0
                    next = 0
                    if not cond_error:
                        indexError = j
                    cond_error = 1
                #Se o caractere nao leva a um proximo estado, mas tb o automato nao esta no estado
                #inicial, ainda pode ser aceito pela linguagem
                else:
                    # j = cm
                    #Se nao for um dos caracteres especiais, podera imprimir o token
                    #do ultimo estado final, caso contrario, deve-se verificar qual
                    #eh o token lido

                    if last_final == 1:
                        j = j - 1
                        id = line[start_char:j]
                        str_final = identifiers(dic, id, str_final)
                        current = 0
                        last_final = 0
                        next = 0
                        cm = j
                    else:
                        if last_final != 18:
                            # print("2:Token lido: " + get_token(last_final))
                            str_final = str_final + get_token(last_final) + "\n"
                            j = cm
                            current = 0
                            next = 0
                            last_final = 0
                        else:
                            # print("C: " + c + "line[j]: " + line[j])
                            # print("5:Token lido: " + get_special_token(line[j-2]) + " | J: " + str(j))
                            str_final = str_final + get_special_token(line[j-2]) + "\n"
                            j = cm
                            current = 0
                            next = 0
                            last_final = 0


        #Se o simbolo lido nao pertence ao alfabeto
        else:
            #Se o simbolo lido for espaco, nao ha erro lexico, apenas imprimimos o token lido
            #ate aqui, e resetamos o automato
            if c == ' ' and current != 0:
                #Se nao for um dos caracteres especiais, podera imprimir o token
                #do ultimo estado final, caso contrario, deve-se verificar qual
                #eh o token lido
                if last_final == 1:
                    id = line[start_char:j - 1]
                    str_final = identifiers(dic, id, str_final)
                    current = 0
                    last_final = 0
                    next = 0
                    cm = j
                else:
                    if last_final != 18:
                        # print("3:Token lido: " + get_token(last_final))
                        str_final = str_final + get_token(last_final) + "\n"
                        j = cm
                        current = 0
                        last_final = 0
                        next = 0
                    else:
                        # print("6:Token lido: " + get_special_token(line[j-2]))
                        str_final = str_final + get_special_token(line[j-2]) + "\n"
                        current = 0
                        last_final = 0
                        next = 0
                        cm = j
            #Se o simbolo lido eh um espaco, mas esta no estado inicial, devemos desconsidera-lo
            elif c == ' ' and current == 0:
                current = 0
                last_final = 0
                next = 0
                cm = j
            else:
                # print("Erro lexico")
                if not cond_error:
                    indexError = j
                cond_error = 1


    if cond_error:
        print("\033[01;32m")
        print("\nErro lexico em:\n\033[00;37m" + line)
        for k in range(1, indexError):
            print(" ", end = "")
        print("\033[01;32m^\033[00;37m\n\n\n")
    else:
        print(str_final)
    line = input("Digite sua entrada de dados: ")
