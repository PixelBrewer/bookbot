def count_words(file_contents):
	words = file_contents.split()
	return len(words)

def count_characters(file_contents):
	chars = {}
	for char in file_contents.lower():
		if char in chars:
			chars[char] += 1
		else:
			chars[char] = 1
	return chars

def print_report(words, characters):
	print("\nCharacter counts:")
	for char, count in sorted (characters.items()):
		if char.isalpha():
			print(f"The '{char}': character appears {count} times")
		else:
			# Ignore non-alphabetic characters
			continue

def main():
	with open("books/frankenstein.txt") as f:
		file_contents = f.read()
		words = count_words(file_contents)
		characters = count_characters(file_contents)
		print_report(words, characters)


main()