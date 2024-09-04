words = input("Enter whitespace-separated words: ").split()
unique_sorted_words = sorted(set(words))
print(" ".join(unique_sorted_words))