import queue
from collections import defaultdict, deque
from typing import List

ip_ = [[1, 3], [0, 2], [1, 3], [0, 2]]


# build default dict
def build_adj_list(ip: List) -> defaultdict:
    ddict = defaultdict(list)
    for j in range(0, len(ip)):
        for i in range(0, len(ip[j])):
            ddict[j].append(ip[j][i])

    return ddict


def bfs(ip: List, s: int):
    graph = build_adj_list(ip)
    visited = dict()
    q = deque()
    visited[s] = 1
    q.append(s)
    parent = {}
    path = []

    while len(q) > 0:
        v = q.popleft()

        for i in graph[v]:
            if i not in visited:
                visited[i] = 1
                q.append(i)
                parent[i] = v
                path.append([v,i])
    return visited, parent, path


if __name__ == '__main__':
    print(build_adj_list(ip_))
    print(bfs(ip_, 0))