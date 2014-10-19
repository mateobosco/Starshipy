#!/usr/bin/python
import pygame
import Modelo.Nave
import Modelo.Enemigo
import Modelo.Jugador

ANCHO_PANTALLA = 640
ALTO_PANTALLA = 480


class Dibujador(object):

	def __init__(self,universo):
		pygame.init()
		pygame.font.init()
		self.pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
		self.universo = universo
		self.dibujadorNave = DibujadorNave()

	def actualizar(self):

		self.pantalla.fill(pygame.Color(0,0,0))

		self.universo.dibujar(self.pantalla)

		dibujables = self.universo.getDibujables()
		self.dibujar(dibujables)

		pygame.display.flip()
		pygame.time.wait(10)

	def dibujar(self,dibujables):
		for dibujable in dibujables:
			self.disclaimer(dibujable)

	def disclaimer(self,dibujable):

		if type(dibujable) == Modelo.Nave:
			self.dibujadorNave.dibujar(self.pantalla,nave)



class DibujadorNave(object):
	def __init__(self):
		self.sprite = pygame.image.load("/home/mateo/git/Starshipy/Vista/Imagenes/spriteNave2.png")


	def dibujar(self,pantalla,nave):
		x = nave.movil.posicion[0]
		y = nave.movil.posicion[1]
		ancho = nave.movil.tamano[0]
		alto = nave.movil.tamano[1]
		self.sprite = pygame.transform.scale(self.sprite, (ancho, alto))
		pantalla.blit(self.sprite, (x,y))
		for disparo in nave.disparos:
			disparo.dibujar(pantalla)