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