def print_number_pattern(N):
    arr = [[0] * N for _ in range(N)]
    num = 1
    for i in range(N // 2 + 1):
        for j in range(i, N - i):
            arr[i][j] = num
            num += 1
        for j in range(i + 1, N - i):
            arr[j][N - i - 1] = num
            num += 1
        for j in range(N - i - 2, i - 1, -1):
            arr[N - i - 1][j] = num
            num += 1
        for j in range(N - i - 2, i, -1):
            arr[j][i] = num
            num += 1
    for row in arr:
        print(' '.join(map(str, row)))

print_number_pattern(4)