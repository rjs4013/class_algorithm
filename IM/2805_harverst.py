def harvest(N, arr, i, j, visited, lev):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    visited[i][j] = True
    total = arr[i][j]

    if lev >= N // 2:
        return total

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0<=ni<N and 0<=nj<N and not visited[ni][nj]:
            total += harvest(N, arr, ni, nj, visited, lev + 1)

    return total

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    start_i = N//2
    start_j = N//2
    visited = [[False] * N for _ in range(N)]
    print(f'#{test_case} {harvest(N, arr, start_i,start_j, visited, 0)}')