from typing import List


def grep(pattern: str, file: str) -> List[str]:

	answer = []

	with open(file, "r") as f:
		text = f.read().split('\n')
		for line in text:
			if pattern in line:
				answer.append(line)

	return answer
