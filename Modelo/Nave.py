#!/usr/bin/python
import pygame
import Disparo

ANCHO_PANTALLA = 640
ALTO_PANTALLA = 480


class Nave(object):
	def __init__(self):
		self.posicion = [ANCHO_PANTALLA/2, ALTO_PANTALLA - 40]
		self.tamano = [10,10]
		self.velocidad = [5,5]
		self.vida = 100
		self.disparos = []

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
		self.posicion[1] -= self.velocidad[1]

	def moverAbajo(self):
		if (self.posicion[1] - self.tamano[1] > ALTO_PANTALLA):
			return
		self.posicion[1] += self.velocidad[1]

	def dibujar(self,pantalla):
		x = self.posicion[0]
		y = self.posicion[1]
		ancho = self.tamano[0]
		alto = self.tamano[1]
		pygame.draw.rect(pantalla,pygame.Color(255,0,255),pygame.Rect((x,y), (ancho, alto)))
		for disparo in self.disparos:
			disparo.dibujar(pantalla)

	def __str__(self):
		return "Jugador en posicion " + str(self.posicion)

	def disparar(self):
		disparo = Disparo.Disparo(self.posicion+[-1,0])
		self.disparos.append(disparo)
