# Алгоритм
# 1 класс Человек базовый
# 2 создаем два класса зомби и игрок которые 
# 	будут наследовать класс Человек
# 	Создаем метод attack() для вызова драки
# 	Игра на рекорд(Кто убьет больше зомби)

class Human:
	def __init__(self,name, health, damage):
		self.health = health
		self.damage = damage
		self.name = name
	def attack(self, target):
		print(self.name, "нанес ", self.damage, "урона", target.name)
		target.health -= self.damage
		print("После атаки у ", target.name, "осталось", target.health)

class Heros(Human):
	def __init__(self, name, health, damage, medical_box):
		super().__init__(name, health, damage)
		self.medical_box = medical_box

	def heal(self):
		print("Вы воспользовались аптечкой")
		if self.medical_box<= 0:
			self.health  += 10
			self.medical_box-= 1
		else:
			print("Больше нет аптечек")
	def оружие список инпут

	def shoop(self):
		print("Путин, не воруй")

class Zombi(Human):
	def dead__shoop(self):
		print("Хайль Лизгины")

def game():
	eldar = Heros("Даша-следопыт", 150, 20, 50)
	zombo = Zombi("Ватник", 30, 20)
	count_kill = 0 
	while True:
		if eldar.health > 0:
			eldar.attack(zombo)
			input()
			zombo.attack(eldar)
			if zombo.health <= 0:
				zombo.dead__shoop()
				count_kill += 1
				zombo = Zombi("Ватник", 30, 20)
			else:
				zombo.attack(eldar)
			print(eldar.name, "Воспользуйтесь аптечкой")
			i = int(input("1. Да, 2. Нет"))
			if i == 1:
				eldar.heal()
		else:
			print("Слава Навальному. Я сделал все, что смог")
			print("Я успел убить", count_kill , "ватников")
			break
game()


gun = {
	"вилы": 10 
	"" 
}