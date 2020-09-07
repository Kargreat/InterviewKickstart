from collections import defaultdict, deque
from typing import List

ip_ = [[1, 2], [2], [0, 3], [3]]


def build_adj_list(ip: List):
    ddict = defaultdict(list)
    for i in range(0, len(ip)):
        for j in range(0, len(ip[i])):
            ddict[i].append(ip[i][j])

    return ddict


def dfs(ip: List, s: int):
    graph = build_adj_list(ip)

    visited = dict()
    visited[s] = 1

    parent = dict()
    parent[s] = s

    circular_parent = list()
    
    path = []

    q = deque()
    q.append(s)
    while len(q) > 0:
        v = q.pop()
        for i in graph[v]:
            if parent[v] == i:
                circular_parent.append([v, i])
            if i not in visited:
                visited[i] = 1
                parent[i] = v
                path.append([v, i])

                q.append(i)
    print(f'visited: {visited}')
    print(f'parent: {parent}')
    print(f'circular_parent: {circular_parent}')
    print(f'path: {path}')
    return visited, parent, path, circular_parent


if __name__ == '__main__':
    print(build_adj_list(ip_))
    print(dfs(ip_, 0))
