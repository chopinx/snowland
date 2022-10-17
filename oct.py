from typing import List


class Solution:
    # Problem No.207 Course Schedule
    #
    # There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an
    # array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to
    # take course ai.
    #
    # For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
    # Return true if you can finish all courses. Otherwise, return false.
    #
    # Example 1:
    #   Input: numCourses = 2, prerequisites = [[1,0]]
    #   Output: true
    #   Explanation: There are a total of 2 courses to take.
    #   To take course 1 you should have finished course 0. So it is possible.
    #
    # Example 2:
    #   Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    #   Output: false
    #   Explanation: There are a total of 2 courses to take.
    #   To take course 1 you should have finished course 0, and to take course 0 you should also have finished course
    #   1. So it is impossible.
    #
    # Constraints:
    #   1 <= numCourses <= 2000
    #   0 <= prerequisites.length <= 5000
    #   prerequisites[i].length == 2
    #   0 <= ai, bi < numCourses
    #   All the pairs prerequisites[i] are unique.
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        neighbors = [[] for _ in range(numCourses)]
        for e in prerequisites:
            neighbors[e[0]].append(e[1])
        visited = [False for _ in range(numCourses)]
        path = [False for _ in range(numCourses)]
        for v in range(numCourses):
            if not visited[v] and self.isCycle(v, neighbors, visited, path):
                return False
        return True

    def isCycle(self, v: int, neighbors: list, visited: list, path: list):
        for v2 in neighbors[v]:
            if visited[v2]:
                continue
            if path[v2]:
                return True
            path[v2] = True
            if self.isCycle(v2, neighbors, visited, path):
                return True
            path[v2] = False
        visited[v] = True
        return False
