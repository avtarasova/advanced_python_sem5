class Human(object):

	def __init__(self, name, sex, year_of_birth):
		self.name = name
		self.sex = sex
		self.year_of_birth = year_of_birth

class Movie(object):

	def __init__(self, name, director, year, country, duration, age_rating):
		self.name = name
		self.director = director
		self.year = year
		self.country = country
		self.duration = duration
		self.age_rating = age_rating

	def is_allowed(self, human):
		if (2023 - human.year_of_birth) >= self.age_rating:
			return True
		return False

class Cartoon(object):

	def __init__(self, name, director, year, country, duration, age_rating, technique):
		self.name = name
		self.director = director
		self.year = year
		self.country = country
		self.duration = duration
		self.age_rating = age_rating
		self.technique = technique

	def is_allowed(self, human):
		if (2023 - human.year_of_birth) >= self.age_rating:
			return True
		return False


class Anime(object):

	def __init__(self, name, director, year, duration,
	 age_rating,country='Япония',  technique='рисованный'):
		self.name = name
		self.director = director
		self.year = year
		self.country = country
		self.duration = duration
		self.age_rating = age_rating

	def is_allowed(self, human):
		if (2023 - human.year_of_birth) >= self.age_rating:
			return True
		return False


#Проверка работы

movie = Movie(
  name="Dune", director="Denis Villeneuve", year=2021,
  country="USA", duration=155, age_rating=13
  )

human = Human(name="Neo", sex="M", year_of_birth=1994)

print(movie.is_allowed(human)) 