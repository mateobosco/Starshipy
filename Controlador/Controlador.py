#!/usr/bin/python
import pygame
import sys
from pygame.locals import *


class Controlador(object):
	def __init__(self,universo):
		self.universo = universo
		self.jugador = universo.jugador
               

	def aplicar(self):
		keys = pygame.key.get_pressed()
		if keys[K_LEFT]: self.jugador.nave.moverIzquierda()
		if keys[K_RIGHT]: self.jugador.nave.moverDerecha()
		if keys[K_DOWN]: self.jugador.nave.moverAbajo()
		if keys[K_UP]: self.jugador.nave.moverArriba()
		if keys[K_SPACE]: self.jugador.nave.disparar()

		if keys[K_ESCAPE]: self.salirJuego()

		for event in pygame.event.get():
			if event.type == QUIT:self.salirJuego()


	def salirJuego(self):
		pygame.quit()
		sys.exit()