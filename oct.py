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

    # Problem No.210 Course Schedule II
    #
    # There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an
    # array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to
    # take course ai.
    #
    # For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
    # Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any
    # of them. If it is impossible to finish all courses, return an empty array.
    #
    # Example 1:
    #   Input: numCourses = 2, prerequisites = [[1,0]]
    #   Output: [0,1]
    #   Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the
    #   correct course order is [0,1].
    #
    # Example 2:
    #   Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    #   Output: [0,2,1,3]
    #   Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1
    #   and 2. Both courses 1 and 2 should be taken after you finished course 0.
    #   So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
    #
    # Example 3:
    #   Input: numCourses = 1, prerequisites = []
    #   Output: [0]
    #
    # Constraints:
    #   1 <= numCourses <= 2000
    #   0 <= prerequisites.length <= numCourses * (numCourses - 1)
    #   prerequisites[i].length == 2
    #   0 <= ai, bi < numCourses
    #   ai != bi
    #   All the pairs [ai, bi] are distinct.
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        neighbors = [[] for _ in range(numCourses)]
        for e in prerequisites:
            neighbors[e[0]].append(e[1])
        visited = [False for _ in range(numCourses)]
        path = [False for _ in range(numCourses)]
        top_list = []
        for v in range(numCourses):
            if not visited[v] and self.isCycle2(v, neighbors, visited, path, top_list):
                return []
        return top_list

    def isCycle2(self, v: int, neighbors: list, visited: list, path: list, top_list: list):
        for v2 in neighbors[v]:
            if visited[v2]:
                continue
            if path[v2]:
                return True
            path[v2] = True
            if self.isCycle2(v2, neighbors, visited, path, top_list):
                return True
            path[v2] = False
        visited[v] = True
        top_list.append(v)
        return False

    # Problem No.12 Integer to Roman.
    #
    # Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
    #   Symbol       Value
    #   I             1
    #   V             5
    #   X             10
    #   L             50
    #   C             100
    #   D             500
    #   M             1000
    # For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is
    # simply X + II. The number 27 is written as XXVII, which is XX + V + II.
    #
    # Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not
    # IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
    # The same principle applies to the number nine, which is written as IX. There are six instances where subtraction
    # is used:
    #   I can be placed before V (5) and X (10) to make 4 and 9.
    #   X can be placed before L (50) and C (100) to make 40 and 90.
    #   C can be placed before D (500) and M (1000) to make 400 and 900.
    # Given an integer, convert it to a roman numeral.
    #
    # Example 1:
    #   Input: num = 3
    #   Output: "III"
    #   Explanation: 3 is represented as 3 ones.
    #
    # Example 2:
    #   Input: num = 58
    #   Output: "LVIII"
    #   Explanation: L = 50, V = 5, III = 3.
    #
    # Example 3:
    #   Input: num = 1994
    #   Output: "MCMXCIV"
    #   Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
    #
    # Constraints:
    #   1 <= num <= 3999
    def intToRoman(self, num: int) -> str:
        symbols, halfs, i = "IXCM", "VLD", -1
        ans = ""
        while num > 0:
            d = num % 10
            num, i = num // 10, i + 1
            if d == 0:
                continue
            if d < 4:
                ans = symbols[i] * d + ans
            elif d == 4:
                ans = symbols[i] + halfs[i] + ans
            elif d < 9:
                ans = halfs[i] + symbols[i] * (d - 5) + ans
            elif d == 9:
                ans = symbols[i] + symbols[i + 1] + ans
        return ans

    # Problem No.253 Meeting Rooms II
    #
    # Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number
    # of conference rooms required.
    #
    # Example 1:
    #   Input: intervals = [[0,30],[5,10],[15,20]]
    #   Output: 2
    #
    # Example 2:
    #   Input: intervals = [[7,10],[2,4]]
    #   Output: 1
    #
    # Constraints:
    #   1 <= intervals.length <= 10^4
    #   0 <= starti < endi <= 10^6
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])
        ans, ep = 0, 0
        for t in starts:
            if t >= ends[ep]:
                ans -= 1
                ep += 1
            ans += 1
        return ans
