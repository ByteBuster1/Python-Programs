
string = input("Enter a string: ")
length = len(string)
substring = "country" in string
words = string.split()
word_count = {word: words.count(word) for word in set(words)}
print(f"Length of the string: {length}")
print(f"Substring 'country' found: {substring}")
print(f"Word occurrences: {word_count}")