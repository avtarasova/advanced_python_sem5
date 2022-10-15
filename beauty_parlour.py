import random

class Human(object):

	def __init__(self, name, sex, year_of_birth,
		hair_length, nail_length, nail_colour='бесцветные'):
		self.name = name
		self.sex = sex
		self.year_of_birth = year_of_birth
		self.hair_length = hair_length
		self.nail_length = nail_length
		self.nail_colour = nail_colour



class Manicurist(object):

	def __init__(self, name, sex, year_of_birth):
		self.name = name
		self.sex = sex
		self.year_of_birth = year_of_birth

	def do_job(self, human):
		color = ["фиолетовый", "красный", "зеленый"]
		if human.nail_length > 0:
			human.nail_length = human.nail_length - 1
			human.nail_colour = random.choice(color)
			return human.nail_length, human.nail_colour
		return ValueError

class Hairdresser(object):

	def __init__(self, name, sex, year_of_birth):
		self.name = name
		self.sex = sex
		self.year_of_birth = year_of_birth

	def do_job(self, human):
		if human.hair_length > 0:
			return human.hair_length - 1
		return ValueError



class Barber(object):

	def __init__(self, name, sex, year_of_birth):
		self.name = name
		self.sex = sex
		self.year_of_birth = year_of_birth

	def do_job(self, human):
		if human.sex == "F":
			return ValueError
		if human.hair_length > 0:
			return human.hair_length - 1
		return ValueError

#Проверка работы

neo = Human(
  name="Neo", sex="M", year_of_birth=1964,
  hair_length=10, nail_length=2
  )
trinity = Human(
  name="Trinity", sex="F", year_of_birth=1967,
  hair_length=30, nail_length=5
  )

manicurist = Manicurist(name="Samara", sex="F", year_of_birth=1992)
barber = Barber(name="Bob", sex="M", year_of_birth=1987)



print(manicurist.do_job(neo))

print(barber.do_job(neo))

print(barber.do_job(trinity))
