def find_numbers():
    results = []
    for num in range(1000, 2001):
        if num % 7 == 0 and num % 5 != 0:
            results.append(num)
    print("Numbers divisible by 7 but not a multiple of 5 between 1000 and 2000 are:")
    print(results)
find_numbers()