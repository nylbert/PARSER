class grammar:
	preservada = ("main","if","else","while","do","for","int","float","char")
	especial = "AbreParenteses","FechaParenteses","AbreChaves","FechaChaves","PontoVirgula","Virgula"
	oparitmetico = "Soma","Subtracao","Multiplicacao","Divisao","Igual"
	oprelacional = "MenorQ","MaiorQ","MenorIgualQ","MaiorIgualQ","Comparacao","Desigual"	
	
	
	def comparaReservada(self,palavra):
		for i in range (len(self.preservada)):
			if self.preservada[i] == palavra:
				return True

		return False

	def comparaOpR(self,palavra):
		for i in range (len(self.preservada)):
			if self.oprelacional[i] == palavra:
				return True

		return False