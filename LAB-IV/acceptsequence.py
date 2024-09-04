words = input("Enter whitespace-separated words: ").split()
digit_words = [word for word in words if word.isdigit()]
print(digit_words)