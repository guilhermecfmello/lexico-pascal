""""
Equipe:
Guilherme Mello
Vinicius Carloto Carnelocce

"""

import sys
from scanner import AFD
from hash_symbol import HashTable
from parser import Parser

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

    identifier_table.hash_info()
    parser = Parser(scanner.scanned)
    parser.parse()
