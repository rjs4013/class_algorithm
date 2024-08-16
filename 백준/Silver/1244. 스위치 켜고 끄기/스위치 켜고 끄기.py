def onoff(numbers_switch, status, student_num, gen):
    for i in range(student_num):
        if gen[i][0] == 1:  # 남학생
            num = gen[i][1]
            for k in range(num, len(status) + 1, num):
                status[k - 1] = 1 - status[k - 1]  # 상태 반전
        else:  # 여학생
            num = gen[i][1] - 1
            left = num
            right = num
            while left > 0 and right < len(status) - 1 and status[left - 1] == status[right + 1]:
                left -= 1
                right += 1
            for j in range(left, right + 1):
                status[j] = 1 - status[j]
    return status




switch_N = int(input())
status = list(map(int,input().split()))
student_num = int(input())
gen = [list(map(int, input().split())) for _ in range(student_num)]
numbers_switch = []
for q in range(1, switch_N+1):
    numbers_switch.append(q)
answer = ' '.join(map(str,onoff(numbers_switch, status, student_num, gen)))
for i in range(0, len(answer), 40):
    print(answer[i:i+40])