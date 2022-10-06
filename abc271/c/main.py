# 単行本N冊持ってる
N = int(input())
# 持ってる単行本
A = sorted([int(x) for x in input().split()])
res = 0

if len(A)>0 and A[0] == 1:
  for n in range(1, N+1):
    # print(f'{n=}, {res=}, {A=}, {len(A)=}')
    if len(A)==0:
      break
    elif A[0] == n:
      A.pop(0)
      res = n
    elif len(A)>1:
      A = A[:-2]
      res = n 
    else:
      break
print(res)