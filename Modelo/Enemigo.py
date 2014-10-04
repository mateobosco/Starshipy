#!/usr/bin/python
import pygame
import random
import Movil
import Nave
import Disparo

ANCHO_PANTALLA = 640
ALTO_PANTALLA = 480


class Enemigo(object):
	def __init__(self):
		posicion = [random.randrange(0, ANCHO_PANTALLA), 0]
		tamano = [20,20]
		velocidad = [1,1]
		self.vida = 50
		self.movil = Movil.Movil(self,posicion,tamano,velocidad)

	def mover(self):
		self.movil.moverAbajo()


	def dibujar(self,pantalla):
		x = self.movil.posicion[0]
		y = self.movil.posicion[1]
		ancho = self.movil.tamano[0]
		alto = self.movil.tamano[1]
		pygame.draw.rect(pantalla,pygame.Color(0,255,255),pygame.Rect((x,y), (ancho, alto)))

	def destruirNave(self):
		self.movil.destruirMovil()

	def quitarDelMapa(self):
		self.movil.quitarDelMapa()

	def __str__(self):
		return "Enemigo en posicion " + str(self.movil.posicion)

	def colisionarCon(self, otro):
		if (type(otro) == Nave.Nave):
			self.quitarDelMapa()
		if (type(otro) == Enemigo):
			pass
		if (type(otro) == Disparo.Disparo):
			self.quitarDelMapa()

