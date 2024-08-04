def print_pattern(N):
    for i in range(1, N+1):
        print(' ' * (N-i) + '/' + ' ' * (2*i-2) + '\\')
    for i in range(1, N+1):
        print(' ' * (N-i) + '/' + '_' * (2*i-2) + '\\')

print(print_pattern(int(input("Enter value for n: "))))