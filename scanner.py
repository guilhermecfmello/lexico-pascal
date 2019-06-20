import re
import sys


class AFD:
    """
    Define a tabela de transição para o autômato criado, além de indexar as colunas e tokens
    """

    def __init__(self):
        """
        Inicializa as estruturas do automato
        """
        self.transiton_table = [
            # ;,=[]/ a-z 0-9 - + . < > = ( * ) : comentario OTHER
            [+1, 19, 18, 16, 14, +6, 10, 12, +1, +2, +1, +1, +8, -1, -1],  # Estado 0
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 1
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, +3, -1, -1, -1, -1],  # Estado 2
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, +4, -1, -1, +3, -1],  # Estado 3
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, +5, -1, -1, -1],  # Estado 4
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 5
            [-1, -1, -1, -1, -1, +7, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 6
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 7
            [-1, -1, -1, -1, -1, -1, -1, -1, +9, -1, -1, -1, -1, -1, -1],  # Estado 8
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 9
            [-1, -1, -1, -1, -1, -1, -1, -1, 11, -1, -1, -1, -1, -1, -1],  # Estado 10
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 11
            [-1, -1, -1, -1, -1, -1, -1, -1, 13, -1, -1, -1, -1, -1, -1],  # Estado 12
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 13
            [-1, -1, 15, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 14
            [-1, -1, 15, -1, -1, 20, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 15
            [-1, -1, 17, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 16
            [-1, -1, 17, -1, -1, 21, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 17
            [-1, -1, 18, -1, -1, 22, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 18
            [-1, 19, 19, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 19
            [-1, -1, 20, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 20
            [-1, -1, 21, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 21
            [-1, -1, 22, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]  # Estado 22

        self.column = {key: value for value, key in enumerate(
            ['[;,\[\]\{\}\/]', '[a-zA-Z_]', '[0-9]', '\-', '\+', '\.', '\<', '\>', '\=', '\(', '\*', '\)', '\:', '.'])}

        self.state_type = {(1, 2, 6, 8, 10, 12, 14, 16): 'simbolo especial simples',
                           (7, 9, 11, 13): 'simbolo especial composto', (19,): 'identificador',
                           (15, 18): 'numero inteiro positivo', (20, 22): 'numero real positivo',
                           (17,): 'numero inteiro negativo', (21,): 'numero real negativo', (5,): 'comentario'}

    def scan(self, file):
        """
        Realiza a análise léxica do arquivo de entrada,
        utlizando a matriz de ajacencia anteriormente definida
        """
        line_count = 0
        for line in file:
            line_count += 1
            if not line.strip():
                continue
            line = line.rstrip()
            size = len(line)
            pos = 0
            while pos < size:
                token = self.next_word(line, pos, size)
                if token:
                    print(token[1])
                    pos = token[0]
                else:
                    print('Erro lexico')
                    sys.exit(1)

    def next_word(self, line, pos, size):
        """
        Analiza a string a procura de um token, e caso encontre
        retorna uma tupla contendo o tipo do token e seu valor,
        caso contrário, retorna a tupla -1 e o número da coluna, indicando erro léxico
        """
        state = 0
        lexeme = ""
        stack = [-1]

        while pos < size and line[pos].isspace():
            pos += 1

        while pos < size and state != -1:
            lexeme += line[pos]
            if self.is_final(state):
                stack = []
            stack.append(state)
            state = self.transiton_table[state][self.get_column(line[pos])]
            pos += 1

        while not self.is_final(state) and stack:
            state = stack.pop()
            lexeme = lexeme[:-1]
            pos -= 1

        if self.is_final(state):
            return [pos, (self.get_type(state), lexeme)]
        else:
            print(lexeme)
            return False

    def get_column(self, c):
        """
        Dado um caractere pertencente ao alfabeto,
        retorna a coluna correspondente na matriz de adjacencia
        """
        for value in self.column:
            if re.search(value, c):
                return self.column[value]

        return -1

    def is_final(self, state):
        """
        Dado um estado do automato, onde o estado inicial é 0,
        retorna True caso o estado seja final,
        caso contrario retorna False
        """
        for value in self.state_type:
            if state in value:
                return True
        else:
            return False

    def get_type(self, state):
        """
        Dado um estado do automato, onde o estado inicial é 0,
        retorna o tipo de token caso o estado exista,
        caso contrario retorna False
        """
        for value in self.state_type:
            if state in value:
                return self.state_type[value]
        else:
            return False

    # # Quando o automato termina no estado 18, deve-se saber qual eh o simbolo
    # # lido e entao imprimir seu Token
    # @staticmethod
    # def get_special_token(c):
    #     base = "Símbolo Especial Simples "
    #     if re.search('[;,=*\[\]{\}/]', c):
    #         return base + c
    #
    # # Se o caractere passado estiver em [a,b], retorna 1
    # # Retorna 0, caso contrario
    # @staticmethod
    # def is_char(c):
    #     if re.search('[a-z]', c):
    #         return 1
    #     else:
    #         return 0
    #
    # # Trata identificadores
    # @staticmethod
    # def identifiers(dic, string, str_final):
    #     cond_dic = dic.instalar_id(string)
    #     if cond_dic == 0:
    #         str_final = str_final + "Identificador " + string.upper() + "\n"
    #     elif cond_dic == -1:
    #         str_final = str_final + "Palavra Reservada " + string.upper() + "\n"
    #     return str_final
    #
    # # Caso especial 1: Quando lido um numero e em seguida uma letra, ex: 2a
    # # Deve gerar erro lexico
    # @staticmethod
    # def is_number(c):
    #     if re.search('[0-9]', c):
    #         return 1
    #     else:
    #         return 0
    #
    # # Verifica se o estado "state" corresponde a um estado final de token numerico
    # # Caso seja numero, retorna 1. Retorna 0 caso contrario
    # @staticmethod
    # def state_is_numeric(state):
    #     if state in [2, 3, 19, 20, 21, 22]:
    #         return 1
    #     else:
    #         return 0

    # Dado o estado, retorna o seu token, que eh a string referente
    # a sua identificacao, ou retorna "" (string vazia) caso o estado
    # nao exista ou nao tenha um token definido
    # @staticmethod
    # def get_token(state):
    #     if state == 2 or state == 3:
    #         return "Numeral positivo"
    #     elif state == 4:
    #         return "Simbolo especial simples ."
    #     elif state == 5:
    #         return "Simbolo especial composto .."
    #     elif state == 6:
    #         return "Simbolo especial simples :"
    #     elif state == 7:
    #         return "Simbolo especial composto :="
    #     elif state == 8:
    #         return "Simbolo especial simples >"
    #     elif state == 9:
    #         return "Simbolo especial composto >="
    #     elif state == 10:
    #         return "Simbolo especial simples <"
    #     elif state == 11:
    #         return "Simbolo especial composto <="
    #     elif state == 12:
    #         return "Simbolo especial simples ("
    #     elif state == 15:
    #         return "Comentario_fecho"
    #     elif state == 17:
    #         return "Simbolo especial composto )"
    #     elif state == 19 or state == 20:
    #         return "Numeral negativo"
    #     elif state == 21 or state == 22:
    #         return "Numeral positivo"
    #     elif state == 23:
    #         return "Simbolo especial simples +"
    #     elif state == 24:
    #         return "Simbolo especial simples -"
    #     elif state == 25:
    #         return "Simbolo especial composto <>"
    #     else:
    #         return ""
