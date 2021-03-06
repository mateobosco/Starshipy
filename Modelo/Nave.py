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
		tamano = [50,50]
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


	def __str__(self):
		return "Jugador en posicion " + str(self.movil.posicion)

	def disparar(self):
		if self.ciclo == 0 :
			deltaX = self.movil.tamano[0]
			pos1 = [self.movil.posicion[0], self.movil.posicion[1]]
			disparo1 = Disparo.Disparo(pos1)
			pos2 = [self.movil.posicion[0] + deltaX, self.movil.posicion[1]]
			disparo2 = Disparo.Disparo(pos2)
			self.disparos.append(disparo1)
			self.disparos.append(disparo2)
			self.ciclo = 10

	def step(self):
		if (self.ciclo > 0): self.ciclo -= 1


	def colisionarCon(self, otro):
		if (type(otro) == Nave):
			pass
		if (type(otro) == Enemigo.Enemigo):
			self.quitarVida(20)
		if (type(otro) == Disparo.Disparo):
			pass
