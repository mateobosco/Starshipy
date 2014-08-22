from ManejadorEnemigos import * 
from Jugador import *
from Disparo import *

class Universo(object):

	def __init__(self):
		self.jugador = Jugador()
		self.manejador = ManejadorEnemigos()

	def step(self):
		self.manejador.ciclo()
		disparosJugador = self.jugador.nave.disparos
		for disparo in disparosJugador:
			if (disparo is Disparo): 
				disparo.mover()
				print disparosJugador.index(disparo)

	def dibujar(self,pantalla):
		self.jugador.dibujar(pantalla)
		self.manejador.dibujar(pantalla)