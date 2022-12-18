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
	return re.findall(r'«[^«]*»', s)


if __name__ == '__main__':
	parser = createParser()
	args = parser.parse_args()

	string = make_string(args.path)
	result = regular_search(string)

	print(*result, sep='\n')
