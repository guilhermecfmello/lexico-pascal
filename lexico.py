'''
 _____            _
| ____|__ _ _   _(_)_ __   ___   _
|  _| / _` | | | | | '_ \ / _ \ (_)
| |__| (_| | |_| | | |_) |  __/  _
|_____\__, |\__,_|_| .__/ \___| (_)
         |_|       |_|

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

from hash_symbol import HashTable


# Dado um caractere pertencente ao alfabeto, retorna a coluna
# correspondente na matriz de adjacencia
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
    elif c == ';':
        return 18
    elif c == '/':
        return 19
    elif c == '_':
        return 20
    else:
        return -1


# Dado um estado do automato, onde o estado inicial eh 0,
# Retorna 1 caso o estado seja final, caso contrario retorna 0
def is_final(state):
    if state == 0:
        return 0
    elif state == 14:
        return 0
    elif state > 25 or state < 0:
        return 0
    else:
        return 1


# Dado o estado, retorna o seu token, que eh a string referente
# a sua identificacao, ou retorna "" (string vazia) caso o estado
# nao exista ou nao tenha um token definido
def get_token(state):
    if state == 2 or state == 3:
        return "Numeral positivo"
    elif state == 4:
        return "Simbolo especial simples ."
    elif state == 5:
        return "Simbolo especial composto .."
    elif state == 6:
        return "Simbolo especial simples :"
    elif state == 7:
        return "Simbolo especial composto :="
    elif state == 8:
        return "Simbolo especial simples >"
    elif state == 9:
        return "Simbolo especial composto >="
    elif state == 10:
        return "Simbolo especial simples <"
    elif state == 11:
        return "Simbolo especial composto <="
    elif state == 12:
        return "Simbolo especial simples ("
    elif state == 15:
        return "Comentario_fecho"
    elif state == 17:
        return "Simbolo especial composto )"
    elif state == 19 or state == 20:
        return "Numeral negativo"
    elif state == 21 or state == 22:
        return "Numeral positivo"
    elif state == 23:
        return "Simbolo especial simples +"
    elif state == 24:
        return "Simbolo especial simples -"
    elif state == 25:
        return "Simbolo especial composto <>"
    else:
        return ""

# Quando o automato termina no estado 18, deve-se saber qual eh o simbolo
# lido e entao imprimir seu Token
def get_special_token(c):
    base = "Símbolo Especial Simples "

    if c == ';':
        return base + c
    elif c == ',':
        return base + c
    elif c == '=':
        return base + c
    elif c == '*':
        return base + c
    elif c == '[':
        return base + c
    elif c == ']':
        return base + c
    elif c == '{':
        return base + c
    elif c == '}':
        return base + c
    elif c == '/':
        return base + c


# Se o caractere passado estiver em [a,b], retorna 1
# Retorna 0, caso contrario
def is_char(c):
    if c >= 'a' and c <= 'z':
        return 1
    else:
        return 0


# Trata identificadores
def identifiers(dic, string, str_final):
    cond_dic = dic.instalar_id(string)
    if cond_dic == 0:
        str_final = str_final + "Identificador " + string.upper() + "\n"
    elif cond_dic == -1:
        str_final = str_final + "Palavra Reservada " + string.upper() + "\n"
    return str_final


# Caso especial 1: Quando lido um numero e em seguida uma letra, ex: 2a
# Deve gerar erro lexico
def is_number(c):
    if c in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return 1
    else:
        return 0


# Verifica se o estado "state" corresponde a um estado final de token numerico
# Caso seja numero, retorna 1. Retorna 0 caso contrario
def state_is_numeric(state):
    if state in [2, 3, 19, 20, 21, 22]:
        return 1
    else:
        return 0


# CONSTANTES PARA CORES NO TERMINAL
VERMELHO = '\033[01;31m'
VERDE = '\033[32m'
BRANCO = '\033[00;37m'

#   a-z, 0-9, . , ' , , , : , ) , = , * , [ , ] , { , } , < , > , ( ,  + , - , ; , / , _
states = [
    [ 1,  2,  4, 18, 18,  6, 17, 18, 18, 18, 18, 18, 18, 10,  8, 12, 23, 24, 18, 18, -1],  # Estado 0
    [ 1,  1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  1],  # Estado 1
    [-1,  2,  3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 2
    [-1,  3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 3
    [-1, -1,  5, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 4
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 5
    [-1, -1, -1, -1, -1, -1, -1,  7, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 6
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 7
    [-1, -1, -1, -1, -1, -1, -1,  9, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 8
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 9
    [-1, -1, -1, -1, -1, -1, -1, 11, -1, -1, -1, -1, -1, -1, 25, -1, -1, -1, -1, -1, -1],  # Estado 10
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 11
    [-1, -1, -1, -1, -1, -1, -1, -1, 26, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 12
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 13
    [-1, -1, -1, -1, -1, -1, 15, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 14
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 15
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 16
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 17
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 18
    [-1, 19, 20, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 19
    [-1, 20, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 20
    [-1, 21, 22, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 21
    [-1, 22, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 22
    [-1, 21, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 23
    [-1, 19, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 24
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 25
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]  # Estado 26
]
print("Analisador Lexico\nPara sair, digite \'exit()\'\n\n\n")
line = input().lower()

# Inicializando tabela de palavras-chave/identificadores
dic = HashTable()
lineError = 1
finalPrint = ''
while line != '':
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

    excep1 = False
    while j < len(line):
        c = line[j]
        if not is_char(c):
            excep1 = False

        # Excecao do underline
        if c == '_' and current != 1:
            if not cond_error:
                indexError = j
            cond_error = 1

        # Verifica se comecou a reconhecer uma palavra-chave/identificador
        if is_char(c) and current == 0:
            start_char = j

        j = j + 1
        column = get_column(c)
        # Se o simbolo lido pertencer ao alfabeto
        if column > -1 and not excep1:

            next = states[current][column]
            # Se o caractere lido leva a um proximo estado
            if next > -1:
                current = next
                # Se o proximo estado eh um estado final, confirmamos a leitura lida ate aqui
                if is_final(next):
                    last_final = current
                    cm = j
                    # Se chegou no final da linha
                    if j == len(line):

                        # Se nao for um dos caracteres especiais, podera imprimir o token
                        # do ultimo estado final, caso contrario, deve-se verificar qual
                        # eh o token lido
                        if last_final == 1:
                            # Se terminar no estado 1 do automato, devera haver uma verificacao
                            # na tabela de simbolos
                            id = line[start_char:j]
                            str_final = identifiers(dic, id, str_final)

                            cm = j
                        else:
                            if last_final != 18:
                                str_final = str_final + get_token(last_final) + "\n"
                                j = cm
                            else:
                                str_final = str_final + get_special_token(c) + "\n"

                        current = 0
                        last_final = 0
                        next = 0
            # Se o caractere lido nao leva a um proximo estado
            else:
                # Se o caractere lido nao leva a um proximo estado e o automato esta no estado inicial
                # entao o char nao existe no alfabeto da linguagem, ou seja, erro lexico
                if current == 0:
                    cm = j
                    current = 0
                    last_final = 0
                    next = 0
                    if not cond_error:
                        indexError = j
                    cond_error = 1
                # Se o caractere nao leva a um proximo estado, mas tb o automato nao esta no estado
                # inicial, ainda pode ser aceito pela linguagem
                else:
                    # Caso excessao 1 , exemplo 2a
                    if state_is_numeric(last_final) and is_char(c):
                        excep1 = True
                    # Se nao for um dos caracteres especiais, podera imprimir o token
                    # do ultimo estado final, caso contrario, deve-se verificar qual
                    # eh o token lido
                    if last_final == 1:
                        j = j - 1
                        id = line[start_char:j]
                        str_final = identifiers(dic, id, str_final)
                        current = 0
                        last_final = 0
                        next = 0
                        cm = j
                    else:
                        if excep1:
                            if not cond_error:
                                cond_error = 1
                                indexError = j
                        else:
                            if last_final != 18:
                                str_final = str_final + get_token(last_final) + "\n"
                            else:
                                str_final = str_final + get_special_token(line[j - 2]) + "\n"

                            j = cm
                            current = 0
                            next = 0
                            last_final = 0


        # Se o simbolo lido nao pertence ao alfabeto
        else:
            # Se o simbolo lido for espaco, nao ha erro lexico, apenas imprimimos o token lido
            # ate aqui, e resetamos o automato
            if c == ' ' and current != 0:
                # Se nao for um dos caracteres especiais, podera imprimir o token
                # do ultimo estado final, caso contrario, deve-se verificar qual
                # eh o token lido
                if last_final == 1:
                    id = line[start_char:j - 1]
                    str_final = identifiers(dic, id, str_final)
                    cm = j
                else:
                    if last_final != 18:
                        str_final = str_final + get_token(last_final) + "\n"
                        j = cm
                    else:
                        str_final = str_final + get_special_token(line[j - 2]) + "\n"
                        cm = j

                current = 0
                last_final = 0
                next = 0
            # Se o simbolo lido eh um espaco, mas esta no estado inicial, devemos desconsidera-lo
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
        print(VERMELHO)
        print("\nErro lexico na linha " + VERDE + str(lineError) + VERMELHO + " coluna " + VERDE + str(
            indexError) + BRANCO)
        print(line)
        for k in range(1, indexError):
            print(" ", end="")
        print(VERDE + "^" + BRANCO + "\n\n\n")
        break
    else:
        finalPrint = finalPrint + str_final
    # /        str_final = str_final
    # print(str_final, end="")
    try:
        line = input().lower()
    except EOFError:
        break
    lineError = lineError + 1
    # line = line.lower()

# dic.hash_info()

if not cond_error:
    print(VERDE + "COMPILADO SEM ERROS LEXICOS:" + BRANCO)
    print(finalPrint)




# Antigo get_token() aqui:



# elif state == 4:
#     return "Ponto simples"
# elif state == 5:
#     return "Ponto duplo"
# elif state == 6:
#     return "Dois pontos"
# elif state == 7:
#     return "Atribuicao"
# elif state == 8:
#     return "Maior que"
# elif state == 9:
#     return "Maior ou igual que"
# elif state == 10:
#     return "Menor que"
# elif state == 11:
#     return "Menor ou igual que"
# elif state == 12:
#     return "Parenteses_esq"
# elif state == 15:
#     return "Comentario_fecho"
# elif state == 17:
#     return "Parenteses_dir"
# elif state == 18:
#     return "Varios (Tratar aqui)"
# elif state == 19 or state == 20:
#     return "Numeral negativo"
# elif state == 21 or state == 22:
#     return "Numeral positivo"
# elif state == 23:
#     return "Mais"
# elif state == 24:
#     return "Menos"
# elif state == 25:
#     return "Diferente"