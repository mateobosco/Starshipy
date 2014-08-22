#!/usr/bin/python
import pygame
import sys
import random
from pygame.locals import *
from Vista.Dibujador import *
from Modelo.Universo import *
from Controlador.Controlador import * 


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