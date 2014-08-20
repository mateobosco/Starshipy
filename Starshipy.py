#!/usr/bin/python
import pygame
import sys
import random
from pygame.locals import *
import Modelo
import Vista/Dibujador
import Controlador


def main():
	pygame.init()
	dibujador = Dibujador()

	jugador = Jugador()
	manejador = ManejadorEnemigos()
	dibujables = [jugador,manejador]

	controlador = Controlador(jugador)
	while 1:

		manejador.ciclo()
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		
		dibujador.actualizar(dibujables)
		controlador.aplicar()	




main()