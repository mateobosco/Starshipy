import pygame

class Disparo(object):

	def __init__(self, posicion):
# 		self.dueno = dueno
		self.posicion = posicion
		self.velocidad = [0,-1]
		self.tamano = [10,10]

	def moverDisparo(self):
		self.posicion[1] += self.velocidad[1]

	def dibujar(self,pantalla):
		ancho = self.tamano[0]
		alto = self.tamano[1]
		x = self.posicion[0]
		y = self.posicion[1]
		pygame.draw.rect(pantalla,pygame.Color(0,255,255),pygame.Rect((x,y), (ancho, alto)))


	def __str__(self):
		return "Disparo en posicion " + str(self.posicion)