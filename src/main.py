def count_words(file_contents):
	words = file_contents.split()
	return len(words)

def count_characters(file_contents):
	file_contents_lower = file_contents.lower()
	c_dict = {}
	for c in file_contents_lower:
		c_dict[c] += 1

def main():
	with open("books/frankenstein.txt") as f:
		file_contents = f.read()
		words = count_words(file_contents)
		characters = count_characters(file_contents)
		print (f"Words: {words}, Characters: {characters}")


main()