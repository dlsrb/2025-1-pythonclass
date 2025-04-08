# 2025.4.2 파이썬 수업 프로젝트 2번째
# 콜라츠 추측, 또는 우박수
#1부터 1000까지 숫자중, 가장많은 단계를 거쳐서 1로가는 수는 무엇인가?, 가장많은 단계는 몇단계인가
#규칙: n이 짝수 -> n/2
#     n이 홀수 -> 3*n+1
#예: 5-> 16 -> 8 -> 4 -> 2 -> 1  (5단계)
#
from itertools import count

# 단계의 갯수를 셀것 - done
# n을 1부터 99까지 변화하면서, 각각의 단계 수를 출력할 것
# 그중 가장 큰 수를 찾을 것
# n = 97: 118번만에 1로 도달
# n = 73: 115번만에 1로 도달

maxvalue = -100
maxvaluen = -100
max2value = 0
max2valuen = 0
max3value = 0
max3valuen = 0

for n in range(1,1000):
    # print(f'{n=}')
    ncount = 0
    i = n # n과 i를 따로둬 n은 초기값만 존재
    #nsave = n #n 값을 바꾸기전에 초기값

    while i!=1:
        if i % 2 == 1:
            i = 3 * i + 1
        else:
            i = i / 2
        ncount = ncount + 1



    print(f'{ncount}')
    if maxvalue < ncount:
        max3value = max2value
        max3valuen =max2valuen
        max2value = maxvalue
        max2valuen = maxvaluen
        maxvalue = ncount
        maxvaluen = n
    elif ncount > max2value:
        max2value = ncount
        max2valuen = n
    elif ncount > max3value:
        max3value = ncount
        max3valuen = n
print(f'{maxvalue=}, {maxvaluen=}')
print(f'{max2value=}, {max2valuen=}')
print(f'{max3value=},{max3valuen=}')