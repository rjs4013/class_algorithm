
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    pascal_tri = [[] for _ in range(N)]
    pascal_tri[0].append(1)
    for i in range(1, N):
        stack = pascal_tri[i-1][:]
        pascal_tri[i].append(1)
        for j in range(1, i):
            pascal_tri[i].append(stack.pop() + stack[-1])
        pascal_tri[i].append(1)

    for x in pascal_tri:
        print(*x)


