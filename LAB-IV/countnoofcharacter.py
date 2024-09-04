string = input("Enter a string: ")
char_count = {char: string.count(char) for char in set(string)}
for char, count in char_count.items():
    print(f"{char},{count}")