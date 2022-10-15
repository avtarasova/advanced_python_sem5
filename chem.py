class Acid(object):

	def __init__(self, name="acid"):
		self.name = name

	def __repr__(self):
		return f"{self.name}"
	def __str__(self):
		return f"{self.name}"

	def __add__(self, other):
		if other.name == "base":
			return Salt(), Water()
		elif other.name == "salt":
			return Salt(), Acid()
		elif other.name == "phenolphthalein":
			return Phenolphthalein(colour = "бесцветный")
		elif other.name == "litmus":
			return Litmus(colour = "красный")
		elif other.name == "MethylOrange":
			return MethylOrange(colour = "розовый")
		else:
			return TypeError


class Base(object):

	def __init__(self, name="base"):
		self.name = name

	def __repr__(self):
		return f"{self.name}"
	def __str__(self):
		return f"{self.name}"

	def __add__(self, other):
		if other.name == "acid":
			return Salt(), Water()
		elif other.name == "salt":
			return Salt(), Base()
		elif other.name == "phenolphthalein":
			return Phenolphthalein(colour = "малиновый")
		elif other.name == "litmus":
			return Litmus(colour = "синий")
		elif other.name == "methylorange":
			return MethylOrange(colour = "желтый")
		else:
			return TypeError

class Water(object):

	def __init__(self, name="water"):
		self.name = name

	def __repr__(self):
		return f"{self.name}"
	def __str__(self):
		return f"{self.name}"

class Salt(object):

	def __init__(self, name="salt"):
		self.name = name

	def __repr__(self):
		return f"{self.name}"
	def __str__(self):
		return f"{self.name}"

	def __add__(self, other):
		if other.name == "acid":
			return Salt(), Acid()
		elif other.name == "base":
			return Salt(), Base()
		else:
			return TypeError

class Phenolphthalein(object):

	def __init__(self, name="phenolphthalein", colour="бесцветный"):
		self.name = name
		self.colour = colour

	def __repr__(self):
		return f"{self.name}, {self.colour}"
	def __str__(self):
		return f"{self.name}({self.colour})"

	def __add__(self, other):
		if other.name == "acid":
			self.colour = "бесцветный" 
			return Phenolphthalein(colour="бесцветный")
		elif other.name == "base":
			self.colour = "малиновый" 
			return Phenolphthalein(colour="малиновый")
		else:
			return TypeError

class MethylOrange(object):

	def __init__(self, name="methylorange", colour="бесцветный"):
		self.name = name
		self.colour = colour

	def __repr__(self):
		return f"{self.name}, {self.colour}"
	def __str__(self):
		return f"{self.name}({self.colour})"

	def __add__(self, other):
		if other.name == "acid":
			self.colour = "розовый" 
			return MethylOrange(colour="розовый")
		elif other.name == "base":
			self.colour = "желтый" 
			return MethylOrange(colour="желтый")
		else:
			return TypeError

class Litmus(object):

	def __init__(self, name="litmus", colour="бесцветный"):
		self.name = name
		self.colour = colour

	def __repr__(self):
		return f"{self.name}, {self.colour}"
	def __str__(self):
		return f"{self.name}({self.colour})"

	def __add__(self, other):
		if other.name == "acid":
			self.colour = "красный" 
			return Phenolphthalein(colour="красный")
		elif other.name == "base":
			self.colour = "синий" 
			return Phenolphthalein(colour="синий")
		else:
			return TypeError


