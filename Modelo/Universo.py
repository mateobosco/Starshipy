from ManejadorEnemigos import ManejadorEnemigos
from Jugador import Jugador


ANCHO_PANTALLA = 640
ALTO_PANTALLA = 480

class Universo(object):

	def __init__(self):
		self.jugador = Jugador()
		self.manejador = ManejadorEnemigos()

	def step(self):
		self.manejador.ciclo()
		disparosJugador = self.jugador.nave.disparos
		self.stepDisparo(disparosJugador)
			
			
	def dibujar(self,pantalla):
		self.jugador.dibujar(pantalla)
		self.manejador.dibujar(pantalla)
		
	def stepDisparo(self,disparos):
		for disparo in disparos:
			disparo.moverDisparo()
			aux = 0
			if disparo.posicion[0] > ANCHO_PANTALLA : aux = 1
			if disparo.posicion[0] < 0 : aux = 1
			if disparo.posicion[1] > ALTO_PANTALLA : aux = 1
			if disparo.posicion[1] < 0 : aux = 1
			if aux == 1:
				disparos.remove(disparo)
				disparo = 0