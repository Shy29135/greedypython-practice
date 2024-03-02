from queue import PriorityQueue
N=int(input())
plusPq=PriorityQueue()
minusPq=PriorityQueue()
one=0 #1의 갯수 카운트
zero=0 #0의 갯수 카운트

for i in range(N):
 data=int(input())
 data = int(input())
if data>1:
 plusPq.put(data*-1) #우선순위 queue는 무조건 오름차순 정렬인데, -1을 곱하면 내림차순 정렬이 되!
elif data==1:
 one+=1
elif data==0:
 zero+=1
else: minusPq.put(data)

sum=0

# 양수큐에서 큐사이즈가 1개 또는 0개가 될때까지 큰수 두개 곱해서 합에 더해줌
while plusPq.qsize()>1: 
 first=plusPq.get()*-1
 second=plusPq.get()*-1
sum+=first*second

if plusPq.qsize()>0:
 sum+=plusPq.get()*-1 #plusPq의 갯수가 홀수 일 때는 남은 1개의 갯수를 더해줘야 한다! (1이 1개 남음! (있을 경우!))

while minusPq.qsize()>1: #음수처리
 first=minusPq.get() #원래가 오름차순이므로 -값(음수)이 먼저 나온다!
 second=minusPq.get()
 sum=first*second

 if minusPq.qsize()>0: #제일 작은 1이 홀수로 1개로 남음! (1을 포함시키기 위해 다시 조건문을 씀!)
  if zero==0:
   sum+=minusPq.get()

   sum+=one #1처리 (1이 1개가 아니고 여러개일 경우 2개씩 묶는 것이나 일일이 다 더해주는 것이나 결과는 같음!)
   print(sum)
   





