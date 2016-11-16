class Token():
	simbolo = " "
	lexema = " "
	linha = 0
	coluna = 0

	def setSimbolo(self,simbolo):
		self.simbolo = simbolo

	def setLexema(self,lexema):
		self.lexema = lexema

	def setLinha(self,linha):
		self.linha = linha

	def setColuna(self,coluna):
		self.coluna = coluna

	def getSimbolo(self):
		return self.simbolo

	def getLexema(self):
		return self.lexema

	def getLinha(self):
		return self.linha

	def getColuna(self):
		return self.coluna
