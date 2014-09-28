ANCHO_PANTALLA = 640
ALTO_PANTALLA = 480

class Movil(object):
	lista = []
	def __init__(self,dueno,posicion,tamano,velocidad):
		self.dueno = dueno
		self.posicion = posicion
		self.tamano = tamano
		self.velocidad = velocidad
		self.posicionEnLista = len(Movil.lista)
		Movil.lista.append(self)
		print self.posicionEnLista

	def moverDerecha(self):
		self.posicion[0] += self.velocidad[0]

	def moverIzquierda(self):
		self.posicion[0] -= self.velocidad[0]

	def moverArriba(self):
		self.posicion[1] -= self.velocidad[1]

	def moverAbajo(self):
		self.posicion[1] += self.velocidad[1]

	def destruirMovil(self):
		Movil.lista.remove(self)

	def quitarDelMapa(self):
		self.posicion = [2000,2000]

	def __str__(self):
		print "Movil en posicion " + str(self.posicion)




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


class Singleton(object):
	instance = None
	def __new__(cls, *args, **kargs): 
		if cls.instance is None:
			cls.instance = object.__new__(cls, *args, **kargs)
			return cls.instance
		else: return cls.instance


class CollisionDetector(Singleton):
	
	def checkColisiones(self, moviles):
		for movil in moviles:
			for candidato in moviles:
				# if (moviles.index(movil) == moviles.index(candidato)): continue
				resultado = self.colsionaCon(movil,candidato)
				if resultado : 
					print "Colsiono el " + str(movil.dueno) + " con el " + str(candidato.dueno)

					#Double Dispatching
					movil.dueno.colisionarCon(candidato)
					candidato.dueno.colisionarCon(movil)
				

	def colsionaCon(self,obj1,obj2):
		if (obj1 == obj2):
			return False
		if (obj1.posicion[0] + obj1.tamano[0] < obj2.posicion[0]):
			return False
		if (obj1.posicion[1] + obj1.tamano[1] < obj2.posicion[1]):
			return False
		if (obj1.posicion[0] > obj2.posicion[0] + obj2.tamano[0]):
			return False
		if (obj1.posicion[1] > obj2.posicion[1] + obj2.tamano[1]):
			return False
		return True
