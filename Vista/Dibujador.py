#!/usr/bin/python
import pygame

ANCHO_PANTALLA = 640
ALTO_PANTALLA = 480


class Dibujador(object):

	def __init__(self):
		pygame.init()
		pygame.font.init()
		self.pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

	def actualizar(self, universo):

		

		self.pantalla.fill(pygame.Color(0,0,0))

		universo.dibujar(self.pantalla)

		pygame.display.flip()
		pygame.time.wait(10)
