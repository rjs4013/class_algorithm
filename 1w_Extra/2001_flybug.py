T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = float('-inf')
    for x in range(N-M+1):
        for y in range(N-M+1):
            count=0
            for i in range(x, M+x):
                for j in range(y, M+y):
                    count += arr[i][j]
            if answer < count:
                answer = count
    print(f'#{test_case} {answer}')


