


ANCHO_PANTALLA = 640
ALTO_PANTALLA = 480

class Movil(object):
	def __init__(self,posicion,tamano,velocidad):
		self.posicion = posicion
		self.tamano = tamano
		self.velocidad = velocidad

	def moverDerecha(self):
		self.posicion[0] += self.velocidad[0]

	def moverIzquierda(self):
		self.posicion[0] -= self.velocidad[0]

	def moverArriba(self):
		self.posicion[1] -= self.velocidad[1]

	def moverAbajo(self):
		self.posicion[1] += self.velocidad[1]


class MovilNave(Movil):

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

class MovilFactory(object):
	instance = None
	def __new__(cls, *args, **kargs): 
		if cls.instance is None:
			cls.instance = object.__new__(cls, *args, **kargs)
			return cls.instance
		else: return cls.instance

	def __init__(self):
		self.moviles = []

	def crearMovil(self,posicion,tamano,velocidad):
		m = Movil(posicion,tamano,velocidad)
		self.moviles.append(m)
		return m

	def crearMovilNave(self,posicion,tamano,velocidad):
		m = MovilNave(posicion,tamano,velocidad)
		self.moviles.append(m)
		return m
