""" 현재 상태에서 선택할 수 있는 최선의 선택을 하게 되면, 전체 선택 
    지 중 최선의 선택이 되는 알고리즘! (부분, 부분마다 베스트 인 상태를 선택!)
    문제점: 각각마다 최선의 선택이 전체를 아우르는 최선의 선택 일 지는 보장 (X)
    => 코딩테스트에선 최적의 해, 최적의 값을 원하지만, 그리디 알고리즘은 최적의 
    해가 나올 수도 있고, 안 나올 수도 있다!
    """

'''핵심이론
  3단계 반복: '''

N,K=map(int,input().split())
A=[0]*N

for i in range(N):
    A[i]=int(input())

count=0

for i in range(N-1,-1,-1): #전달인자가 3개인 경우 이므로 N-1부터 -1전까지(=0까지) -1씩 간격을 두며 내림차순으로 반복 (큰 수부터 계산!)
    if A[i]<=K: #현재 동전이 K보다 작거나 같으면 구성에 추가!
        count += int(K/ A[i])
        K = K%A[i] #현재 동전을 사용하고 남은 금액으로 갱신

        print(count)


