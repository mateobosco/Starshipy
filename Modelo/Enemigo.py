#!/usr/bin/python
import pygame
import random

ANCHO_PANTALLA = 640
ALTO_PANTALLA = 480


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