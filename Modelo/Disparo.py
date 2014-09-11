import pygame
import Movil

class Disparo(object):

	def __init__(self, posicion):
# 		self.dueno = dueno
		posicion = posicion
		velocidad = [0,-1]
		tamano = [10,10]
		self.movil = Movil.Movil(self,posicion,tamano,velocidad)


	def moverDisparo(self):
		self.movil.moverAbajo()

	def dibujar(self,pantalla):
		ancho = self.movil.tamano[0]
		alto = self.movil.tamano[1]
		x = self.movil.posicion[0]
		y = self.movil.posicion[1]
		pygame.draw.rect(pantalla,pygame.Color(0,255,255),pygame.Rect((x,y), (ancho, alto)))


	def __str__(self):
		return "Disparo en posicion " + str(self.movil.posicion)