class Cinema:
	def __init__(self, longtime, name, mark):
		self.__longtime  = longtime
		self.__name = name
		self.__mark = mark
	def go(self):
		print("Зато лучше чем защитники России")
	@property
	def mark(self):
		return "The best mark, what have been anytime"
	@mark.setter 
	def mark(self, value):
		print("Фильм и так хорош")
	
	@property
	def longtime(self):
		return self.__longtime/3
	@longtime.setter
	def longtime(self, value):
		print(self.__longtime - value)

	@property
	def name(self):
		return "Тебе не надо"
	@name.setter
	def name(self, value):
		print(self.__name)


thor = Cinema(120, "Тор", "5 из 10")
print(thor.mark)

print(thor.longtime)

print(thor.name)


