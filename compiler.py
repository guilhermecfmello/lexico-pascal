""""
Equipe:
Guilherme Mello
Vinicius Carloto Carnelocce

"""

from hash_symbol import HashTable
from lexico import AFD


if __name__ == '__main__':

    # CONSTANTES PARA CORES NO TERMINAL
    VERMELHO = '\033[01;31m'
    VERDE = '\033[32m'
    BRANCO = '\033[00;37m'

    print("Analisador Lexico\nPara sair, digite \'exit()\'\n\n\n")
    line = input().lower()

    # Inicializando tabela de palavras-chave/identificadores
    dic = HashTable()
    aut = AFD()
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
            if not aut.is_char(c):
                excep1 = False

            # Excecao do underline
            if c == '_' and current != 1:
                if not cond_error:
                    indexError = j
                cond_error = 1

            # Verifica se comecou a reconhecer uma palavra-chave/identificador
            if aut.is_char(c) and current == 0:
                start_char = j

            j = j + 1
            column = aut.get_column(c)
            # Se o simbolo lido pertencer ao alfabeto
            if column > -1 and not excep1:

                next = aut.transiton_table[current][column]
                # Se o caractere lido leva a um proximo estado
                if next > -1:
                    current = next
                    # Se o proximo estado eh um estado final, confirmamos a leitura lida ate aqui
                    if aut.is_final(next):
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
                                str_final = aut.identifiers(dic, id, str_final)

                                cm = j
                            else:
                                if last_final != 18:
                                    str_final = str_final + aut.get_token(last_final) + "\n"
                                    j = cm
                                else:
                                    str_final = str_final + aut.get_special_token(c) + "\n"

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
                        if aut.state_is_numeric(last_final) and aut.is_char(c):
                            excep1 = True
                        # Se nao for um dos caracteres especiais, podera imprimir o token
                        # do ultimo estado final, caso contrario, deve-se verificar qual
                        # eh o token lido
                        if last_final == 1:
                            j = j - 1
                            id = line[start_char:j]
                            str_final = aut.identifiers(dic, id, str_final)
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
                                    str_final = str_final + aut.get_token(last_final) + "\n"
                                else:
                                    str_final = str_final + aut.get_special_token(line[j - 2]) + "\n"

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
                        str_final = aut.identifiers(dic, id, str_final)
                        cm = j
                    else:
                        if last_final != 18:
                            str_final = str_final + aut.get_token(last_final) + "\n"
                            j = cm
                        else:
                            str_final = str_final + aut.get_special_token(line[j - 2]) + "\n"
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
