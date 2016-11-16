import scanner
import token
import sys
import parser

local = sys.argv[1]

arquivo = open(local,"r")
codigo = arquivo.read()
arquivo.close()


aux = parser.Parser()
aux.Inicializa(codigo)
