# 백준 1715번
""" 카드의 개수가 A,B일 때 두 묶음을 합쳐 1개로 만들
    려면, A+B번 비교해야 한다. ex) 20장의 숫자카드와 30장의 숫자카드를 비교하려면 50번의
    비교가 필요!
    매우 많은 숫자카드 묶음이 있다고 할 때, 두 묶음씩 골라 서로 합쳐나가면, 고르는 순서에
    따라, 비교횟수가 다르다!"""

'''N개의 숫자 카드 몪음의 각각의 크기가 주어질 때, 최소한 몇 번의 비교가 필요한 지 구함!
카드묶음 수 (1줄에), 그 다음부터 카드 묶음 수에 맞게, 카드 묶음 수들의 각각 주어진다!'''

#힙 큐는 최소값 정렬로 기본세팅 되어 있다!
#큐에서 또다시 제일 작은 두 묶음을 구하고 더하는 것을 반복한다.

import sys
import heapq

n = int(input())
cards = []
for i in range(n):
    heapq.heappush(cards, int(sys.stdin.readline()))

total_cost = 0
while len(cards) > 1:
    # 가장 작은 두 카드 묶음을 꺼내서 합칩니다.
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    sum_value = a + b

    # 두 묶음을 합친 비용을 누적하고, 합친 결과를 다시 큐에 넣습니다.
    total_cost += sum_value
    heapq.heappush(cards, sum_value)

print(total_cost)
