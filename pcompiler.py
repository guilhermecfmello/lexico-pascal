""""
Equipe:
Guilherme Mello
Vinicius Carloto Carnelocce

"""
import sys

from scanner import AFD

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("Modo de uso: python pcompiler.py arquivo")
        sys.exit(1)

    try:
        file = open(sys.argv[1])
    except IOError:
        print("Erro na abertura do arquivo")
        sys.exit(1)

    scanner = AFD()

    with file:
        scanner.scan(file)
