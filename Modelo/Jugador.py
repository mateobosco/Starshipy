from Nave import *


class Jugador(object):
	def __init__(self):
		self.nave = Nave()
		self.vidas = 3

	def dibujar(self,pantalla):
		self.nave.dibujar(pantalla)