#!/usr/bin/python
import pygame
import sys
import random
from pygame.locals import *

ANCHO_PANTALLA = 640
ALTO_PANTALLA = 480


class Dibujador(object):

	def __init__(self):
		pygame.init()
		self.pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

	def actualizar(self, dibujables):
		self.pantalla.fill(pygame.Color(0,0,0))

		for d in dibujables:
			d.dibujar(self.pantalla)

		pygame.display.flip()
		pygame.time.wait(10)

class Jugador(object):
	def __init__(self):
		self.nave = Nave()
		self.vidas = 3

	def dibujar(self,pantalla):
		self.nave.dibujar(pantalla)
