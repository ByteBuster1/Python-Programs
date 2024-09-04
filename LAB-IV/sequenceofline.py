lines = []
while True:
    line = input("Enter a line (or type 'done' to finish): ")
    if line.lower() == 'done':
        break
    lines.append(line.upper())
print("\n".join(lines))