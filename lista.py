import sys

class Node:
   # Declaracao dos atributos desta Classe
   tipo = None
   nome = None
   escopo = None
   nextNode = None
   # Fim declaracao


   # Nesta secao encontram-se os metodos para acesso
   # dos respectivos atributos
   def __init__(self,nome, tipo, escopo):
      self.tipo = tipo
      self.nome = nome
      self.escopo = escopo
      self.proximo = None

   def getTipo(self):
      return(self.tipo)
   def getNome(self):
      return(self.nome)
   def getEscopo(self):
      return(self.escopo)
   def getProximo(self):
      return(self.proximo)   
   def setTipo(self, tipo):
      self.tipo = setTipo
   def setNome(self, nome):
      self.nome = nome
   def setEscopo(self, escopo):
      self.escopo = escopo
   def setProximo(self, proximo):
      self.proximo = proximo
   # Fim declaracao Metodos Get e Set   


class List:

   def __init__(self):
      self.firstNode = None
      self.lastNode = None

   def insereInicio(self, nome, tipo, escopo):
      newNode = Node(nome,tipo,escopo)
      
      if self.isEmpty():
         self.firstNode = self.lastNode = newNode

      else:
         newNode.setProximo(self.firstNode)
         self.firstNode = newNode

   # Metodo para remocao
   def remove(self,escopo):
      while self.firstNode.getEscopo() == escopo:

         if self.firstNode == self.lastNode:
            self.firstNode = self.lastNode = None
            sys.exit()
         else:
            self.firstNode = self.firstNode.getProximo()
         

   def buscaEscopo(self,nome, escopo):
      temp = self.firstNode
      while temp != None:
         if temp.getNome() == nome and temp.getEscopo() == escopo :
            return True
         else:
            temp = temp.getProximo()
      return False

   def buscar(self,nome):
      temp = self.firstNode
      
      while temp != None:
         if temp.getNome() == nome:
            return temp.getTipo()
         else:
            temp = temp.getProximo()
      return False      

   def isEmpty(self):
      if self.firstNode == None:
         return True
      else:
         return False