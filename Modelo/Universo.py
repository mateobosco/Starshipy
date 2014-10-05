from ManejadorEnemigos import ManejadorEnemigos
from Jugador import Jugador
import Movil
import pygame


ANCHO_PANTALLA = 640
ALTO_PANTALLA = 480

class Universo(object):

	def __init__(self):
		self.jugador = Jugador()
		self.manejador = ManejadorEnemigos()
		self.collisionDetector = Movil.CollisionDetector()

	def step(self):
		self.manejador.ciclo()
		self.jugador.step()
		disparosJugador = self.jugador.nave.disparos
		self.stepDisparo(disparosJugador)
		lista = Movil.Movil.lista
		self.collisionDetector.checkColisiones(lista)

			
	def dibujar(self,pantalla):
		self.jugador.dibujar(pantalla)
		self.manejador.dibujar(pantalla)
		self.dibujarCantidadEnemigos(pantalla)
		self.dibujarCantidadDisparos(pantalla)
		self.dibujarVidaDelJugador(pantalla)

	def dibujarCantidadEnemigos(self,pantalla):
		texto = "Enemigos = " + str(len(self.manejador.enemigos))
		fuente = pygame.font.Font(None, 25)
		texto = fuente.render(texto, 1, (255, 0, 255))
		pantalla.blit(texto, (0, 0))

	def dibujarCantidadDisparos(self,pantalla):
		texto = "Disparos = " + str(len(self.jugador.nave.disparos))
		fuente = pygame.font.Font(None, 25)
		texto = fuente.render(texto, 1, (255, 0, 255))
		pantalla.blit(texto, (0, 20))

	def dibujarVidaDelJugador(self,pantalla):
		texto = "Vida = " + str(self.jugador.nave.vida)
		fuente = pygame.font.Font(None, 25)
		texto = fuente.render(texto, 1, (255, 0, 255))
		pantalla.blit(texto, (0, 40))

		
	def stepDisparo(self,disparos):
		for disparo in disparos:
			disparo.moverDisparo()
			aux = 0
			if disparo.movil.posicion[0] > ANCHO_PANTALLA : aux = 1
			if disparo.movil.posicion[0] < 0 : aux = 1
			if disparo.movil.posicion[1] > ALTO_PANTALLA : aux = 1
			if disparo.movil.posicion[1] < 0 : aux = 1
			if aux == 1:
				disparo.destruirDisparo()
				disparos.remove(disparo)
				disparo = 0
