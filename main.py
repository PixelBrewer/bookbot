character_cout = {}


def main():
	path_to_file = "books/frankenstein.txt"
	with open(path_to_file) as f:
		text = f.read()
		print(text)
		print(" ")
		print("Number of words in the text: ", countWords(text))
		print (" ")
		countCharacters(text)
		# Convert to list of dictionaries
		char_list = [{"character": char, "count": count} for char, count in character_cout.items()]
		# Sort the list by count in descending order
		char_list.sort(key=lambda x: x["count"], reverse=True)
		print("Characters sorted by occurrence: ", char_list)

def countWords(text):
	words = text.split()
	return len(words)

def countCharacters(text):
	text = text.lower()
	for character in text:
		if character in character_cout:
			character_cout[character] += 1
		else:
			character_cout[character] = 1
	return character_cout

if __name__ == "__main__":
	main()