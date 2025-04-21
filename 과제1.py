# 2025.4.2 파이썬 수업 프로젝트 2번째
# 콜라츠 추측, 또는 우박수
#1부터 1000까지 숫자중, 가장많은 단계를 거쳐서 1로가는 수는 무엇인가?, 가장많은 단계는 몇단계인가
#규칙: n이 짝수 -> n/2
#     n이 홀수 -> 3*n+1
#예: 5-> 16 -> 8 -> 4 -> 2 -> 1  (5단계)
import numpy as np
import time
import statistics

from p02Collatzfunc import collatz

maxnum = 100

# 리스트 방식
start = time.time()
ncountl = []

for n in range(1, maxnum):
    ncount = collatz(n)
    ncountl.append(ncount)

print("\n[리스트 방식] 통계 결과:")
print(f'최대값={max(ncountl)}')
print(f'해당숫자={ncountl.index(max(ncountl)) + 1}')
print(f'평균={statistics.mean(ncountl):.5f}')
print(f'중앙값={statistics.median(ncountl)}')
print(f'최빈값={statistics.mode(ncountl):.5f}')
print(f'표준편차={statistics.stdev(ncountl):.5f}')
end = time.time()
print(f'{end - start:.5f}초가 걸렸습니다')

# 리스트 방식: 상위 3개 출력
sorted_list = sorted(enumerate(ncountl, start=1), key=lambda x: x[1], reverse=True)
print("\n[리스트 방식] 상위 3개 단계 수:")
for i in range(3):
    print(f"{i+1}위: 숫자 {sorted_list[i][0]}, 단계 수 {sorted_list[i][1]}")

# 넘파이 방식
start = time.time()
ncounta = np.zeros(maxnum - 1)
for n in range(1, maxnum):
    ncounta[n - 1] = collatz(n)

print("\n[넘파이 방식] 통계 결과:")
print(f'최대값={np.max(ncounta)}')
print(f'해당숫자={ncounta.argmax(axis=0) + 1}')
print(f'평균={np.mean(ncounta):.5f}')
print(f'중앙값={np.median(ncounta)}')
print(f'표준편차={np.std(ncounta):.5f}')
end = time.time()
print(f'{end - start:.5f}초가 걸렸습니다')

# 넘파이 방식: 상위 3개 출력
top3_indices = np.argsort(ncounta)[-3:][::-1]
print("\n[넘파이 방식] 상위 3개 단계 수:")
for i, idx in enumerate(top3_indices):
    print(f"{i+1}위: 숫자 {idx+1}, 단계 수 {int(ncounta[idx])}")



