import scanner
import token
import sys 
import gramatica
import queue
import lista

class Parser():
	div = None
	escopo = 0
	tok = token.Token()
	scan = scanner.Scanner()
	tabelaSimbolos = lista.List()

	
	def Inicializa(self,codigo):

		self.scan.getTokens(codigo)

		self.tok = self.scan.getNextToken()
		
		if self.tok.getLexema() == "int":
			self.tok = self.scan.getNextToken()

			if self.tok.getLexema() == "main":
				self.tok = self.scan.getNextToken()

				if self.tok.getLexema() == "AbreParenteses":
					self.tok = self.scan.getNextToken()

					if self.tok.getLexema() == "FechaParenteses":
						self.tok = self.scan.getNextToken()

						self.Bloco()

						if self.tok.getLexema() == "Fim":
							print ("SUCESS !!!! FIM DO PROGRAMA")
							sys.exit

						else:
							print("ERRO na linha ",self.tok.getLinha(), "coluna ",self.tok.getColuna(), "ultimo token lido: ",self.tok.getLexema(),",ERRO Fim de Arquivo !")
							sys.exit()	
					else:
						print("ERRO na linha ",self.tok.getLinha(), "coluna ",self.tok.getColuna(), "ultimo token lido: ",self.tok.getLexema(),",ERRO no fechamento de parenteses!")
						sys.exit()	
				else:
					print("ERRO na linha ",self.tok.getLinha(), "coluna ",self.tok.getColuna(), "ultimo token lido: ",self.tok.getLexema(),",ERRO, Falta Abre parenteses!")
					sys.exit()
			else:
				print("ERRO na linha ",self.tok.getLinha(), "coluna ",self.tok.getColuna(), "ultimo token lido: ",self.tok.getLexema(),",ERRO na declaração do main!")
				sys.exit()
		else:
			print("ERRO na linha ",self.tok.getLinha(), "coluna ",self.tok.getColuna(), "ultimo token lido: ",self.tok.getLexema(),",ERRO na declaração do tipo da função main!")
			sys.exit()


	def Bloco(self):

		if self.tok.getLexema()=='AbreChaves':
			self.tok = self.scan.getNextToken()
			self.escopo += 1

			while self.FirstDV ():
				self.DeclaraVariavel()

			while self.FirstComando():
				self.Comando()

			if self.tok.getLexema() == 'FechaChaves':
				self.tabelaSimbolos.remove(self.escopo)				
				self.tok = self.scan.getNextToken()
				self.escopo -= 1
				return

			else:
				print("ERRO na linha ",self.tok.getLinha(), "coluna ",self.tok.getColuna(), "ultimo token lido: ",self.tok.getLexema(),",ERRO, Falta Fecha Chaves no fim do bloco!")
				sys.exit()
		else:
			print("ERRO na linha ",self.tok.getLinha(), "coluna ",self.tok.getColuna(), "ultimo token lido: ",self.tok.getLexema(),",ERRO, Fim de Arquivo esperado!")
			sys.exit()


	def DeclaraVariavel(self):

		if self.tok.getLexema() == 'int' or self.tok.getLexema() == 'float' or self.tok.getLexema() == 'char':
			self.variavel = self.tok.getLexema()
			self.tok = self.scan.getNextToken()

			if self.tok.getSimbolo() == 'ID':

				if self.tabelaSimbolos.buscaEscopo(self.tok.getLexema(),self.escopo):
					print("ERRO na linha ",self.tok.getLinha(), "coluna ",self.tok.getColuna(), "ultimo token lido: ",self.tok.getSimbolo(),",ERRO, Variavel ja declarada!")
					sys.exit()

				else:
					self.tabelaSimbolos.insereInicio(self.tok.getLexema(),self.variavel,self.escopo)
					self.tok = self.scan.getNextToken()

				while self.tok.getLexema() == 'Virgula':
					self.tok = self.scan.getNextToken()

					if self.tok.getSimbolo() == 'ID':

						if self.tabelaSimbolos.buscaEscopo(self.tok.getLexema(),self.escopo):
							print("ERRO na linha ",self.tok.getLinha(), "coluna ",self.tok.getColuna(), "ultimo token lido: ",self.tok.getSimbolo(),",ERRO, Variavel ja declarada!")
							sys.exit()

						else:
							self.tabelaSimbolos.insereInicio(self.tok.getLexema(),self.variavel,self.escopo)
							self.tok = self.scan.getNextToken()
						

					else:
						print("ERRO na linha ",self.tok.getLinha(), "coluna ",self.tok.getColuna(), "ultimo token lido: ",self.tok.getLexema(),",ERRO, Nome da variavel nao especificada!")
						sys.exit()

				if self.tok.getLexema() == 'PontoVirgula':
					self.tok = self.scan.getNextToken()
					return True

				else:
					print("ERRO na linha ",self.tok.getLinha(), "coluna ",self.tok.getColuna(), "ultimo token lido: ",self.tok.getLexema(),",ERRO, Falta ponto e virgula apos declaração de variavel(is)!")
					sys.exit()

			else:
				print("ERRO na linha ",self.tok.getLinha(), "coluna ",self.tok.getColuna(), "ultimo token lido: ",self.tok.getLexema(),",ERRO,  Nome da variavel nao especificada!1")
				sys.exit()

		else:
			print("ERRO na linha ",self.tok.getLinha(), "coluna ",self.tok.getColuna(), "ultimo token lido: ",self.tok.getLexema(),",ERRO,  Tipo de variavel nao especificada!")
			sys.exit()



	def Comando(self):
		if self.FirstIteracao():
			self.Iteracao()
		
		elif self.FirstComandoBasico():
			self.ComandoBasico()

		elif self.tok.getLexema() == 'if':
			self.tok = self.scan.getNextToken()
			if self.tok.getLexema() == 'AbreParenteses':
				self.tok = self.scan.getNextToken()

				self.ExpRelacional()

				if self.tok.getLexema() == 'FechaParenteses':
					self.tok = self.scan.getNextToken()
					self.Comando()

					if self.tok.getLexema() == 'else':
						self.tok = self.scan.getNextToken()
						self.Comando()
						return

				else:
					print("ERRO na linha ",self.tok.getLinha(), "coluna ",self.tok.getColuna(), "ultimo token lido: ",self.tok.getLexema(),",ERRO, Falta fecha parenteses no fim do if!")
					sys.exit()

			else:
				print("ERRO na linha ",self.tok.getLinha(), "coluna ",self.tok.getColuna(), "ultimo token lido: ",self.tok.getLexema(),",ERRO, Falta abre parenteses no inicio do if!")
				sys.exit()

		else:
			print("ERRO na linha ",self.tok.getLinha(), "coluna ",self.tok.getColuna(), "ultimo token lido: ",self.tok.getLexema(),",ERRO, Comando invalido!")
			sys.exit()
				

	def Iteracao(self):

		if self.tok.getLexema() == 'while':
			self.tok = self.scan.getNextToken()

			if self.tok.getLexema() == 'AbreParenteses':
				self.tok = self.scan.getNextToken()
				self.ExpRelacional()

				if self.tok.getLexema() == 'FechaParenteses':
					self.tok = self.scan.getNextToken()
					self.Comando()
					return

				else:
					print("ERRO na linha ",self.tok.getLinha(), "coluna ",self.tok.getColuna(), "ultimo token lido: ",self.tok.getLexema(),",ERRO, Falta fechar parenteses no fim da Iteracao!")
					sys.exit()

			else:
				print("ERRO na linha ",self.tok.getLinha(), "coluna ",self.tok.getColuna(), "ultimo token lido: ",self.tok.getLexema(),",ERRO, Falta abrir parenteses apos o inicio da Iteracao!")
				sys.exit()

		if self.tok.getLexema() == 'do':
			self.tok = self.scan.getNextToken()

			self.Comando()

			if self.tok.getLexema() == 'while':
				self.tok = self.scan.getNextToken()

				if self.tok.getLexema() == 'AbreParenteses':
					self.tok = self.scan.getNextToken()

					self.ExpRelacional()

					if self.tok.getLexema() == 'FechaParenteses':
						self.tok = self.scan.getNextToken()

						if self.tok.getLexema() != 'PontoVirgula':
							print("ERRO na linha ",self.tok.getLinha(), "coluna ",self.tok.getColuna(), "ultimo token lido: ",self.tok.getLexema(),",ERRO, Falta Ponto e Virgula apos o fim da iteracao!")
							sys.exit()

						else:
							self.tok = self.scan.getNextToken()
							return

					else:
						print("ERRO na linha ",self.tok.getLinha(), "coluna ",self.tok.getColuna(), "ultimo token lido: ",self.tok.getLexema(),",ERRO, Falta fechar parenteses no fim da Iteracao!")
						sys.exit()

				else:
					print("ERRO na linha ",self.tok.getLinha(), "coluna ",self.tok.getColuna(), "ultimo token lido: ",self.tok.getLexema(),",ERRO, Falta abrirr parenteses apos o inicio da Iteracao!")
					sys.exit()

			else:
				print("ERRO na linha ",self.tok.getLinha(), "coluna ",self.tok.getColuna(), "ultimo token lido: ",self.tok.getLexema(),",ERRO, Falta comando while no fim da Iteracao!")
				sys.exit()		

	def ComandoBasico(self):
		
		if self.FirstAtribuicao():
			self.Atribuicao()

		elif self.FirstBloco():
			self.Bloco()

		else:
			print("ERRO na linha ",self.tok.getLinha(), "coluna ",self.tok.getColuna(), "ultimo token lido: ",self.tok.getLexema(),",ERRO, Comando Básico Invalido!")
			sys.exit()

	def Atribuicao(self):
		if self.tok.getSimbolo() == 'ID':

			variavel = self.tabelaSimbolos.buscar(self.tok.getLexema())
			if (self.variavel) != False:
				self.tok = self.scan.getNextToken()
			

				if self.tok.getLexema() == 'Igual':
					self.tok = self.scan.getNextToken()

					tipo = self.ExpAritimetrica()

					if tipo == 'char' and variavel != 'char':
						print("ERRO na linha ",self.tok.getLinha(), "coluna ",self.tok.getColuna(), "ultimo token lido: ",self.tok.getLexema(),",ERRO, Tipo de variaveis incompativeis! A variavel de atribuição tem que ser do tipo char")
						sys.exit()

					if (tipo == 'int'):
						if (variavel !='int' and variavel != 'float') :
							print("ERRO na linha ",self.tok.getLinha(), "coluna ",self.tok.getColuna(), "ultimo token lido: ",self.tok.getLexema(),",ERRO, Atribuicao de tipos incompativeis!A variavel de atribuição tem que ser do tipo int ou float!")
							sys.exit()

					if tipo == 'float' and variavel != 'float':
						print("ERRO na linha ",self.tok.getLinha(), "coluna ",self.tok.getColuna(), "ultimo token lido: ",self.tok.getLexema(),",ERRO, Atribuicao de tipos incompativeis! A variavel de atribuição tem que ser do tipo float")
						sys.exit()

					if tipo != 'float' and self.div == '1':
						print("ERRO na linha ",self.tok.getLinha(), "coluna ",self.tok.getColuna(), "ultimo token lido: ",self.tok.getLexema(),",ERRO, Atribuicao de tipos incompativeis! A divisao sempre resulta num tipo float")
						sys.exit()

					self.tok = self.scan.getNextToken()

					if self.tok.getLexema() == 'PontoVirgula':
						self.tok = self.scan.getNextToken()
						return
					else:
						print("ERRO na linha ",self.tok.getLinha(), "coluna ",self.tok.getColuna(), "ultimo token lido: ",self.tok.getLexema(),",ERRO, Falta Ponto e Virgula no Fim da Atribuição!")
						sys.exit()

				else:
					print("ERRO na linha ",self.tok.getLinha(), "coluna ",self.tok.getColuna(), "ultimo token lido: ",self.tok.getLexema(),",ERRO, Falta operador de atribuicao!")
					sys.exit()
			else:
				print("ERRO na linha ",self.tok.getLinha(), "coluna ",self.tok.getColuna(), "ultimo token lido: ",self.tok.getLexema(),",ERRO, Variavel não declarada!")
				sys.exit()

	def ExpRelacional(self):

		var1 = self.ExpAritimetrica()

		aux = gramatica.grammar()

		if aux.comparaOpR (self.tok.getLexema()):
			self.tok = self.scan.getNextToken()
			var2 = self.ExpAritimetrica()

			if (var1 == 'char ' and var2 == 'char') :
				return

			elif (var1 == 'int' and var2 == 'float'):
				return

			elif (var1 == 'int' and var2 == 'int') :
				return

			elif (var1 == 'float') and (var2 == 'float'):
				return

			elif (var1 == 'float' and var2 == 'int'):
				return
			else:
				print("ERRO na linha ",self.tok.getLinha(), "coluna ",self.tok.getColuna(), "ultimo token lido: ",self.tok.getLexema(),",ERRO, Tipo das variaveis incompativeis!!")
				sys.exit()

		else:
			print("ERRO na linha ",self.tok.getLinha(), "coluna ",self.tok.getColuna(), "ultimo token lido: ",self.tok.getLexema(),",ERRO, Operador Relacional invalido!")
			sys.exit()

	def ExpAritimetrica(self):

		var1 = self.Termo()	

		self.tok = self.scan.getNextToken()

		var2 = self.ExpAux()

		print (var1,var2)
		if var2 != None :
			if (var1 == 'char ' and var2 == 'char') :
				var1 = 'char'

			elif (var1 == 'int' and var2 == 'float'):
				var1 = 'float'

			elif (var1 == 'int' and var2 == 'int') :
				var1 = 'int'

			elif (var1 == 'float') and (var2 == 'float'):
				var1 = 'float'

			elif (var1 == 'float' and var2 == 'int'):
				var1 = 'float'
				
			else:
				print("ERRO na linha ",self.tok.getLinha(), "coluna ",self.tok.getColuna(), "ultimo token lido: ",self.tok.getLexema(),",ERRO, Operacao Relacional entre variaveis de tipos diferente!!")
				sys.exit()
		print (var1)
		return var1

	def ExpAux(self):

		var1 = None

		if self.tok.getLexema() == 'Soma' or self.tok.getLexema() == 'Subtracao':
			self.tok = self.scan.getNextToken()
			var1 = self.Termo()

			var2 = self.ExpAux()	

			print (var1 ,var2)
		return var1

	def Termo(self):

		var1 = self.Fator()	

		self.tok = self.scan.getNextToken()

		var2 = self.TermoAux()

		print (var1,var2)
		if var2 != None :
			if (var1 == 'char ' and var2 == 'char') :
				var1 = 'char'

			elif (var1 == 'int' and var2 == 'float'):
				var1 = 'float'

			elif (var1 == 'int' and var2 == 'int') :
				var1 = 'int'

			elif (var1 == 'float') and (var2 == 'float'):
				var1 = 'float'

			elif (var1 == 'float' and var2 == 'int'):
				var1 = 'float'
				
			else:
				print("ERRO na linha ",self.tok.getLinha(), "coluna ",self.tok.getColuna(), "ultimo token lido: ",self.tok.getLexema(),",ERRO, Operacao Relacional entre variaveis de tipos diferente!!")
				sys.exit()
		print (var1)
		return var1

	def TermoAux(self):

		var1 = None

		if self.tok.getLexema() == 'Multiplicacao' or self.tok.getLexema() == 'Divisao':
			if self.tok.getLexema() == 'Divisao':
				self.div = '1'
			else:
				self.div = '0'


			self.tok = self.scan.getNextToken()
			var1 = self.Fator()

			var2 = self.TermoAux()	

			print (var1 ,var2)
		return var1

	def Fator(self):

		if self.tok.getLexema() == 'AbreParenteses':
			self.tok = self.scan.getNextToken()

			var1 = self.ExpAritimetrica()

			if self.tok.getLexema() == 'FechaParenteses':
				self.tok = self.scan.getNextToken()
				return var1
			

		elif self.tok.getSimbolo() == 'ID':
			aux = self.tabelaSimbolos.buscar(self.tok.getLexema())

			if aux != False:
				print (aux)
				print ("1")
				return aux

			else :
				print("ERRO na linha ",self.tok.getLinha(), "coluna ",self.tok.getColuna(), "ultimo token lido: ",self.tok.getLexema(),",ERRO, Variavel Não Declarada!!!")
				sys.exit()

			
		

		elif self.tok.getSimbolo() == 'float':
			self.tok = self.scan.getNextToken()
	

		elif self.tok.getSimbolo() ==	'int':
			self.tok = self.scan.getNextToken()

	

		elif self.tok.getSimbolo() == 'char':
			self.tok = self.scan.getNextToken()
		
		else:
			print("ERRO na linha ",self.tok.getLinha(), "coluna ",self.tok.getColuna(), "ultimo token lido: ",self.tok.getLexema(),",ERRO, Fator invalido!")
			sys.exit()

		return



	
	def FirstDV(self):
		lexema = self.tok.getLexema()
		if lexema == 'int' or lexema == 'float' or lexema == 'char':
			return True
		else:
			return False

	def FirstComando(self):
		lexema = self.tok.getLexema()
		simbolo = self.tok.getSimbolo()
		if lexema == 'do' or lexema == 'while' or simbolo == 'ID' or lexema == 'if' or lexema == 'AbreChaves':
			return True
		else:
			return False

	def FirstComandoBasico(self):
		lexema = self.tok.getLexema()
		simbolo = self.tok.getSimbolo()
		if simbolo == 'ID' or lexema == 'AbreChaves':
			return True
		else:
			return False

	def FirstIteracao(self):
		lexema = self.tok.getLexema()
		if lexema == 'while' or lexema == 'do':
			return True
		else:
			return False

	def FirstAtribuicao(self):
		simbolo = self.tok.getSimbolo()
		if simbolo == 'ID':
			return True
		else:
			return False

	def FirstBloco(self):
		lexema = self.tok.getLexema()
		if lexema == 'AbreChaves':
			return True
		else:
			return False