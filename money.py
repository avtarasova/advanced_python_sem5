import re
import argparse

def createParser():
	parser = argparse.ArgumentParser()
	parser.add_argument ('path', type=str)
	return parser

def make_string(path):
	with open(path, encoding='utf-8') as f:
		return ''.join(f.readlines())


def regular_search(s):
	return re.finditer(r'((\d+)(\s?)(\$|₽|€))|((\$|₽|€)(\s?)(\d+))', s)


if __name__ == '__main__':
	parser = createParser()
	args = parser.parse_args()

	string = make_string(args.path)
	result = regular_search(string)

	money = []
	for match in result:
		if match.group(2) is None:
			money.append(match.group(8))
		else:
			money.append(match.group(2))

	print(*money, sep='\n')