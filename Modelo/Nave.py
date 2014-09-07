#!/usr/bin/python
import pygame
import Disparo
import Movil

ANCHO_PANTALLA = 640
ALTO_PANTALLA = 480


class Nave(object):
	def __init__(self):
		posicion = [ANCHO_PANTALLA/2, ALTO_PANTALLA - 40]
		tamano = [10,10]
		velocidad = [5,5]
		self.vida = 100
		self.disparos = []

		m = Movil.MovilFactory()
		self.movil = m.crearMovilNave(posicion,tamano,velocidad)

	def moverDerecha(self):
		self.movil.moverDerecha()

	def moverIzquierda(self):
		self.movil.moverIzquierda()

	def moverArriba(self):
		self.movil.moverArriba()

	def moverAbajo(self):
		self.movil.moverAbajo()

	def dibujar(self,pantalla):
		x = self.movil.posicion[0]
		y = self.movil.posicion[1]
		ancho = self.movil.tamano[0]
		alto = self.movil.tamano[1]
		pygame.draw.rect(pantalla,pygame.Color(255,0,255),pygame.Rect((x,y), (ancho, alto)))
		for disparo in self.disparos:
			disparo.dibujar(pantalla)

	def __str__(self):
		return "Jugador en posicion " + str(self.posicion)

	def disparar(self):
		disparo = Disparo.Disparo(self.movil.posicion+[-1,0])
		self.disparos.append(disparo)
