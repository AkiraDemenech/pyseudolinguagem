'''class vetor:
	def __init__ (self,size):
		self.__comprimento__ = size
		self.__
		self.__getitem__ = '''

booleanos =	{None:("FALSO","VERDADEIRO")}
l = False
while l < len(booleanos[None]):
	l = l.__bool__()
	booleanos[l] = booleanos[None][l]
	booleanos[booleanos[None][l]] = l
	l += 1
Logico = "LÓGICO"
Literal = 'LITERAL'
Numerico = 'NUMÉRICO'
Registro = 'REGISTRO'
Tipos = {
	None:(Numerico,Literal,Logico,Registro),
	bool:Logico,
	str:Literal,
	int:Numerico,
	float:Numerico,
	complex:Numerico,
	dict:Registro
}

def tamanho (v):
	try:
		return v.__tipo__, v.__comprimento__
	except AttributeError:
		c = []
	while type(v) == dict:
		c.append(0)
		for e in v:	
			if type(e) == str:
			#	t = Registro
				return Registro,c
			c[len(c)-1]+=1
		try:
		#	print('Camada ',len(c),e)
			v = v[e]
		except UnboundLocalError:
		#	print("Registro/Vetor vazio!")
			break
	try:
		return Tipos[type(v)],c
	except KeyError:
		return Numerico,c

def escreva (v):
	try:
		return Tipos[v]
	except Exception:
		if type(v) == bool:
			return booleanos[None][v]
		return str(v)

def copiar (v=None):
	try:
		v = v.__class__(__valor__(v))
		if v.__class__ == dict:
			for c in v:
				v[c] = copiar(v[c])
	except TypeError:
		pass
	return v

def matriz (val,ind):
	while type(ind) == tuple:#len(ind) > 1 
		if len(ind) > 1:
			val = matriz(val,ind[1:])#[0]
		ind = ind[0]
	try:
		return vetor(val,ind.start,ind.stop,ind.step)
	except AttributeError:
		return vetor(val,ind)

def vetor (v,i=0,f=None,t=None,vet=None):
	if type(v) == tuple:
		vet = vetor(var(),len(v),vet=vet)
		c = 0
		while c < len(v):
			vet[c].__valor__(v[c])
	if t == None or t == 0:
		t = 1
	if f == None:
		f = i - t
		i = 0
	if vet == None:
		vet = {}
	while i <= f:
		if not i in vet:
			vet[i] = copiar(v)
		i += t
	return vet

def __valor__ (valor):
	while var == valor.__class__:
		valor = valor.__value__
	return valor

class var:
	def __valor__ (self,v=None,permit=False):
		if permit == None:
			v = copiar(v)
		try:
			if self.__tipo__ != v.__tipo__ and not (permit or self.__varia__):
				v = None
			self.__comprimento__ = v.__comprimento__
			self.__value__ = v.__valor__()
			self.__tipo__ = v.__tipo__
		except AttributeError:
			if v == None:
				return self.__value__
			tip,com = tamanho(v)
			if tip == self.__tipo__ or permit or self.__varia__:
				self.__tipo__ = tip
				self.__value__ = v
				self.__comprimento__ = com
			else:
				return self.__value__
		if self.__tipo__ == Registro:
			for com in v:
				if type(v[com]) == dict:
					v[com] = var(v[com],False)
				self.__setattr__(com,v[com])
		return v#self.__value__

	def __str__ (self):
		if self.__tipo__ == Logico:
			return booleanos[self.__value__]
		if self.__value__.__class__ != dict:
			return self.__value__.__str__()
		if self.__varia__:
			return self.__repr__()	# se não estiverem em modo aberto, 
		return id(self).__repr__()	# Registros e Vetores devem ser printados só como ponteiros de baixo nível
	def __repr__ (self):
		return self.__class__.__name__ + '(%s)' %self.__value__.__repr__()
	def __rpow__ (self,base=1):
		return self.__value__.__rpow__(__valor__(base))
	def __pow__ (self,exp = 0):
		return self.__value__.__pow__(__valor__(exp))
	def __rxor__ (self,x = 1):
		return self.__value__.__rxor__(__valor__(x))
	def __xor__ (self, x = 0):
		return self.__value__.__xor__(__valor__(x))
	def __ror__ (self, x = False):
		return self.__value__.__ror__(__valor__(x))
	def __or__ (self, x = False):
		return self.__value__.__or__(__valor__(x))
	def __and__ (self, x = True):
		return self.__value__.__and__(__valor__(x))
	def __add__ (self, p = 0):
		return self.__value__.__add__(__valor__(p))
	def __abs__ (self):
		return self.__value__.__abs__()
	def __pos__ (self):
		return self.__value__.__pos__()
	def __neg__ (self):
		return self.__value__.__neg__()
	def __sub__ (self, s = 0):
		return self.__value__.__sub__(__valor__(s))
	def __mul__ (self, n = 1):
		return self.__value__.__mul__(__valor__(n))
	def __rfloordiv__ (self, n = 1):
		return self.__value__.__rfloordiv__(__valor__(n))
	def __floordiv__ (self, d = 1):
		return self.__value__.__floordiv__(__valor__(d))
	def __truediv__ (self, d = 1):
		return self.__value__.__truediv__(__valor__(d))
	def __rtruediv__ (self, n = 1):
		return self.__value__.__rtruediv__(__valor__(n))
	def __rdivmod__ (self, n = 1):
		return self.__value__.__rdivmod__(__valor__(n))
	def __divmod__ (self, d = 1):
		return self.__value__.__divmod__(__valor__(d))
	def __mod__ (self, m = 2):
		return self.__value__.__mod__(__valor__(m))
	def __rmod__ (self, m = 2):
		return self.__value__.__rmod__(__valor__(m))
	def __rmul__ (self, n = 1):
		return self.__value__.__rmul__(__valor__(n))
	def __rsub__ (self, s = 0):
		return self.__value__.__rsub__(__valor__(s))
	def __radd__ (self, p = 0):
		return self.__value__.__radd__(__valor__(p))
	def __rand__ (self, x = True):
		return self.__value__.__rand__(__valor__(x))
	def __rshift__ (self, x = False):
		return self.__value__.__rshift__(__valor__(x))
	def __rrshift__ (self,x = False):
		return self.__value__.__rrshift__(__valor__(x))
	def __rlshift__ (self,x = 0):
		return self.__value__.__rlshift__(__valor__(x))
	def __lshift__ (self, x = 0):
		return self.__value__.__lshift__(__valor__(x))
		
		
	def __round__ (self, c = 0):
		return self.__value__.__round__(c)
	def __trunc__ (self):
		return self.__value__.__trunc__()
	def __index__ (self):
		return self.__value__.__index__()
	def __invert__ (self):
		return self.__value__.__invert__()
		
	def __floor__ (self):
		return self.__value__.__floor__()
	def __float__ (self):
		return self.__value__.__float__()
	def __int__ (self):
		return self.__value__.__int__()
	def __bool__ (self):
		return self.__value__ != False;
	def __ceil__ (self):
		return self.__value__.__ceil__();
	def __call__ (self,*arg,**args):
		return self.__value__.__call__(*arg,**args);
		
	def __contains__ (self, c = None):
		try:
			return self.__value__.__contains__(c)
		except AttributeError:
			return False
	def __iter__ (self):
		return self.__value__.__iter__()

	def __init__ (self,valor=None,copia=True):
		if copia:
			valor = copiar(valor)
		self.__value__=valor
		self.__tipo__ =Numerico # inicialização por padrão
		self.__varia__=True # variação de tipo permitida, por enquanto
		self.__valor__(valor)
		
	
	def __getitem__ (self,i=None):
		try:
			return self.__value__.__getitem__(i)
		except KeyError as k:
			raise IndexError(('vector','matrix')[len(self.__comprimento__)>1]+' index out of range: '+str(k))
		except AttributeError:
	#	if(self.__value__.__class__ != dict):
			if self.__varia__:
				return self.__valor__(matriz(self,i))		
	def __setitem__ (self,i=None,v=None):
		self.__value__[i] = v
	
	def __ge__ (self, t = None):
		return self.__gt__(t) or self.__eq__(t)
	def __le__ (self, t = None):
		return not self.__gt__(t)
	def __lt__ (self, t = None):
		return not self.__ge__(t)
	def __ne__ (self, t = None):
		return not self.__eq__(t)
	def __eq__ (self, t = None):
		if self.__varia__ or self.__value__.__class__ != dict:
			return self.__value__.__eq__(__valor__(t))
		return self.__str__().__eq__(str(t))
	def __gt__ (self, t = None):
		if self.__value__.__class__ != dict:
			return self.__value__.__gt__(__valor__(t))
		return self.__str__().__gt__(str(t))
	
		
	
		
	
while __name__ == '__main__':#True:
	try:
		ln = input('>'*3)
		try:
			ln = eval(ln)
		except SyntaxError:
			ln = exec(ln)
		print(escreva(ln))
	except KeyboardInterrupt:
	#	if 'S' == input('Gostaria de interromper novamente e sair?')[0].upper():
		if 'S' in input('Gostaria de interromper novamente e sair?'+('<'*3)).upper():
			break
#	except RecursionError as re:
#		raise re
	except Exception as ex:
		print(' '*3 + type(ex).__name__, ex)
