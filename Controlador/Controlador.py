#!/usr/bin/python
import pygame
import sys
import random
from pygame.locals import *

ANCHO_PANTALLA = 640
ALTO_PANTALLA = 480

class Controlador(object):
	def __init__(self,jugador):
		self.jugador = jugador

	def aplicar(self):
		keys = pygame.key.get_pressed()
		if keys[K_LEFT]: self.jugador.nave.moverIzquierda()
		elif keys[K_RIGHT]: self.jugador.nave.moverDerecha()
		elif keys[K_DOWN]: self.jugador.nave.moverAbajo()
		elif keys[K_UP]: self.jugador.nave.moverArriba()
