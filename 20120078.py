# n = 정점의 개수
# m = 간선의 개수
# start = 시작점
n, m, start = map(int, input().split())

a = []
for i in range(n+1):
    a.append([])

for i in range(m):
    u, v = map(int, input().split())
    
    a[u].append(v)
    a[v].append(u)

for i in range(1, n+1):
    a[i].sort()

check = [False] * (n+1)

# 모든정점을 한번씩 방문
def dfs(a, check, now):
    # a : 인접리스트
    # check: 방문했는지 안했는지 확인하는 리스트
    # now: 현재 방문한 정점
    if check[now]:
        return
    check[now] = True
    print(now, end=' ')
    for nextVertex in a[now]:
        # now -> nextVertex
        dfs(a, check, nextVertex)

dfs(a, check, start)
print()

def bfs(a, start):
    # start 정점에서 시작
    check = [False] * (n+1)
    queue = []
    queue.append(start)
    check[start] = True
    while queue:
        now = queue[0]
        queue.pop(0)
        print(now, end=' ')
        for nextVertex in a[now]:
            # now -> nextVertex
            if check[nextVertex] == True:
                continue
            queue.append(nextVertex)
            check[nextVertex] = True

bfs(a, start)
print()