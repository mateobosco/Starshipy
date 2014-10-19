from ManejadorEnemigos import ManejadorEnemigos
from Jugador import Jugador
import Movil
import pygame


ANCHO_PANTALLA = 640
ALTO_PANTALLA = 480

class Universo(object):

	def __init__(self):
		self.jugador = Jugador()
		self.manejador = ManejadorEnemigos()
		self.collisionDetector = Movil.CollisionDetector()

	def step(self):
		self.manejador.ciclo()
		self.jugador.step()
		disparosJugador = self.jugador.nave.disparos
		self.stepDisparo(disparosJugador)
		lista = Movil.Movil.lista
		self.collisionDetector.checkColisiones(lista)
		
	def stepDisparo(self,disparos):
		for disparo in disparos:
			disparo.moverDisparo()
			aux = 0
			if disparo.movil.posicion[0] > ANCHO_PANTALLA : aux = 1
			if disparo.movil.posicion[0] < 0 : aux = 1
			if disparo.movil.posicion[1] > ALTO_PANTALLA : aux = 1
			if disparo.movil.posicion[1] < 0 : aux = 1
			if aux == 1:
				disparo.destruirDisparo()
				disparos.remove(disparo)
				disparo = 0

	def getDibujables(self):
		dibujables = []
		dibujables.append(self.jugador)
		dibujables.append(self.jugador.nave)
		dibujables += self.manejador.enemigos
		dibujables += self.jugador.nave.disparos
		return dibujables