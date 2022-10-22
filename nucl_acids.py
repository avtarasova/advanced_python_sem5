from abc import ABC, abstractmethod
import random

class Nucl_acids(ABC):

	def __init__(self, acid):
		self.acid = acid
	def __repr__(self):
		return f"{self.acid}"
	def __str__(self):
		return f"{self.acid}"

	#общие методы для ДНК и РНК
	def is_equal(self, acid_other):
		if self.acid == acid_other.acid:
			return True
		else:
			return False


	#абстрактные методы
	@abstractmethod
	def enter_check(self):
		pass

	def index(self):
		pass

	def complement(self):
		pass

	def __add__(self, acid1):
		pass

class RNA(Nucl_acids):

	def enter_check(self):
		super().enter_check()
		nitrogen_bases = ["A", "U", "G", "C"]
		for i in self.acid:
			if i not in nitrogen_bases:
				print(Exception)
				break

	def index(self):
		super().index()
		ind = int(input())
		return self.acid[ind]

	def make_DNA(self):
		DNA_coding = []
		DNA_matrix = []
		for i in self.acid:
			if i == 'A':
				DNA_matrix.append('T')
				DNA_coding.append('A')
			elif i == 'U':
				DNA_matrix.append('A')
				DNA_coding.append('T')
			elif i == 'G':
				DNA_matrix.append('C')
				DNA_coding.append('G')
			elif i == 'C':
				DNA_matrix.append('G')
				DNA_coding.append('C')
		DNA_coding = ''.join(DNA_coding)
		DNA_matrix = ''.join(DNA_matrix)
		return DNA(acid=[DNA_coding, DNA_matrix])

	def __add__(self, acid_other):
		new_acid = self.acid + acid_other.acid
		return RNA(acid=new_acid)

	def __mul__(self, acid_other):
		if len(self.acid) >= len(acid_other.acid):
			min_len = len(acid_other.acid)
			short = self.acid[min_len:]
		else:
			min_len = len(self.acid)
			short = acid_other.acid[min_len:]

		new_acid = []
		for i in range(min_len):
			base = random.choice([self.acid[i], acid_other.acid[i]])
			new_acid.append(base)
		new_acid.append(short)
		new_acid = ''.join(new_acid)
		return RNA(acid=new_acid)


class DNA(Nucl_acids):

	def enter_check(self):
		super().enter_check()
		nitrogen_bases = ["A", "T", "G", "C"]
		for i in self.acid:
			for j in i:
				if j not in nitrogen_bases:
					print(Exception)
					break

	def index(self):
		super().index()
		ind = int(input())
		base1 = self.acid[0][ind]
		base2 = self.acid[1][ind]
		answer = [base1, base2]
		return answer

	def return_complement(self, arr: str):
		chain2 = []
		for i in arr:
			if i == 'A':
				chain2.append('T')
			elif i == 'T':
				chain2.append('A')
			elif i == 'G':
				chain2.append('C')
			elif i == 'C':
				chain2.append('G')
		chain2 = ''.join(chain2)
		return chain2


	def __add__(self, acid_other):
		chain1 = self.acid[0] + acid_other.acid[0]
		chain2 = self.acid[1] + acid_other.acid[1]
		new_dna = [chain1, chain2]
		return DNA(acid=new_dna)

	def __mul__(self, acid_other):
		if len(self.acid[0]) >= len(acid_other.acid[0]):
			min_len = len(acid_other.acid)
			short = self.acid[0][min_len:]
		else:
			min_len = len(self.acid)
			short = acid_other.acid[0][min_len:]

		new_acid = []
		for i in range(min_len):
			base = random.choice([self.acid[0][i], acid_other.acid[0][i]])
			new_acid.append(base)
		new_acid.append(short)
		chain1 = ''.join(new_acid)
		chain2 = self.return_complement(chain1)

		return DNA(acid=[chain1, chain2])


#Проверка работы кода

rna = RNA(acid="AUCCGU")
rna1 =  RNA(acid="ACGGUUUUU")
rna.enter_check()
print(rna.index())
print(rna.make_DNA())
print(rna + rna1)
print(rna * rna1)

dna = DNA(acid=["AGTCTA", "TCAGAT"])
dna1 = DNA(acid=["GAGAGAGAGATT", "CTCTCTCTCTAA"])
print(dna)
dna.enter_check()
print(dna.index())
print(dna.is_equal(rna1))
print(dna * dna1)