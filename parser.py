import re
import sys


class Parser:

    def __init__(self):
        """
        Inicializa as estruturas do parser
        """
        self.scanned = list()  # Lista de tokens do scanner
        self.pos = -1  # Inicializa em -1, para iterar em 0
        self.current = ''  # Guarda o token atual

    def parsing_error(self):
        """
        Reporta um erro sintatico
        """
        print('Erro sintatico: ' + str(self.scanned[self.pos]))
        sys.exit(1)

    @staticmethod
    def parsing_end():
        print('Sucesso!')

    def next(self):
        if self.pos + 1 >= len(self.scanned):
            return False
        else:
            self.pos += 1
            self.current = self.scanned[self.pos]
            return True

    def eat(self, match):
        """
        Caso o proximo token seja match,
        move pos para frente e retorna True,
        caso contrário, retorna False
        """
        if match in self.current:
            self.next()
            return True
        else:
            self.parsing_error()

    def parse(self):
        """
        Inicia a análise sintática
        """
        self.next()
        if self.program():
            return True
        else:
            return False

    def program(self):
        self.eat('program')
        self.identifier()
        self.eat('(')
        self.identifier()
        while ',' in self.current:
            self.eat(',')
            self.identifier()
        self.eat(')')
        self.eat(';')
        # self.digest(self.block())
        return self.eat('.')  # End of program

    # def block(self):
    #     if self.eat('label'):
    #         self.digest(self.number())
    #         while self.eat(','):
    #             self.digest(self.number())
    #         self.digest(self.eat(';'))
    #         return self.digest(self.block())
    #     if self.eat('type'):
    #         self.digest(self.identifier())
    #         self.digest(self.eat('='))
    #         self.digest(self.type())  # TODO type
    #         self.digest(self.eat(';'))
    #         while self.identifier():
    #             self.digest(self.eat(';'))
    #         return self.digest(self.block())
    #     if self.digest(self.eat('var')):
    #         self.digest(self.identifier())
    #         while self.eat(','):
    #             self.digest(self.identifier())
    #         self.digest(self.eat(':'))
    #         self.digest(self.type())
    #         self.digest(self.eat(';'))
    #         while self.identifier():
    #             while self.eat(','):
    #                 self.digest(self.identifier())
    #             self.digest(self.eat(':'))
    #             self.digest(self.type())
    #             self.digest(self.eat(';'))
    #         return self.digest(self.block())
    #     if self.eat('procedure'):
    #         self.digest(self.identifier())
    #         self.formal_param()  # TODO formal_param
    #         self.digest(self.eat(';'))
    #         self.digest(self.block())
    #         self.digest(self.eat(';'))
    #         return self.digest(self.block())
    #     if self.eat('procedure'):
    #         self.digest(self.identifier())
    #         self.formal_param()
    #         self.digest(self.eat(':'))
    #         self.digest(self.identifier())
    #         self.digest(self.eat(';'))
    #         self.digest(self.block())
    #         self.digest(self.eat(';'))
    #         return self.digest(self.block())
    #     if self.eat('begin'):
    #         self.digest(self.command())  # TODO command
    #         while self.command():
    #             pass
    #         return self.digest(self.eat('end'))  # End of block

    def identifier(self):
        if self.eat('identificador'):
            return True
        else:
            return False

    def number(self):
        if self.eat('numero inteiro') or self.eat('numero real'):
            return True
        else:
            return False


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("Modo de uso: python parser.py arquivo")
        sys.exit(1)

    try:
        file = open(sys.argv[1])
    except IOError:
        print("Erro na abertura do arquivo")
        sys.exit(1)

    parser = Parser()

    with file:
        line_count = 0
        for line in file:
            line_count += 1
            lexeme = re.search("<([a-z\s]*),([\S\s]*)>", line)
            if lexeme:
                parser.scanned.append([lexeme.group(1).strip(), lexeme.group(2).strip()])
        if parser.parse():
            parser.parsing_end()
        else:
            parser.parsing_error()
