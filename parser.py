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
        print('Erro sintatico: ' + str(self.current))
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

    def eat(self, *match):
        """
        Caso o proximo token seja match,
        move pos para frente e retorna True,
        caso contrário, retorna False
        """
        if match:
            if match in self.current:
                self.next()
            else:
                self.parsing_error()
        else:
            self.next()

    def parse(self):
        """
        Inicia a análise sintática
        """
        self.next()
        self.program()

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
        self.block()
        self.eat('.')  # End of program

    def block(self):
        if 'label' in self.current:
            self.eat('label')
            self.number()
            while ',' in self.current:
                self.eat(',')
                self.number()
            self.eat(';')
            return self.block()

        elif 'type' in self.current:
            self.eat('type')
            self.identifier()
            self.eat('=')
            self.type()  # TODO type
            self.eat(';')
            while 'identificador' in self.current:
                self.identifier()
                self.eat(';')
            return self.block()

        elif 'var' in self.current:
            self.eat('var')
            self.identifier()
            while ',' in self.current:
                self.eat(',')
                self.identifier()
            self.eat(':')
            self.type()
            self.eat(';')
            while 'identificador' in  self.current:
                self.identifier()
                while ',' in self.current:
                    self.eat(',')
                    self.identifier()
                self.eat(':')
                self.type()
                self.eat(';')
            return self.block()

        elif 'procedure' in self.current:
            self.eat('procedure')
            self.identifier()
            if ';' in self.current:
                self.eat(';')
            else:
                self.formal_param()  # TODO formal_param
            self.block()
            self.eat(';')
            return self.block()

        elif 'function' in self.current:
            self.eat('function')
            self.identifier()
            if ':' in self.current:
                pass
            else:
                self.formal_param()
            self.eat(':')
            self.identifier()
            self.eat(';')
            self.block()
            self.eat(';')
            return self.block()

        else:
            self.eat('begin')
            self.command()  # TODO command
            while 'end' not in self.current:
                self.command()
            self.eat('end') # End of block

    def type(self):
        if 'identificador' in self.current:
            self.identifier()
        else:
            self.eat('array')
            self.eat('[')
            self.number()
            self.eat('..')
            self.number()
            while ',' in self.current:
                self.eat(',')
                self.number()
                self.eat('..')
                self.number()
            self.eat(']')
            self.eat('of')
            self.type()

    def formal_param(self):
        self.eat('(')
        if 'function' in self.current:
            self.eat('function')
            while ',' in self.current:
                self.eat(',')
                self.identifier()
            self.eat(':')
            self.identifier()

        elif 'procedure' in self.current:
            self.identifier()
            while ',' in self.current:
                self.eat(',')
                self.identifier()

        else:
            if 'var' in self.current:
                self.eat('var')
            while ',' in self.current:
                self.eat(',')
                self.identifier()
            self.eat(':')
            self.identifier()

        while ';' in self.current:
            self.eat(';')
            if 'function' in self.current:
                self.eat('function')
                while ',' in self.current:
                    self.eat(',')
                    self.identifier()
                self.eat(':')
                self.identifier()

            elif 'procedure' in self.current:
                self.identifier()
                while ',' in self.current:
                    self.eat(',')
                    self.identifier()

            else:
                if 'var' in self.current:
                    self.eat('var')
                while ',' in self.current:
                    self.eat(',')
                    self.identifier()
                self.eat(':')
                self.identifier()

        self.eat(')')

        def command():
            self.number()
            while ':' in self.current:
                self.eat(':')
                self.number()
            self.command_without_label()

    def identifier(self):
        if self.eat('identificador'):
            return True
        else:
            return False

    def number(self):
        if any(elem in ['numero inteiro', 'numero real']  for elem in self.current):
            self.eat()
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
        parser.parse()
