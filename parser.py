import re
import sys


class Parser:

    def __init__(self):
        self.scanned = list()
        self.pos = -1

    def parsing_error(self):
        print('erro semantico: ' + str(self.scanned[self.pos]))
        sys.exit(1)

    @staticmethod
    def parsing_end():
        print('Sucesso!')

    def eat(self, match):
        if self.pos + 1 > len(self.scanned):
            return False
        if match in self.scanned[self.pos+1]:
            self.pos +=1
            return True
        else:
            return False

    def digest(self, value):
        if value:
            return True
        else:
            self.parsing_error()

    def program(self):
        self.digest(self.eat('program'))
        self.digest(self.identifier())
        self.digest(self.eat('('))
        self.digest(self.identifier())
        while self.eat(','):
            self.digest(self.identifier())
        self.digest(self.eat(')'))
        self.digest(self.eat(';'))
        self.digest(self.block())
        return self.digest(self.eat('.'))  # End of program

    def block(self):
        if self.eat('label'):
            self.digest(self.number())
            while self.eat(','):
                self.digest(self.number())
            self.digest(self.eat(';'))
            return self.digest(self.block())
        if self.eat('type'):
            self.digest(self.identifier())
            self.digest(self.eat('='))
            self.digest(self.type())  # TODO type
            self.digest(self.eat(';'))
            while self.identifier():
                self.digest(self.eat(';'))
            return self.digest(self.block())
        if  self.digest(self.eat('var')):
            self.digest(self.identifier())
            while self.eat(','):
                self.digest(self.identifier())
            self.digest(self.eat(':'))
            self.digest(self.type())
            self.digest(self.eat(';'))
            while self.identifier():
                while self.eat(','):
                    self.digest(self.identifier())
                self.digest(self.eat(':'))
                self.digest(self.type())
                self.digest(self.eat(';'))
            return self.digest(self.block())
        if self.eat('procedure'):
            self.digest(self.identifier())
            self.formal_param() # TODO formal_param
            self.digest(self.eat(';'))
            self.digest(self.block())
            self.digest(self.eat(';'))
            return self.digest(self.block())
        if self.eat('procedure'):
            self.digest(self.identifier())
            self.formal_param()
            self.digest(self.eat(':'))
            self.digest(self.identifier())
            self.digest(self.eat(';'))
            self.digest(self.block())
            self.digest(self.eat(';'))
            return self.digest(self.block())
        if self.eat('begin'):
            self.digest(self.command())  # TODO command
            while self.command():
                pass
            return self.digest(self.eat('end'))  # End of block

    def identifier(self):
        return self.eat('identificador')

    def number(self):
        if self.digest(self.eat()):
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
        if parser.program():
            parser.parsing_end()
        else:
            parser.parsing_error()
