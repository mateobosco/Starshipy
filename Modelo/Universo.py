from ManejadorEnemigos import * 
from Jugador import *
#from Disparo import *
import Disparo
import time


class Universo(object):

	def __init__(self):
		self.jugador = Jugador()
		self.manejador = ManejadorEnemigos()

	def step(self):
		self.manejador.ciclo()
		disparosJugador = self.jugador.nave.disparos
		for disparo in disparosJugador:
			disparo.moverDisparo()

	def dibujar(self,pantalla):
		self.jugador.dibujar(pantalla)
		self.manejador.dibujar(pantalla)