# N個の数列
# Q個のクエリ
N,Q = [int(x) for x in input().split()]
# 長さLの数列A
# 変数Lは使わなかったので、index合わせと時短のため
A = []
for _ in range(N):
  A.append([int(x) for x in input().split()])
  
# クエリ
for _ in range(Q):
  s, t = [int(x) for x in input().split()]
  print(A[s-1][t])