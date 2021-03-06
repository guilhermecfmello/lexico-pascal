import sys


class Parser:

    def __init__(self, scanner_output):
        """
        Inicializa as estruturas do parser
        """
        self.scanned = scanner_output  # Lista de tokens do scanner
        self.pos = -1  # Inicializa em -1, para iterar em 0
        self.current = ''  # Guarda o token atual

    def parsing_error(self):
        """
        Reporta um erro sintatico

        """
        print("\n  Erro sintático\n\n    linha {0} coluna {1}\n".format(self.current[2], self.current[3]))
        sys.exit(1)

    @staticmethod
    def parsing_end():
        print('  Compilado sem erros sintáticos\n')

    def next(self):
        if self.pos + 1 >= len(self.scanned):
            return False
        else:
            self.pos += 1
            # print(str(self.current))
            self.current = self.scanned[self.pos]
            return True

    def eat(self, *match):
        """
        Caso o proximo token seja match,
        move pos para frente e retorna True,
        caso contrário, retorna False
        """
        if match:
            if match[0] in self.current:
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
        self.parsing_end()

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
            self.block()

        elif 'type' in self.current:
            self.eat('type')
            self.identifier()
            self.eat('=')
            self.type()
            self.eat(';')
            while 'identificador' in self.current:
                self.identifier()
                self.eat(';')
            self.block()

        elif 'var' in self.current:
            self.eat('var')
            self.identifier()
            while ',' in self.current:
                self.eat(',')
                self.identifier()
            self.eat(':')
            self.type()
            self.eat(';')
            while 'identificador' in self.current:
                self.identifier()
                while ',' in self.current:
                    self.eat(',')
                    self.identifier()
                self.eat(':')
                self.type()
                self.eat(';')
            self.block()

        elif 'procedure' in self.current:
            self.eat('procedure')
            self.identifier()
            if ';' not in self.current:
                self.formal_param()
            self.eat(';')
            self.block()
            self.eat(';')
            self.block()

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
            self.block()

        else:
            self.eat('begin')
            self.command()
            while ';' in self.current:
                self.eat(';')
                self.command()
            self.eat('end')  # End of block

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
            self.identifier()
            while ',' in self.current:
                self.eat(',')
                self.identifier()
            self.eat(':')
            self.identifier()

        elif 'procedure' in self.current:
            self.eat('procedure')
            self.identifier()
            while ',' in self.current:
                self.eat(',')
                self.identifier()

        else:
            if 'var' in self.current:
                self.eat('var')
            self.identifier()
            while ',' in self.current:
                self.eat(',')
                self.identifier()
            self.eat(':')
            self.identifier()

        while ';' in self.current:
            self.eat(';')
            if 'function' in self.current:
                self.eat('function')
                self.identifier()
                while ',' in self.current:
                    self.eat(',')
                    self.identifier()
                self.eat(':')
                self.identifier()

            elif 'procedure' in self.current:
                self.eat('procedure')
                self.identifier()
                while ',' in self.current:
                    self.eat(',')
                    self.identifier()

            else:
                if 'var' in self.current:
                    self.eat('var')
                self.identifier()
                while ',' in self.current:
                    self.eat(',')
                    self.identifier()
                self.eat(':')
                self.identifier()

        self.eat(')')

    def command(self):
        if any(elem in self.current for elem in ['numero inteiro', 'numero real']):
            self.number()
            self.eat(':')
        self.command_no_label()

    def command_no_label(self):
        if 'identificador' in self.current:
            self.identifier()
            if '[' in self.current:
                self.eat('[')
                self.expression()
                while ',' in self.current:
                    self.eat(',')
                    self.expression()
                self.eat(']')
                self.eat(':=')
                self.expression()
            elif '(' in self.current:
                self.eat('(')
                self.expression()
                while ',' in self.current:
                    self.eat(',')
                    self.expression()
                self.eat(')')
            elif ':=' in self.current:
                self.eat(':=')
                self.expression()
            else:
                pass

        elif 'goto' in self.current:
            self.eat('goto')
            self.number()
        elif 'begin' in self.current:
            self.eat('begin')
            self.command()
            while ';' in self.current:
                self.eat(';')
                self.command()
            self.eat('end')
        elif 'if' in self.current:
            self.eat('if')
            self.expression()
            self.eat('then')
            self.command_no_label()
            if 'else' in self.current:
                self.eat('else')
                self.command_no_label()
        # elif 'while':
        else:
            self.eat('while')
            self.expression()
            self.eat('do')
            self.command_no_label()

    def expression(self):
        self.simple_expression()
        if any(item in self.current for item in ['=', '<>', '<', '<=', '>=', '>']):
            self.eat()
            self.simple_expression()

    def simple_expression(self):
        if '+' in self.current:
            self.eat('+')
        elif '-' in self.current:
            self.eat('-')

        self.term()

        while '+' in self.current or '-' in self.current or 'or' in self.current:
            self.eat()
            self.term()

    def term(self):
        self.factor()
        while '*' in self.current or 'div' in self.current or 'and' in self.current:
            if '*' in self.current:
                self.eat('*')
            elif 'div' in self.current:
                self.eat('div')
            elif 'and' in self.current:
                self.eat('and')
            self.factor()

    def factor(self):
        if 'identificador' in self.current:
            self.identifier()
            if '[' in self.current:
                self.eat('[')
                self.expression()
                while ',' in self.current:
                    self.eat(',')
                    self.expression()
                self.eat(']')
            elif '(' in self.current:
                if '(' in self.current:
                    self.eat('(')
                    self.expression()
                    while ',' in self.current:
                        self.eat(',')
                        self.expression()
                    self.eat(')')
            else:
                pass
        elif any(elem in self.current for elem in ['numero inteiro', 'numero real']):
            self.number()
        elif '(' in self.current:
            self.eat('(')
            self.expression()
            self.eat(')')
        elif 'not' in self.current:
            self.eat('not')
            self.factor()
        elif 'true' in self.current:
            self.eat('true')
        # elif 'false' in self.current:
        else:
            self.eat('false')

    def identifier(self):
        if self.eat('identificador'):
            return True
        else:
            return False

    def number(self):
        if any(elem in self.current for elem in ['numero inteiro', 'numero real']):
            self.eat()
            return True
        else:
            return False


# if __name__ == '__main__':
#
#     if len(sys.argv) < 2:
#         print("Modo de uso: python parser.py arquivo")
#         sys.exit(1)
#
#     try:
#         file = open(sys.argv[1])
#     except IOError:
#         print("Erro na abertura do arquivo")
#         sys.exit(1)
#
#     parser = Parser()
#
#     with file:
#         line_count = 0
#         for line in file:
#             line_count += 1
#             lexeme = re.search("<([a-z\s]*),([\S\s]*)>", line)
#             if lexeme:
#                 parser.scanned.append([lexeme.group(1).strip(), lexeme.group(2).strip()])
#         parser.parse()
