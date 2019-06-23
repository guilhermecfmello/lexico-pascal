""""
Equipe:
Guilherme Mello
Vinicius Carloto Carnelocce

"""
import re
import sys

from hash_symbol import HashTable


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
            [+3, +3, +3, +3, +3, +3, +3, +3, +3, +3, +4, -1, +3, +3, -1],  # Estado 3
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, +5, -1, -1, -1],  # Estado 4
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 5
            [-1, -1, -1, -1, -1, +7, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 6
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 7
            [-1, -1, -1, -1, -1, -1, -1, -1, +9, -1, -1, -1, -1, -1, -1],  # Estado 8
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 9
            [-1, -1, -1, -1, -1, -1, -1, 23, 11, -1, -1, -1, -1, -1, -1],  # Estado 10
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
            [-1, -1, 22, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # Estado 22
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]  # Estado 23

        self.column = {key: value for value, key in enumerate(
            ['[\';,\[\]\{\}\/]', '[a-zA-Z_]', '[0-9]', '\-', '\+', '\.', '\<', '\>', '\=', '\(', '\*', '\)', '\:',
             '.'])}

        self.state_type = {(1, 2, 6, 8, 10, 12, 14, 16): 'simbolo especial simples',
                           (7, 9, 11, 13, 23): 'simbolo especial composto', (19,): 'identificador',
                           (15, 18): 'numero inteiro', (20, 22): 'numero real',
                           (17,): 'numero inteiro', (21,): 'numero real', (3,): 'comentario'}

        self.scanned = list()  # Lista de tokens lidos

    def scan(self, file, id_table):
        """
        Realiza a análise léxica do arquivo de entrada,
        utlizando a matriz de ajacencia anteriormente definida
        """
        line_count = 0  # Numero de linhas lidas / ultima linha lida
        for line in file:
            line_count += 1
            if not line.strip():  # verifica se é uma linha vazia
                continue
            line = line.rstrip()  # Remove nova linha e espaços à direita
            size = len(line)
            pos = 0
            while pos < size:
                token = self.next_word(line, pos, size, id_table)
                pos = token[0]
                if token[1]:  # Verifica se há erro léxico
                    self.scanned.append(token[1])
                else:
                    self.scanner_error(line_count, pos)

    def next_word(self, line, pos, size, id_table):
        """
        Analiza a string a procura de um token, e caso encontre
        retorna a coluna e uma tupla contendo o tipo do token e seu valor,
        caso contrário, retorna a coluna e o valor False, indicando erro léxico
        """
        state = 0
        lexeme = ""
        stack = [-1]

        while pos < size and line[pos].isspace():  # Lê os espaços
            pos += 1

        while pos < size and state != -1:  # Lê a linha char a char, até encontrar um estado inválido
            if state == 0 and line[pos] == '_':  # Exceção de começar com underline
                return [pos, False]
            lexeme += line[pos]
            if self.is_final(state):
                stack = []
            stack.append(state)  # Empilha os estados encontrados
            state = self.transiton_table[state][self.get_column(line[pos])]
            pos += 1

        while not self.is_final(state) and stack:  # Desempilha os estados até encontar um estado final, ou até esvaziar
            state = stack.pop()
            lexeme = lexeme[:-1]
            pos -= 1

        if self.is_final(state):  # Verifica se o estado é final

            if state == 3:  # Desconsidera os comentários
                commentary = re.search('[\s\S]*\*\)', line[pos:])
                if not commentary:
                    return [pos, False]  # Erro léxico
                lexeme += commentary.group()
                pos += commentary.end()

            if state == 19:  # Passa o identificador para a hash table

                if not id_table.instalar_id(lexeme):
                    return [pos, ['palavra reservada', lexeme]]

            return [pos, [self.get_type(state), lexeme]]
        else:
            return [pos, False]  # Erro léxico

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

    @staticmethod
    def scanner_error(line_count, pos):
        """
        Printa para o usuario a informação sobre o erro léxico,
        contendo a linha do erro, e a respectiva coluna
        """
        print("\n  Erro léxico\n\n    linha {0} coluna {1}\n".format(line_count, pos + 1))
        sys.exit(1)

    def scanner_print(self):
        """
        Printa os tokens reconhecidos pelo scanner
        """
        for token in self.scanned:
            print("< {0} ,  {1}  >\n".format(token[0], token[1]))


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("Modo de uso: python scanner.py arquivo")
        sys.exit(1)

    try:
        file = open(sys.argv[1])
    except IOError:
        print("Erro na abertura do arquivo")
        sys.exit(1)

    scanner = AFD()
    identifier_table = HashTable()

    with file:
        scanner.scan(file, identifier_table)
        scanner.scanner_print()
        identifier_table.hash_info()
