T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    turn = [list(map(int, input().split())) for _ in range(M)]
    table = [[0] * N for p in range(N)]
    a = N // 2 - 1
    di = [0, 1, 1, 1, 0, -1, -1, -1]
    dj = [1, 1, 0, -1, -1, -1, 0, 1]
    table[a][a], table[a + 1][a + 1] = 2, 2
    table[a][a + 1], table[a + 1][a] = 1, 1

    for x in turn:
        row, col, color = x[1] - 1, x[0] - 1, x[2]
        table[row][col] = color

        for k in range(8):
            ni, nj = row + di[k], col + dj[k]
            flip_list = []

            while 0 <= ni < N and 0 <= nj < N and table[ni][nj] != 0 and table[ni][nj] != color:
                flip_list.append((ni, nj))
                ni += di[k]
                nj += dj[k]

            if 0 <= ni < N and 0 <= nj < N and table[ni][nj] == color:
                for flip_i, flip_j in flip_list:
                    table[flip_i][flip_j] = color

    w_count = 0
    b_count = 0
    for i in range(N):
        for j in range(N):
            if table[i][j] == 1:
                b_count += 1
            elif table[i][j] == 2:
                w_count += 1

    print(f'#{test_case} {b_count} {w_count}')
