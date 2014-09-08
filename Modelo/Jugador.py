from Nave import Nave


class Jugador(object):
	def __init__(self):
		self.nave = Nave()
		self.vidas = 3

	def dibujar(self,pantalla):
		self.nave.dibujar(pantalla)

	def step(self):
		self.nave.step()