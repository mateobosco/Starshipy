import pygame
import Movil
import Nave
import Enemigo

class Disparo(object):

	def __init__(self, posicion):
		# self.dueno = dueno
		posicion = posicion
		velocidad = [0,-3]
		tamano = [2,7]
		self.movil = Movil.Movil(self,posicion,tamano,velocidad)


	def moverDisparo(self):
		self.movil.moverAbajo()

	def destruirDisparo(self):
		self.movil.destruirMovil()

	def quitarDelMapa(self):
		self.movil.quitarDelMapa()


	def __str__(self):
		return "Disparo en posicion " + str(self.movil.posicion)

	def colisionarCon(self, otro):
		if (type(otro) == Nave.Nave):
			pass
		if (type(otro) == Enemigo.Enemigo):
			self.quitarDelMapa()
		if (type(otro) == Disparo):
			pass
