

class Cliente:
	def __init__(self):
		self._n = 0
		self._i = 0
		self._s = 0

	@property
	def Normal(self):
		return self._n
	@Normal.setter
	def Normal(self, n):
		self._n+=n

	@property
	def Inferior(self):
		return self._i
	@Inferior.setter
	def Inferior(self, i):
		self._i+=i

	@property
	def Superior(self):
		return self._s
	@Superior.setter
	def Superior(self, s):
		self._s+=s

	def Total(self):
		return (self._n * 50)+(self._i * 80)+(self._s * 100)
		

	
