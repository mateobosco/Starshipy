#!/usr/bin/python
import pygame
import sys
import random
import enemigo.py
from pygame.locals import *

ANCHO_PANTALLA = 640
ALTO_PANTALLA = 480


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
		if (self.ciclos == 60):
			self.crearEnemigo()
			self.ciclos = 0

	def dibujar(self,pantalla):
		for e in self.enemigos:
			e.dibujar(pantalla)