# Kosaraju's algorithm
# A linear time algorithm to find the strongly-connected components of a directed graph.
from typing import List


def kosaraju(v_num: int, edges: 'List[List[int]]') -> list:
    top_list, visited = [], [False for _ in range(v_num)]
    ins, outs = [[] for _ in range(v_num)], [[] for _ in range(v_num)]
    for e in edges:
        ins[e[1]].append(e[0])
        outs[e[0]].append(e[1])
    for i in range(v_num):
        top_list = visit(i, top_list, visited, outs)
        print(top_list)
    ans = [-1 for _ in range(v_num)]
    for i in top_list:
        ans = assign(i, i, ins, ans)
    return ans


def visit(v: int, top_list: list, visited: list, outs: 'List[List[int]]') -> list:
    if visited[v]:
        return top_list
    visited[v] = True
    for v2 in outs[v]:
        top_list = visit(v2, top_list, visited, outs)
    top_list = [v] + top_list
    print(top_list)
    return top_list


def assign(v: int, root: int, ins: 'List[List[int]]', ans: list) -> list:
    if ans[v] >= 0:
        return ans
    ans[v] = root
    for v2 in ins[v]:
        ans = assign(v2, root, ins, ans)
    return ans
