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

	def __str__(self):
		print "Movil en posicion " + str(self.posicion)

	# def __eq__(self,otro):
		# return (self.tamano == otro.tamano and self.posicion == otro.tamano and self.velocidad == otro.velocidad)


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


class CollisionDetectorHash(Singleton):
	def __init__(self):
		self.moviles = {}
		self.tamMax = [1,1]
		self.tabla = []
		for x in range(ANCHO_PANTALLA):
			self.tabla.append([])
			for y in range(ALTO_PANTALLA):
				self.tabla[x].append(0)

	def updateMovil(self,movil,posicionVieja):
		self.checkTamanoMax(movil)
		self.deshashearMovil(movil,posicionVieja)
		self.hashearMovil(movil)
		self.detectarColision(movil)

	def checkTamanoMax(self,movil):
		if (self.tamMax[0] < movil.tamano[0]): self.tamMax[0] = movil.tamano[0]
		if (self.tamMax[1] < movil.tamano[1]): self.tamMax[1] = movil.tamano[1]

	def hashearMovil(self,movil):
		pos = movil.posicion[0]*movil.posicion[1]
		if (pos not in self.moviles): self.moviles[pos] = [movil]
		else: self.moviles[pos].append(movil)

	def deshashearMovil(self,movil,posicionVieja):
		pos = posicionVieja[0] * posicionVieja[1]
		if (pos in self.moviles):
			if (movil in self.moviles[pos]):
				self.moviles[pos].remove(movil)
			lista = self.moviles.get(pos,0)
			if lista == []: del self.moviles[pos]

	def detectarColision(self,movil):
		inicioX = movil.posicion[0] - self.tamMax[0]
		inicioY = movil.posicion[1] - self.tamMax[1]

		for x in range(inicioX , inicioX + self.tamMax[0]):
			for y in range(inicioY , inicioY + self.tamMax[1]):
				resultado = self.checkPosicion(movil,[x,y])
				if (resultado is Movil): print "COLISION EN " + resultado.posicion


	def checkPosicion(self,movil,posicion):
		pos = posicion[0] * posicion[1]
		if pos not in self.moviles:
			return False
		else:
			lista = self.moviles.get(pos,[])
			for candidato in lista:
				if (candidato != movil):
					if (candidato.posicion == posicion): return candidato
				else: 
					return False


class CollisionDetectorTable(Singleton):
	def __init__(self):
		self.tamMax = [1,1]
		self.tabla = []
		for x in range(ANCHO_PANTALLA+100):
			self.tabla.append([])
			for y in range(ALTO_PANTALLA+100):
				self.tabla[x].append(0)

	def updateMovil(self,movil,posicionVieja):
		self.checkTamanoMax(movil)
		self.deshashearMovil(movil,posicionVieja)
		self.hashearMovil(movil)
		# self.detectarColision(movil)

	def checkTamanoMax(self,movil):
		if (self.tamMax[0] < movil.tamano[0]): self.tamMax[0] = movil.tamano[0]
		if (self.tamMax[1] < movil.tamano[1]): self.tamMax[1] = movil.tamano[1]

	def deshashearMovil(self,movil,posicionVieja):
		# pos = movil.posicion
		self.tabla[posicionVieja[0]][posicionVieja[1]] = 0

	def hashearMovil(self,movil):
		pos = movil.posicion
		self.tabla[pos[0]][pos[1]] = movil

	def detectarColision(self,movil):
		inicioX = movil.posicion[0] - self.tamMax[0]/2
		inicioY = movil.posicion[1] - self.tamMax[1]/2

		for x in range(inicioX , inicioX + self.tamMax[0]):
			for y in range(inicioY , inicioY + self.tamMax[1]):
				resultado = self.checkPosicion(movil,[x,y])
				if (resultado != 0 ): 
					print("COLISION",resultado)


	def checkPosicion(self,movil,posicion):
		resultado = self.tabla[posicion[0]][posicion[1]]
		if (resultado == movil): return False
		else: return resultado


class MovilFactory(Singleton):
	def __init__(self):
		self.moviles = []
		self.collisionDetector = CollisionDetectorTable()

	def crearMovil(self,dueno,posicion,tamano,velocidad):
		m = Movil(dueno,posicion,tamano,velocidad)
		self.moviles.append(m)
		#print (self.moviles)
		self.collisionDetector.hashearMovil(m)
		return m

	def crearMovilNave(self,dueno,posicion,tamano,velocidad):
		m = MovilNave(dueno,posicion,tamano,velocidad)
		self.moviles.append(m)
		self.collisionDetector.hashearMovil(m)
		#print (self.moviles)
		return m


class CollisionDetector(Singleton):
	
	def checkColisiones(self, moviles):
		for movil in moviles:
			for candidato in moviles:
				if (moviles.index(movil) == moviles.index(candidato)): continue
				resultado = self.colsionaCon(movil,candidato)
				if resultado : print "Colsiono el " + str(movil.dueno) + "con el" + str(candidato.dueno)


	def colsionaCon(self,movil,candidato):
		# if (movil == candidato): return False
		left = movil.posicion[0]
		right = movil.posicion[1] + movil.tamano[0]
		top = movil.posicion[1] + movil.tamano[1]
		bottom = movil.posicion[1]
		r_left = candidato.posicion[0]
		r_right = candidato.posicion[0] + candidato.tamano[0]
		r_top = candidato.posicion[1] + candidato.tamano[1]
		r_bottom = candidato.posicion[1]
		if (right >= r_left and left <= r_right and top >= r_bottom and bottom <= r_top) :return True
		return False

	def intersects(self,obj1,obj2):
		# if (obj1 == obj2):
			# return False
		if (obj1.posicion[0] + obj1.tamano[0] < obj2.posicion[0]):
			return False
		if (obj1.posicion[1] + obj1.tamano[1] < obj2.posicion[1]):
			return False
		if (obj1.posicion[0] > obj2.posicion[0] + obj2.tamano[0]):
			return False
		if (obj1.posicion[1] > obj2.posicion[1] + obj2.tamano[1]):
			return False
		return True

