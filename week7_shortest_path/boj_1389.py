'''
입력
첫째 줄에 유저의 수 N (2 ≤ N ≤ 100)과 친구 관계의 수 M (1 ≤ M ≤ 5,000)이 주어진다. 
둘째 줄부터 M개의 줄에는 친구 관계가 주어진다. 친구 관계는 A와 B로 이루어져 있으며, A와 B가 친구라는 뜻이다. 
A와 B가 친구이면, B와 A도 친구이며, A와 B가 같은 경우는 없다. 
친구 관계는 중복되어 들어올 수도 있으며, 친구가 한 명도 없는 사람은 없다. 
또, 모든 사람은 친구 관계로 연결되어져 있다. 사람의 번호는 1부터 N까지이며, 두 사람이 같은 번호를 갖는 경우는 없다.

출력
첫째 줄에 BOJ의 유저 중에서 케빈 베이컨의 수가 가장 작은 사람을 출력한다. 
그런 사람이 여러 명일 경우에는 번호가 가장 작은 사람을 출력한다.
'''

import sys
data = sys.stdin.readline().rstrip().split()
N = int(data[0])
M = int(data[1])

graph = []
for _ in range(M):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    graph.append((A, B))

inf = 1000000000
dist = [[inf] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    dist[i][i] = 0
    
for A, B in graph:
    dist[A][B] = 1
    dist[B][A] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

personal_sum = []
for i in range(1, N + 1):
    personal_sum.append(sum(dist[i][1:]))

min_value = min(personal_sum)
answer = personal_sum.index(min_value) + 1

print(answer)