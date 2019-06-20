class HashTable:
    """
    Tabela hash contendo os identificadores lidos
    """
    tbSize = 256
    # keywords = ("array", "asm", "begin", "case", "const", "constructor", "destructor", "div", "do", "downto", "else",
    #             "end", "file", "for", "forward", "function", "goto", "if", "implementation", "in", "inline",
    #             "interface", "label", "mod", "nil", "not", "object", "of", "or", "packed", "procedure", "program", "record",
    #             "repeat", "set", "shl", "shr", "string", "then", "to", "type", "unit", "until", "uses", "var", "while",
    #             "with", "xor", "and")
    keywords = (
    "and", "array", "begin", "case", "const", "constructor", "destructor", "div", "do", "downto", "else", "end", "file",
    "for", "function", "goto", "if", "inherited", "implementation", "in", "inline", "interface", "label", "mod", "nil",
    "not", "object", "of", "or", "packed", "procedure", "program", "record", "repeat", "set", "shl", "shr", "string",
    "then", "to", "type", "unit", "until", "uses", "var", "while", "with")

    def __init__(self):
        """
        Inicializa a hash table
        """
        self.table = [[] for _ in range(self.tbSize)]

    def hash_func(self, key):
        """
        Função de hash apresentada pela professora

        """
        hash_value = 0
        alfa = 10
        for i in range(len(key)):
            hash_value = alfa * hash_value + ord(key[i])
        hash_value = hash_value % self.tbSize
        return hash_value

    def instalar_id(self, data):
        if data.lower() in self.keywords:
            return 0

        result = self.search(data)
        if result:
            return 1
        else:
            self.table[self.hash_func(data)].append(data)
            return 1

    def search(self, key):
        bucket = self.table[self.hash_func(key)]
        for i, data in enumerate(bucket):
            if data == key:
                return 1
        return 0

    def hash_info(self):
        for _ in range(self.tbSize):
            bucket = self.table[_]
            for i, data in enumerate(bucket):
                index = self.hash_func(data)
                aux = (data, index)
                print("Identificador >> %s << armazenado no indice >> %d << da tabela" % aux)

    # def delete(self, key):
    #     bucket = self.table[self.hash_func(key)]
    #     valid_key = False
    #     for i, kd in enumerate(bucket):
    #         k, data = kd
    #         if k == key:
    #             valid_key = True
    #             break
    #     if valid_key:
    #         print("Bucket {} deletado".format(bucket[i]))
    #         del bucket[i]
    #     else:
    #         print("Chave {} nao encontrada".format(key))
