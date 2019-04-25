class SymbolsTab:
    def __init__(self):
        self.dic = {"array":26,"asm":27,"begin":28,
        "case":29, "const":30, "constructor": 31, "destructor":32,
        "div":33, "do":34, "downto": 35, "else": 36, "End": 37,
        "File": 38, "For": 39, "Foward": 40, "Function": 41, "Goto": 42,
        "If": 43, "implementation": 44, "In": 45, "inline": 46,
        "interface": 47, "Label": 48, "mod": 49, "nil": 50, "not": 51,
        "object": 52, "of": 53, "or": 54, "packed": 55, "procedure": 56,
        "program": 57, "record": 58, "repeat": 59, "set": 60, "shl": 61,
        "shr": 62, "string": 63, "then": 64, "to": 65, "type": 66,
        "unit": 67, "until": 68, "uses": 69, "var": 70, "while": 71,
        "with": 72, "xor": 73, "and": 74}


    #Acessa a tabela de simbolos, se a string existir na mesma e
    #for uma palavra-chave, retorna seu token , caso nao seja
    #palavra-chave retorna 1
    #Se a string nao existir na tabela, adiciona e retorna 0
    def instalar_id(self, string):
        if string in self.dic:
            # print("Existe no dic")
            return self.dic[string]
        else:
            # print("Nao existe no dic")
            self.dic[string] = 1
            return 0


    #Procura na tabela a ocorrencia de string
    #Caso exista e seja uma palavra-chave, retorna seu token,
    #caso nao seja uma palavra-chave e exista, retorna 1
    #Caso nao exista na tabela, retorna 0
    # def obter_token(self, string):
    #     if(string in self.dic):
    #         return self.dic["string"]
    #     else:
    #         return -1
