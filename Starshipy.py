#!/usr/bin/python
import pygame
from Vista.Dibujador import Dibujador
from Modelo.Universo import *
from Controlador.Controlador import Controlador


def main():
	pygame.init()
	dibujador = Dibujador()
	universo = Universo()

	controlador = Controlador(universo)
	while 1:

		universo.step()

		dibujador.actualizar(universo)

		controlador.aplicar()



main()