def maze(N, start, arr):
    di = [0, 1 ,0, -1]
    dj = [1, 0, -1, 0]
    invited = [[0] * N for _ in range(N)]
    for x in range(N-1,0,-1):
        for y in range(N):
            if arr[x][y] == '2':
                invited[x][y] = 1

                break

    for i in range(N-1, -1, -1):
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0<=ni<N and 0<=nj<N:
                    if arr[ni][nj] == '0':







T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    print(arr)
    maze(N,1,arr)