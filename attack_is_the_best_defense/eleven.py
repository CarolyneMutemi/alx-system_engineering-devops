#!/usr/bin/python3
"""
Finds the words in the rockyou dictionary file that have 11 letters.
"""

def find_words(file_path):
	"""
	Finds the words in the rockyou dictionary file that have 11 letters,
	and writes them to the result.txt file.
	"""
	with open(file_path, 'r') as file:
		content = file.readlines()
		with open('result.txt', 'w') as res:
			for word in content:
				if len(word) == 12:
					res.write(word)

file_name = "rockyou_1.txt"
find_words(file_name)

#print("Words containing three characters:")
#print(result)
