#!/usr/bin/python
import pygame
import Modelo.Nave
import Modelo.Enemigo
import Modelo.Jugador

ANCHO_PANTALLA = 640
ALTO_PANTALLA = 480


class Dibujador(object):

	def __init__(self,universo):
		pygame.init()
		pygame.font.init()
		self.pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
		self.universo = universo
		self.dibujadorNave = DibujadorNave(self.pantalla)
		self.dibujadorEnemigo = DibujadorEnemigo(self.pantalla)
		self.dibujadorDisparo = DibujadorDisparo(self.pantalla)

	def actualizar(self):

		self.pantalla.fill(pygame.Color(0,0,0))

		dibujables = self.universo.getDibujables()
		self.dibujar(dibujables)

		pygame.display.flip()
		pygame.time.wait(10)

	def dibujar(self,dibujables):
		self.dibujarCantidadEnemigos()
		self.dibujarCantidadDisparos()
		self.dibujarVidaDelJugador()
		for dibujable in dibujables:
			self.disclaimer(dibujable)

	def disclaimer(self,dibujable):
		if type(dibujable) == Modelo.Nave.Nave:
			self.dibujadorNave.dibujar(dibujable)
		if type(dibujable) == Modelo.Enemigo.Enemigo:
			self.dibujadorEnemigo.dibujar(dibujable)
		if type(dibujable) == Modelo.Disparo.Disparo:
			self.dibujadorDisparo.dibujar(dibujable)


	def dibujarCantidadEnemigos(self):
		texto = "Enemigos = " + str(len(self.universo.manejador.enemigos))
		fuente = pygame.font.Font(None, 25)
		texto = fuente.render(texto, 1, (255, 0, 255))
		self.pantalla.blit(texto, (0, 0))

	def dibujarCantidadDisparos(self):
		texto = "Disparos = " + str(len(self.universo.jugador.nave.disparos))
		fuente = pygame.font.Font(None, 25)
		texto = fuente.render(texto, 1, (255, 0, 255))
		self.pantalla.blit(texto, (0, 20))

	def dibujarVidaDelJugador(self):
		texto = "Vida = " + str(self.universo.jugador.nave.vida)
		fuente = pygame.font.Font(None, 25)
		texto = fuente.render(texto, 1, (255, 0, 255))
		self.pantalla.blit(texto, (0, 40))


class DibujadorNave(object):
	def __init__(self,pantalla):
		self.pantalla = pantalla
		self.sprite = pygame.image.load("/home/mateo/git/Starshipy/Vista/Imagenes/spriteNave2.png")

	def dibujar(self,nave):
		x = nave.movil.posicion[0]
		y = nave.movil.posicion[1]
		ancho = nave.movil.tamano[0]
		alto = nave.movil.tamano[1]
		self.sprite = pygame.transform.scale(self.sprite, (ancho, alto))
		self.pantalla.blit(self.sprite, (x,y))


class DibujadorEnemigo(object):
	def __init__(self,pantalla):
		self.pantalla = pantalla
		self.sprite = pygame.image.load("/home/mateo/git/Starshipy/Vista/Imagenes/spriteEnemigo.png")

	def dibujar(self,enemigo):
		x = enemigo.movil.posicion[0]
		y = enemigo.movil.posicion[1]
		ancho = enemigo.movil.tamano[0]
		alto = enemigo.movil.tamano[1]
		self.sprite = pygame.transform.scale(self.sprite, (ancho, alto))
		self.pantalla.blit(self.sprite, (x,y))

class DibujadorDisparo(object):
	def __init__(self,pantalla):
		self.pantalla = pantalla

	def dibujar(self,disparo):
		ancho = disparo.movil.tamano[0]
		alto = disparo.movil.tamano[1]
		x = disparo.movil.posicion[0]
		y = disparo.movil.posicion[1]
		pygame.draw.rect(self.pantalla,pygame.Color(0,255,255),pygame.Rect((x,y), (ancho, alto)))