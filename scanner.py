import re


class AFD:
    """
    Define a tabela de transição para o autômato criado, além de indexar as colunas e tokens
    """

    def __init__(self):
        """
        Inicializa as estruturas do automato
        """
        self.transiton_table = [
            #    ;.=*[])    a-z    0-9    -     +     .     <     >     =     (     *     )     :     OTHER
            [1, 19, 18, 16, 14, 6, 10, 12, -1, 2, -1, -1, 8, -1],  # Estado 0
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 1
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 3, -1, -1, -1],  # Estado 2
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 4, -1, -1, -1],  # Estado 3
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 5, -1, -1],  # Estado 4
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 5
            [-1, -1, -1, -1, -1, 7, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 6
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 7
            [-1, -1, -1, -1, -1, -1, -1, -1, 9, -1, -1, -1, -1, -1],  # Estado 8
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 9
            [-1, -1, -1, -1, -1, -1, -1, -1, 11, -1, -1, -1, -1, -1],  # Estado 10
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 11
            [-1, -1, -1, -1, -1, -1, -1, -1, 13, -1, -1, -1, -1, -1],  # Estado 12
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 13
            [-1, -1, 15, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 14
            [-1, -1, 15, -1, -1, 20, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 15
            [-1, -1, 17, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 16
            [-1, -1, 17, -1, -1, 21, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 17
            [-1, -1, 18, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 18
            [-1, 19, 19, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 19
            [-1, -1, 20, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 20
            [-1, -1, 21, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]  # Estado 21

        self.column = {key: value for value, key in enumerate(
            ['[a-z]+', '[0-9]+', '\.', '\'', ',', ':', '\)', '=', '\*', '\[', '\]', '\{', '\}', '<', '>', '\(', '\+',
             '-', ';', '/', '_'])}

    # Dado um caractere pertencente ao alfabeto, retorna a coluna
    # correspondente na matriz de adjacencia
    def get_column(self, c):
        for value in self.column:
            if re.search(value, c):
                return self.column[value]

        return -1

    # Dado um estado do automato, onde o estado inicial eh 0,
    # Retorna 1 caso o estado seja final, caso contrario retorna 0
    @staticmethod
    def is_final(state):
        if state == 0 or state == 14:
            return 0
        elif state > 25 or state < 0:
            return 0
        else:
            return 1

    # Dado o estado, retorna o seu token, que eh a string referente
    # a sua identificacao, ou retorna "" (string vazia) caso o estado
    # nao exista ou nao tenha um token definido
    @staticmethod
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
    @staticmethod
    def get_special_token(c):
        base = "Símbolo Especial Simples "
        if re.search('[;,=*\[\]{\}/]', c):
            return base + c

    # Se o caractere passado estiver em [a,b], retorna 1
    # Retorna 0, caso contrario
    @staticmethod
    def is_char(c):
        if re.search('[a-z]', c):
            return 1
        else:
            return 0

    # Trata identificadores
    @staticmethod
    def identifiers(dic, string, str_final):
        cond_dic = dic.instalar_id(string)
        if cond_dic == 0:
            str_final = str_final + "Identificador " + string.upper() + "\n"
        elif cond_dic == -1:
            str_final = str_final + "Palavra Reservada " + string.upper() + "\n"
        return str_final

    # Caso especial 1: Quando lido um numero e em seguida uma letra, ex: 2a
    # Deve gerar erro lexico
    @staticmethod
    def is_number(c):
        if re.search('[0-9]', c):
            return 1
        else:
            return 0

    # Verifica se o estado "state" corresponde a um estado final de token numerico
    # Caso seja numero, retorna 1. Retorna 0 caso contrario
    @staticmethod
    def state_is_numeric(state):
        if state in [2, 3, 19, 20, 21, 22]:
            return 1
        else:
            return 0
