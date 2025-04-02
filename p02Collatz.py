# 2025.4.2 파이썬 수업 프로젝트 2번째
# 콜라츠 추측, 또는 우박수
#1부터 1000까지 숫자중, 가장많은 단계를 거쳐서 1로가는 수는 무엇인가?, 가장많은 단계는 몇단계인가
#규칙: n이 짝수 -> n/2
#     n이 홀수 -> 3*n+1
#예: 5-> 16 -> 8 -> 4 -> 2 -> 1  (5단계)

n =

# 단계의 갯수를 셀것
# n을 1부터 99까지 변화하면서, 각각의 단계 수를 출력할 것
# 그중 가장 큰 수를 찾을 것

while n!=1:
    if n % 2 == 1:
        n = 3 * n + 1
    else:
        n = n / 2
    print(n)
