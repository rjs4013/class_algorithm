# # memorization
# def fibo1(n):
#     # global memo
#     if n>= 2 and memo[n] == 0:
#         memo[n] = fibo1(n-1) + fibo1(n-2)
#     return memo[n]
#
# n = 7
# memo = [0] * (n+1)
# memo[0] = 0
# memo[1] = 1
# fibo1(n)
# print(memo) # [0, 1, 1, 2, 3, 5, 8, 13]
# ---------------------------------------------
# 피보나치 수 DP 적용 알고리즘
# def fibo2(n):
#     f = [0] * (n+1)
#     f[0] = 0
#     f[1] = 1
#     for i in range(2, n+1):
#         f[i] = f[i-1] + f[i-2]
#
#
#     return f[n]
# ---------------------------------------------
