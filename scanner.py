import token
import queue
import gramatica
import sys

class Scanner():
	fila = queue.Fila()


	def getNextToken(self):	
		return self.fila.retira()

	def VerificaFila(self):
		return self.fila.vazia()

	def getTokens(self, codigo):
		pos = 0
		linha = 1
		coluna = 0
		quebralinha=chr(10)
		
		if len(codigo)==0:
				print ("Arquivo vazio!\n")
				sys.exit()
		
		while  pos < len(codigo)-1:
			while codigo[pos].isspace() and pos<len(codigo)-1:
				if codigo[pos]==' ':
					pos+=1
					coluna+=1
				elif codigo[pos]=='\t':
					coluna+=4
					pos+=1
				else:
					linha+=1
					coluna=0
					pos+=1

			if codigo[pos].isalpha() or codigo[pos]=='_':
				posInicio = pos
				pos+=1
				colunaInicio=coluna
				coluna+=1
				while (codigo[pos].isalpha() or codigo[pos].isdigit() or codigo[pos] == '_'):
					pos+=1
					coluna+=1


				t = token.Token()
				t.setLexema(codigo[posInicio : pos])
				t.setLinha(linha)
				t.setColuna(colunaInicio)

				aux = gramatica.grammar()
				if aux.comparaReservada(codigo[posInicio : pos])==True:
					t.setSimbolo("preservada")
				else:
					t.setSimbolo("ID")

				self.fila.insere(t)

			if codigo[pos].isdigit():
				posInicio = pos
				pos += 1
				colunaInicio=coluna
				coluna+=1
				while codigo[pos].isdigit():
					pos+= 1
					coluna+=1
				if codigo[pos]=='.':
					pos += 1
					coluna+=1
					if codigo[pos].isdigit():
						pos += 1
						coluna+=1
						while codigo[pos].isdigit():
							pos+= 1
							coluna+=1
						t = token.Token()
						t.setLexema(codigo[posInicio : pos])
						t.setSimbolo("float")
						t.setLinha(linha)
						t.setColuna(colunaInicio)
						self.fila.insere(t)
					else:
						print("ERRO na linha ",linha, "coluna ",colunaInicio, "ultimo token lido: ", codigo[posInicio:pos+1],"Formato Float Invalido!")
						sys.exit()
				else:
					t = token.Token()
					t.setLexema(codigo[posInicio : pos])
					t.setSimbolo("int")
					t.setLinha(linha)
					t.setColuna(colunaInicio)
					self.fila.insere(t)

			aspas=chr(39)
			if codigo[pos] == aspas :
				posInicio = pos
				pos += 1
				colunaInicio=coluna
				coluna+=1
				if codigo[pos].isalpha() or codigo[pos].isdigit():
					pos+= 1
					coluna+=1
					if codigo[pos] == aspas :
						pos+= 1
						coluna+=1
						t = token.Token()
						t.setLexema(codigo[posInicio : pos])
						t.setSimbolo("char")
						t.setLinha(linha)
						t.setColuna(colunaInicio)
						self.fila.insere(t)
					else:
						print ("ERRO na linha ",linha, "coluna ",colunaInicio, "ultimo token lido:",codigo[posInicio:pos+1]," Formato Char Invalido!")
						sys.exit()

				else:
					print ("ERRO na linha ",linha, "coluna ",colunaInicio, "ultimo token lido:",codigo[posInicio:pos+1]," Char Invalido!")
					sys.exit()

			elif codigo[pos]=='.':
				posInicio= pos
				colunaInicio= coluna
				pos+= 1
				coluna+=1
				if codigo[pos].isdigit():
					pos += 1
					coluna+=1
					while codigo[pos].isdigit():
						pos += 1
						coluna+=1
					t = token.Token()
					t.setLexema(codigo[posInicio : pos])
					t.setSimbolo("float")
					t.setLinha(linha)
					t.setColuna(colunaInicio)
					self.fila.insere(t)
				else:
					print("ERRO na linha ",linha, "coluna ",colunaInicio, "ultimo token lido: ", codigo[posInicio:pos+1],"Formato Float Invalido!")
					sys.exit()			

			elif codigo[pos]=='(':
				pos+= 1
				coluna+=1
				t = token.Token()
				t.setLexema("AbreParenteses")
				t.setSimbolo("especial")
				t.setLinha(linha)
				t.setColuna(coluna-1)
				self.fila.insere(t)

			elif codigo[pos]==')':
				pos+= 1
				coluna+=1
				t = token.Token()
				t.setLexema("FechaParenteses")
				t.setSimbolo("especial")
				t.setLinha(linha)
				t.setColuna(coluna-1)
				self.fila.insere(t)

			elif codigo[pos]==';':
				pos+= 1
				coluna+=1
				t = token.Token()
				t.setLexema("PontoVirgula")
				t.setSimbolo("especial")
				t.setLinha(linha)
				t.setColuna(coluna-1)
				self.fila.insere(t)

			elif codigo[pos]==',':
				pos+= 1
				coluna+=1
				t = token.Token()
				t.setLexema("Virgula")
				t.setSimbolo("especial")
				t.setLinha(linha)
				t.setColuna(coluna-1)
				self.fila.insere(t)

			elif codigo[pos]=='{':
				pos+= 1
				coluna+=1
				t = token.Token()
				t.setLexema("AbreChaves")
				t.setSimbolo("especial")
				t.setLinha(linha)
				t.setColuna(coluna-1)
				self.fila.insere(t)

			elif codigo[pos]=='}':
				pos+= 1
				coluna+=1
				t = token.Token()
				t.setLexema("FechaChaves")
				t.setSimbolo("especial")
				t.setLinha(linha)
				t.setColuna(coluna-1)
				self.fila.insere(t)

			elif codigo[pos]=='>':
				pos+= 1
				coluna+=1
				if codigo[pos]=='=':
					pos+= 1
					coluna+=1
					t = token.Token()
					t.setLexema("MaiorIgualQ")
					t.setSimbolo("oprelacional")
					t.setLinha(linha)
					t.setColuna(coluna-1)
					self.fila.insere(t)
				else:
					t = token.Token()
					t.setLexema("MaiorQ")
					t.setSimbolo("oprelacional")
					t.setLinha(linha)
					t.setColuna(coluna-1)
					self.fila.insere(t)

			elif codigo[pos]=='<':
				pos+= 1
				coluna+=1
				if codigo[pos]=='=':
					pos+= 1
					coluna+=1
					t = token.Token()
					t.setLexema("MenorIgualQ")
					t.setSimbolo("oprelacional")
					t.setLinha(linha)
					t.setColuna(coluna-1)
					self.fila.insere(t)
				else:
					t = token.Token()
					t.setLexema("MenorQ")
					t.setSimbolo("oprelacional")
					t.setLinha(linha)
					t.setColuna(coluna-1)
					self.fila.insere(t)

			elif codigo[pos]=='!':
				pos+= 1
				coluna+=1
				if codigo[pos]=='=':
					pos+= 1
					coluna+=1
					t = token.Token()
					t.setLexema("Desigual")
					t.setSimbolo("oprelacional")
					t.setLinha(linha)
					t.setColuna(coluna-1)
					self.fila.insere(t)
				else:
					print ("ERRO na linha ",linha, "coluna ",coluna,"Ultimo token lido: ",codigo[pos]+1, ",Exclamacao sozinha (nao sucedida por '=')")
					sys.exit()

			elif codigo[pos]=='=':
				pos+= 1
				coluna+=1
				if codigo[pos]=='=':
					pos+= 1
					coluna+=1
					t = token.Token()
					t.setLexema("Comparacao")
					t.setSimbolo("oprelacional")
					t.setLinha(linha)
					t.setColuna(coluna-1)
					self.fila.insere(t)
				else:
					t = token.Token()
					t.setLexema("Igual")
					t.setSimbolo("oparitmetico")
					t.setLinha(linha)
					t.setColuna(coluna-1)
					self.fila.insere(t)

			elif codigo[pos]=='+':
				pos+= 1
				coluna+=1
				t = token.Token()
				t.setLexema("Soma")
				t.setSimbolo("oparitmetico")
				t.setLinha(linha)
				t.setColuna(coluna-1)
				self.fila.insere(t)

			elif codigo[pos]=='-':
				pos+= 1
				coluna+=1
				t = token.Token()
				t.setLexema("Subtracao")
				t.setSimbolo("oparitmetico")
				t.setLinha(linha)
				t.setColuna(coluna-1)
				self.fila.insere(t)

			elif codigo[pos]=='*':
				pos+= 1
				coluna+=1
				t = token.Token()
				t.setLexema("Multiplicacao")
				t.setSimbolo("oparitmetico")
				t.setLinha(linha)
				t.setColuna(coluna-1)
				self.fila.insere(t)

			elif codigo[pos]=='/':
				pos+= 1
				coluna+=1

				if codigo[pos]=='*':
					pos+=1
					coluna+=1
					while pos < len(codigo)-1:

						if codigo[pos]==quebralinha:
							linha+=1
							coluna=0

						elif codigo[pos] == '\t':
							coluna+=4

						elif codigo[pos] == '*' and codigo[pos+1] == '/':
							pos+=2
							coluna+=2
							break
						pos+= 1
						coluna+=1

					if pos == len(codigo):
						print ("ERRO na linha ",linha, "coluna ",coluna, "ultimo token lido: ",codigo[pos], " Erro no fechamento de comentario!")
						sys.exit()

				elif codigo[pos]=='/':
					pos+= 1
					coluna+=1
					while codigo[pos]!=quebralinha:
						pos+= 1
						coluna+=1

				else:
					t = token.Token()
					t.setLexema("Divisao")
					t.setSimbolo("oparitmetico")
					t.setLinha(linha)
					t.setColuna(coluna-1)
					self.fila.insere(t)

			else:
				if codigo[pos].isspace()==False:
					print ("ERRO na linha ",linha, "coluna ",coluna,"ultimo token lido: ",codigo[pos], " caracter invalido!")
					sys.exit()
		t = token.Token()
		t.setLexema("Fim")
		t.setSimbolo(" de Arquivo")
		t.setLinha(linha)
		t.setColuna(coluna-1)
		self.fila.insere(t)