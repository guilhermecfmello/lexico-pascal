import string
import sys
class Automata:
    # número de estados que o autômato tem
    """
    Gera o autômato com N estados
    """

    symbols = 128
    delta = []
    F = []
    # O autômato possui N estados, as funções delta e os estados finais
    def set_transition(self, state, symbol, next_state):
        # print(state)
        self.delta[state-1][ord(str(symbol))] = next_state

    def __init__(self, n_states):
        self.n_states = n_states 
        self.delta = []
        self.F = []

        #Inicialização do autômato vazio
        for i in range(self.n_states):
            line = []
            for j in range(self.symbols):
                line.append(-1)
            self.delta.append(line)

        #A-Za-z
        #falta colocar coisas como _
        for letter in string.ascii_letters:
            self.set_transition(1, letter, 2)
            self.set_transition(2, letter, 2)

        #0-9
        for number in range(9):
            self.set_transition(1, number, 3)
            self.set_transition(2, number, 2)
            self.set_transition(3, number, 3)
            self.set_transition(4, number, 4)
            self.set_transition(20, number, 20)
            self.set_transition(21, number, 21)
            self.set_transition(22, number, 22)
            self.set_transition(23, number, 23)

        #Parenteses ou abre comentário
        self.set_transition(1, '(', 13 )
        self.set_transition(13, '*', 14)

        self. set_transition(1, '+', 22)
        self.set_transition(22, '.', 23)

        self.set_transition(1, '-', 20)
        self.set_transition(20, '.', 21)

        self.set_transition(3, '.', 4)

        self.set_transition(1, '.', 5)
        self.set_transition(5, '.', 6)


        self.set_transition(1, ':', 7)
        self.set_transition(7, '=', 8)

        self.set_transition(1, '>', 9)
        self.set_transition(9, '=', 10)

        self.set_transition(1, '<', 11)
        self.set_transition(11, '=', 12)

        for special in [';', ',', '=', '[', ']']:
            self.set_transition(1, special, 15)
        
        #Adiciona os estados finais
        # 1 a 23
        for i in range(23):
            self.F.append(i)

        #TODO
        #Analisar se há mais estados ou se falta algo no automato

    def is_final(self, state):
        return True if state -1 in self.F else False 
    def get_transition(self,state, symbol):
        return self.delta[state-1][ord(str(symbol))]

    #
    
class SymbolTable:
    def __init__(self):
        print("TODO")
automato = Automata(23)



if len(sys.argv)!= 2:
    print("usage: python lexico.py -f file.txt")
    sys.exit(1)

try:
    file = open(sys.argv[1])
except IOError:
        print("Error opening the file")
        sys.exit(1)

inpt = file.read()

print("File name ", sys.argv[1])
curr_state = 1
last_final = -1

last_final_pos= 0
start = 0
pos = 0
while pos < len(inpt):
    symbol = inpt[pos]
    curr_state = automato.get_transition(curr_state, symbol)
    # print("Symbol ",  symbol, "Curr", curr_state, "last_f", last_final_pos, end=" ")

    if automato.is_final(curr_state):
        last_final = curr_state
        last_final_pos = pos

    #Quando le algum estado inválido
    if curr_state == -1:

        #estado final
        if last_final != -1:
            print(inpt[start:last_final_pos+1])
            start = last_final_pos +1
        else:
            if symbol not in [' ', '\n', '\0']:
                print("Erro " +  inpt[start:pos-start])
            start+=1

        pos = start-1
        curr_state = 1
        last_final = -1



    pos+=1

