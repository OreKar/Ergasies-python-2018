import sys
from random import *


def is_in_lex(lex, word):
	for i in range(100):
		s = ''
		for k in range(100):
			s += lex[i][k]
		if word in s:
			return True
	for j in range(100):
		s = ''
		for k in range(100):
			s += lex[k][j]
		if word in s:
			return True
	return False


if __name__ == "__main__":
	square = []
	for i in range(100):
		square.append([])
		for j in range(100):
			square[i].append(chr(randint(65,90)))
	file_name = sys.argv[1]
	words_list = []
	with open(file_name) as f:
		for line in f:

			if is_in_lex(square,line.rstrip()):
				words_list.append(line)
	print("Οι λέξεις που υπάρχουν είναι:")
	for w in words_list:
		print(w)
