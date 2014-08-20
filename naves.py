import pygame
import sys
import random
from pygame.locals import *


ANCHO_PANTALLA = 640
ALTO_PANTALLA = 480


class Nave(object):
	def __init__(self):
		self.posicion = [ANCHO_PANTALLA/2, ALTO_PANTALLA - 40]
		self.tamano = [10,10]
		self.velocidad = [5,5]
		self.vida = 100

	def moverDerecha(self):
		if (self.posicion[0] + self.tamano[0] > ANCHO_PANTALLA):
			return
		self.posicion[0] += self.velocidad[0]

	def moverIzquierda(self):
		if (self.posicion[0] - self.tamano[0] < 0):
			return
		self.posicion[0] -= self.velocidad[0]

	def moverArriba(self):
		if (self.posicion[1] + self.tamano[1] < 0):
			return
		self.posicion[1] += self.velocidad[1]

	def moverAbajo(self):
		if (self.posicion[1] - self.tamano[1] > ALTO_PANTALLA):
			return
		self.posicion[1] += self.velocidad[1]

	def dibujar(self,pantalla):
		x = self.posicion[0]
		y = self.posicion[1]
		ancho = self.tamano[0]
		alto = self.tamano[1]
		pygame.draw.rect(pantalla,pygame.Color(0,0,255),pygame.Rect((x,y), (ancho, alto)))

	def __str__(self):
		return "Jugador en posicion " + str(self.posicion)

class Enemigo(object):
	def __init__(self):
		self.posicion = [random.randrange(0, ANCHO_PANTALLA), 0]
		self.tamano = [5,5]
		self.vida = 50
		self.velocidad = [1,1]

	def mover(self):
		self.posicion[1] += self.velocidad[1]


	def dibujar(self,pantalla):
		x = self.posicion[0]
		y = self.posicion[1]
		ancho = self.tamano[0]
		alto = self.tamano[1]
		pygame.draw.rect(pantalla,pygame.Color(0,255,255),pygame.Rect((x,y), (ancho, alto)))

	def __str__(self):
		return "Jugador en posicion " + str(self.posicion)

class ManejadorEnemigos(object):
	enemigos = []
	ciclos = 0

	def mover(self):
		for enemigo in self.enemigos:
			enemigo.mover()
			if (enemigo.posicion[1] > ALTO_PANTALLA):
				self.enemigos.remove(enemigo)
				enemigo = 0

	def crearEnemigo(self):
		ene = Enemigo()
		self.enemigos.append(ene)

	def ciclo(self):
		self.mover()
		self.ciclos += 1
		print(self.ciclos)
		if (self.ciclos == 10):
			self.crearEnemigo()
			self.ciclos = 0

	def dibujar(self,pantalla):
		for e in self.enemigos:
			e.dibujar(pantalla)



def main():
	pygame.init()
	pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
	clock = pygame.time.Clock()

	jugador = Nave()
	manejador = ManejadorEnemigos()


	while 1:

		manejador.ciclo()
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		pantalla.fill(pygame.Color(0,0,0))
		jugador.dibujar(pantalla)
		manejador.dibujar(pantalla)
		pygame.display.flip()
		pygame.time.wait(10)




main()