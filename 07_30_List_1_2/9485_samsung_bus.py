'''
버스 정류장 번호 1~5000
버스 노선은 N개, i번째 버스 노선은 번호가 Ai 이상, Bi 이하인 모든 정류장만을 다님.
p개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지 구해라...

주어지는 변수 -> N, Ai, Bi, P, Cj

예시 -> 1번 버스는 1번, 2번, 3번 버정
        2번 버스는 2번, 3번, 4번, 5번 버정
        1 2 2 1 1
'''
import sys
sys.stdin = open("s_input.txt","r")

def bus_route(N, bus_stop, P, C):
    blank_bus = [0] * P
    for i in range(P):
        count = 0
        for bus in bus_stop:
            if bus[0] <= C[i] <= bus[1]:
                count += 1
        blank_bus[i] = count

    answer = ' '.join(map(str, blank_bus))

    print(f'#{test_case} {answer}')
    print()

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    bus_stop = [list(map(int,input().split())) for _ in range(N)]
    P = int(input())
    C = [int(input()) for _ in range(P)]

    bus_route(N, bus_stop, P, C)

# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     line_list = []
#     for i in range(N):
#         line_list.append(list(map(int, input().split())))  # [A, B]
#
#     P = int(input())
#     cnt_list = [0] * P
#     for j in range(P):
#         C = int(input())
#         cnt = 0
#         for line in line_list:
#             if line[0] <= C <= line[1]:
#                 cnt += 1
#         cnt_list[j] = cnt
#
#     print(f'#{tc}', *cnt_list)