#!/usr/bin/python
import pygame
import Disparo
import Movil
import Enemigo

ANCHO_PANTALLA = 640
ALTO_PANTALLA = 480


class Nave(object):
	def __init__(self):
		posicion = [ANCHO_PANTALLA/2, ALTO_PANTALLA - 40]
		tamano = [10,10]
		velocidad = [5,5]
		self.vida = 100
		self.ciclo = 0
		self.disparos = []

		self.movil = Movil.MovilNave(self,posicion,tamano,velocidad)


	def moverDerecha(self):
		self.movil.moverDerecha()

	def moverIzquierda(self):
		self.movil.moverIzquierda()

	def moverArriba(self):
		self.movil.moverArriba()

	def moverAbajo(self):
		self.movil.moverAbajo()

	def quitarVida(self,danio):
		self.vida -= danio

	def dibujar(self,pantalla):
		x = self.movil.posicion[0]
		y = self.movil.posicion[1]
		ancho = self.movil.tamano[0]
		alto = self.movil.tamano[1]
		pygame.draw.rect(pantalla,pygame.Color(255,0,255),pygame.Rect((x,y), (ancho, alto)))
		for disparo in self.disparos:
			disparo.dibujar(pantalla)

	def __str__(self):
		return "Jugador en posicion " + str(self.movil.posicion)

	def disparar(self):
		if self.ciclo == 0 :
			disparo = Disparo.Disparo(self.movil.posicion+[-self.movil.tamano[0]*2,0])
			self.disparos.append(disparo)
			self.ciclo = 20

	def step(self):
		if (self.ciclo > 0): self.ciclo -= 1


	def colisionarCon(self, otro):
		if (otro is Nave):
			pass
		if (otro is Enemigo.Enemigo):
			self.quitarVida(20)
		if (otro is Disparo.Disparo):
			pass
