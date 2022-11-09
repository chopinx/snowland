import heapq
import random
from collections import Counter, defaultdict
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Problem No.588 Design a data structure that simulates an in-memory file system.
#
# Implement the FileSystem class:
#
# FileSystem() Initializes the object of the system.
#
# List<String> ls(String path)
# If path is a file path, returns a list that only contains this file's name.
# If path is a directory path, returns the list of file and directory names in this directory.
# The answer should in lexicographic order.
#
# void mkdir(String path) Makes a new directory according to the given path. The given directory path does not exist.
# If the middle directories in the path do not exist, you should create them as well.
#
# void addContentToFile(String filePath, String content)
# If filePath does not exist, creates that file containing given content.
# If filePath already exists, appends the given content to original content.
#
# String readContentFromFile(String filePath) Returns the content in the file at filePath.
#
# Example 1:
#   Input
#   ["FileSystem", "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
#   [[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]
#   Output
#   [null, [], null, null, ["a"], "hello"]
#
#   Explanation
#   FileSystem fileSystem = new FileSystem();
#   fileSystem.ls("/");                         // return []
#   fileSystem.mkdir("/a/b/c");
#   fileSystem.addContentToFile("/a/b/c/d", "hello");
#   fileSystem.ls("/");                         // return ["a"]
#   fileSystem.readContentFromFile("/a/b/c/d"); // return "hello"
#
# Constraints:
#   1 <= path.length, filePath.length <= 100
#   path and filePath are absolute paths which begin with '/' and do not end with '/' except that the path is just "/".
#   You can assume that all directory names and file names only contain lowercase letters, and the same names will not exist in the same directory.
#   You can assume that all operations will be passed valid parameters, and users will not attempt to retrieve file content or list a directory or file that does not exist.
#   1 <= content.length <= 50
#   At most 300 calls will be made to ls, mkdir, addContentToFile, and readContentFromFile.
#
# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
class FileSystem:

    def __init__(self):
        self.root = {}

    def _parse_path(self, path: str) -> list:
        if path == "/":
            return []
        return path[1:].split("/")

    def ls(self, path: str) -> List[str]:
        name_list = self._parse_path(path)
        curr_dir = self.root
        for name in name_list:
            curr_dir = curr_dir[name]
        if isinstance(curr_dir, str):
            return [name_list[-1]]
        return sorted(curr_dir.keys())

    def mkdir(self, path: str) -> None:
        name_list = self._parse_path(path)
        curr_dir = self.root
        for name in name_list:
            if name in curr_dir:
                continue
            curr_dir[name] = {}
            curr_dir = curr_dir[name]

    def addContentToFile(self, filePath: str, content: str) -> None:
        name_list = self._parse_path(filePath)
        curr_dir = self.root
        for name in name_list[:-1]:
            curr_dir = curr_dir[name]
        filename = name_list[-1]
        if filename not in curr_dir:
            curr_dir[filename] = content
        else:
            curr_dir[filename] += content

    def readContentFromFile(self, filePath: str) -> str:
        name_list = self._parse_path(filePath)
        curr_dir = self.root
        for name in name_list[:-1]:
            curr_dir = curr_dir[name]
        filename = name_list[-1]
        return curr_dir[filename]


# Problem No.1603 Design Parking System
#
# Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: big, medium, and small,
# with a fixed number of slots for each size.
#
# Implement the ParkingSystem class:
#
# ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class. The number of slots for
# each parking space are given as part of the constructor.
# bool addCar(int carType) Checks whether there is a parking space of carType for the car that wants to get into the
# parking lot. carType can be of three kinds: big, medium, or small, which are represented by 1, 2, and 3 respectively.
# A car can only park in a parking space of its carType. If there is no space available, return false, else park the car
# in that size space and return true.
#
# Example 1:
#   Input
#   ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
#   [[1, 1, 0], [1], [2], [3], [1]]
#   Output
#   [null, true, true, false, false]
#   Explanation
#   ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);
#   parkingSystem.addCar(1); // return true because there is 1 available slot for a big car
#   parkingSystem.addCar(2); // return true because there is 1 available slot for a medium car
#   parkingSystem.addCar(3); // return false because there is no available slot for a small car
#   parkingSystem.addCar(1); // return false because there is no available slot for a big car. It is already occupied.
#
# Constraints:
#   0 <= big, medium, small <= 1000
#   carType is 1, 2, or 3
#   At most 1000 calls will be made to addCar
class ParkingSystem:
    # Your ParkingSystem object will be instantiated and called as such:
    # obj = ParkingSystem(big, medium, small)
    # param_1 = obj.addCar(carType)

    def __init__(self, big: int, medium: int, small: int):
        self.slot_left = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.slot_left[carType - 1] > 0:
            self.slot_left[carType - 1] -= 1
            return True
        return False


# Problem No.295 Find Median from Data Stream
#
# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value
# and the median is the mean of the two middle values.
#
# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:
#
# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be
# accepted.
#
# Example 1:
#   Input
#   ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
#   [[], [1], [2], [], [3], []]
#   Output
#   [null, null, null, 1.5, null, 2.0]
#
#   Explanation
#   MedianFinder medianFinder = new MedianFinder();
#   medianFinder.addNum(1);    // arr = [1]
#   medianFinder.addNum(2);    // arr = [1, 2]
#   medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
#   medianFinder.addNum(3);    // arr[1, 2, 3]
#   medianFinder.findMedian(); // return 2.0
#
# Constraints:
#   -10^5 <= num <= 10^5
#   There will be at least one element in the data structure before calling findMedian.
#   At most 5 * 10^4 calls will be made to addNum and findMedian.
#
#
# Follow up:
#   If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
#   If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
#
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
class MedianFinder:
    def __init__(self):
        self.low_list = []
        self.high_list = []

    def _push_high(self, num: int):
        heapq.heappush(self.high_list, num)

    def _push_low(self, num: int):
        heapq.heappush(self.low_list, 0 - num)

    def _pop_high(self) -> int:
        return heapq.heappop(self.high_list)

    def _pop_low(self) -> int:
        return 0 - heapq.heappop(self.low_list)

    def addNum(self, num: int) -> None:
        if len(self.high_list) == 0 and len(self.low_list) == 0:
            self._push_high(num)
            return
        if num > self.high_list[0]:
            self._push_high(num)
        else:
            self._push_low(num)
        if len(self.high_list) > len(self.low_list) + 1:
            self._push_low(self._pop_high())
        elif len(self.low_list) > len(self.high_list):
            self._push_high(self._pop_low())

    def findMedian(self) -> float:
        if len(self.high_list) > len(self.low_list):
            return self.high_list[0]
        return (self.high_list[0] - self.low_list[0]) / 2


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

    # Problem No.273 Integer to English Words
    #
    # Convert a non-negative integer num to its English words representation.
    #
    # Example 1:
    #   Input: num = 123
    #   Output: "One Hundred Twenty Three"
    #
    # Example 2:
    #   Input: num = 12345
    #   Output: "Twelve Thousand Three Hundred Forty Five"
    #
    # Example 3:
    #   Input: num = 1234567
    #   Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
    #
    # Constraints:
    #   0 <= num <= 2^31 - 1
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        units = ['Billion', 'Thousand', 'Million']
        words = []
        i = 0
        while num > 0:
            reminder = num % 1000
            sub_list = self.smallToWords(reminder)
            if len(sub_list) > 0:
                words = sub_list + ([units[i % 3]] if i > 0 else []) + words
            i += 1
            num //= 1000
        return ' '.join(words).strip()

    def smallToWords(self, num: int) -> list:
        """
        Convert a small number to its English words representation. 
        :param num: 0 <= num < 1000
        :return: 
        """
        hundred_word = 'Hundred'
        digits = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
        teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen',
                 'Nineteen']
        tys = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        hundred = num // 100
        ten = (num - hundred * 100) // 10
        one = num % 10
        ans = []
        if hundred > 0:
            ans.append(digits[hundred])
            ans.append(hundred_word)
        if ten == 1:
            ans.append(teens[one])
        elif ten > 1:
            ans.append(tys[ten])
        if ten != 1 and one > 0:
            ans.append(digits[one])
        return ans

    # Problem No.472 Concatenated Words
    #
    # Given an array of strings words (without duplicates), return all the concatenated words in the given list of
    # words.
    #
    # A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given
    # array.
    #
    # Example 1:
    #   Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
    #   Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
    #   Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
    #   "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
    #   "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
    #
    # Example 2:
    #   Input: words = ["cat","dog","catdog"]
    #   Output: ["catdog"]
    #
    # Constraints:
    #   1 <= words.length <= 10^4
    #   1 <= words[i].length <= 30
    #   words[i] consists of only lowercase English letters.
    #   All the strings of words are unique.
    #   1 <= sum(words[i].length) <= 105
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        ans = []
        word_set = set(words)
        for word in words:
            candidates = [0]
            for i in range(len(word)):
                for candidate in candidates:
                    if candidate > i:
                        continue
                    if word[candidate:i + 1] in word_set:
                        candidates.append(i + 1)
                        if candidate > 0 and i == len(word) - 1:
                            ans.append(word)
                            break
        return ans

    # Problem No.545 Boundary of Binary Tree
    #
    # The boundary of a binary tree is the concatenation of the root, the left boundary, the leaves ordered from
    # left-to-right, and the reverse order of the right boundary.
    #
    # The left boundary is the set of nodes defined by the following:
    #
    # The root node's left child is in the left boundary. If the root does not have a left child, then the left boundary
    # is empty.
    # If a node in the left boundary and has a left child, then the left child is in the left boundary.
    # If a node is in the left boundary, has no left child, but has a right child, then the right child is in the left
    # boundary.
    # The leftmost leaf is not in the left boundary.
    # The right boundary is similar to the left boundary, except it is the right side of the root's right subtree.
    # Again, the leaf is not part of the right boundary, and the right boundary is empty if the root does not have a
    # right child.
    #
    # The leaves are nodes that do not have any children. For this problem, the root is not a leaf.
    #
    # Given the root of a binary tree, return the values of its boundary.
    #
    # Example 1:
    #   Input: root = [1,null,2,3,4]
    #   Output: [1,3,4,2]
    #   Explanation:
    #   - The left boundary is empty because the root does not have a left child.
    #   - The right boundary follows the path starting from the root's right child 2 -> 4.
    #     4 is a leaf, so the right boundary is [2].
    #   - The leaves from left to right are [3,4].
    #   Concatenating everything results in [1] + [] + [3,4] + [2] = [1,3,4,2].
    #
    # Example 2:
    #   Input: root = [1,2,3,4,5,6,null,null,null,7,8,9,10]
    #   Output: [1,2,4,7,8,9,10,6,3]
    #   Explanation:
    #   - The left boundary follows the path starting from the root's left child 2 -> 4.
    #     4 is a leaf, so the left boundary is [2].
    #   - The right boundary follows the path starting from the root's right child 3 -> 6 -> 10.
    #     10 is a leaf, so the right boundary is [3,6], and in reverse order is [6,3].
    #   - The leaves from left to right are [4,7,8,9,10].
    #   Concatenating everything results in [1] + [2] + [4,7,8,9,10] + [6,3] = [1,2,4,7,8,9,10,6,3].
    #
    # Constraints:
    #   The number of nodes in the tree is in the range [1, 104].
    #   -1000 <= Node.val <= 1000
    #
    # Definition for a binary tree node.

    def visit_left(self, node: Optional[TreeNode], p_is_b: bool, has_left: bool, left_b: list, leaves: list):
        if node.left is None and node.right is None:
            # leave node
            leaves.append(node.val)
            return
        is_left_b = p_is_b and not has_left
        if is_left_b:
            # left boundary
            left_b.append(node.val)
        if node.left is not None:
            self.visit_left(node.left, is_left_b, False, left_b, leaves)
        if node.right is not None:
            self.visit_left(node.right, is_left_b, node.left is not None, left_b, leaves)

    def visit_right(self, node: Optional[TreeNode], p_is_b: bool, has_right: bool, right_b: list, leaves: list):
        if node.left is None and node.right is None:
            # leave node
            leaves.append(node.val)
            return
        is_right_b = p_is_b and not has_right
        if node.left is not None:
            self.visit_right(node.left, is_right_b, node.right is not None, right_b, leaves)
        if node.right is not None:
            self.visit_right(node.right, is_right_b, False, right_b, leaves)
        if is_right_b:
            # right boundary
            right_b.append(node.val)

    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        left_b, right_b, left_leaves, right_leaves = [], [], [], []
        if root.left is not None:
            self.visit_left(root.left, True, False, left_b, left_leaves)
        if root.right is not None:
            self.visit_right(root.right, True, False, right_b, right_leaves)
        return [root.val] + left_b + left_leaves + right_leaves + right_b

    # Problem No.719 Find K-th Smallest Pair Distance
    #
    # The distance of a pair of integers a and b is defined as the absolute difference between a and b.
    #
    # Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and
    # nums[j] where 0 <= i < j < nums.length.
    #
    # Example 1:
    #   Input: nums = [1,3,1], k = 1
    #   Output: 0
    #   Explanation: Here are all the pairs:
    #   (1,3) -> 2
    #   (1,1) -> 0
    #   (3,1) -> 2
    #   Then the 1st smallest distance pair is (1,1), and its distance is 0.
    #
    # Example 2:
    #   Input: nums = [1,1,1], k = 2
    #   Output: 0
    #
    # Example 3:
    #   Input: nums = [1,6,1], k = 3
    #   Output: 5
    #
    # Constraints:
    #   n == nums.length
    #   2 <= n <= 10^4
    #   0 <= nums[i] <= 10^6
    #   1 <= k <= n * (n - 1) / 2
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        low, high = 0, nums[-1] - nums[0]
        while low < high:
            mid = (low + high) // 2
            if self.count(nums, mid) < k:
                low = mid + 1
            else:
                high = mid
        return low

    def count(self, nums: list, max_diff: int):
        j, s = 0, 0
        for i in range(len(nums)):
            while nums[i] - nums[j] > max_diff:
                j += 1
            s += i - j
        return s

    # 767. Reorganize String
    #
    # Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
    #
    # Return any possible rearrangement of s or return "" if not possible.
    #
    # Example 1:
    #   Input: s = "aab"
    #   Output: "aba"
    #
    # Example 2:
    #   Input: s = "aaab"
    #   Output: ""
    #
    # Constraints:
    #   1 <= s.length <= 500
    #   s consists of lowercase English letters.
    def reorganizeString(self, s: str) -> str:
        cnt, half = Counter(s), (len(s) + 1) // 2
        letters = cnt.most_common()
        if letters[0][1] > half:
            return ""
        ans = []
        for char, cnt in letters:
            ans += [char] * cnt
        ans[::2], ans[1::2] = ans[:half], ans[half:]
        return "".join(ans)

    # Problem No.2455 Average Value of Even Numbers That Are Divisible by Three
    def averageValue(self, nums: List[int]) -> int:
        sum, cnt = 0, 0
        for n in nums:
            if n % 2 == 0 and n % 3 == 0:
                sum += n
                cnt += 1
        return sum // cnt

    # Problem No.2456 Most Popular Video Creator
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        c_cnt = {}
        c_ids_cnt = {}
        max_creators = []
        max_c_views = 0
        for i in range(len(creators)):
            creator, id_, cnt = creators[i], ids[i], views[i]
            if creator not in c_cnt:
                c_cnt[creator] = cnt
            else:
                c_cnt[creator] += cnt
            if c_cnt[creator] > max_c_views:
                max_c_views = c_cnt[creator]
                max_creators = [creator]
            elif c_cnt[creator] == max_c_views:
                max_creators.append(creator)
            if creator not in c_ids_cnt:
                c_ids_cnt[creator] = (id_, cnt)
            else:
                if cnt > c_ids_cnt[creator][1]:
                    c_ids_cnt[creator] = (id_, cnt)
                elif cnt == c_ids_cnt[creator][1] and id_ < c_ids_cnt[creator][0]:
                    c_ids_cnt[creator] = (id_, cnt)
        ans = []
        for creator in set(max_creators):
            ans.append([creator, c_ids_cnt[creator][0]])
        return ans

    # Problem No.2457 Minimum Addition to Make Integer Beautiful
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        d_list = []
        curr = n
        while curr > 0:
            d_list.append(curr % 10)
            curr //= 10
        d_list.append(0)
        s = sum(d_list)
        if s <= target:
            return 0
        p = 0
        ans = 0
        while s > target:
            if d_list[p] == 0:
                p += 1
                continue
            ans += (10 ** p) * (10 - d_list[p])
            s -= d_list[p] - 1
            d_list[p] = 0
            d_list[p + 1] += 1
            p += 1
            while d_list[p] >= 10:
                s -= d_list[p] - d_list[p] % 10 - 1
                d_list[p] = d_list[p] % 10
                d_list[p + 1] += 1
                p += 1
        return ans

    # Problem No.2458 Height of Binary Tree After Subtree Removal Queries
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        hights, depths, row_max = [], [], []
        self.visit(root, hights, depths, row_max, 0)
        ans = []
        for q in queries:
            row = row_max[depths[q]]
            if row[0] > 0 and row[0] != q:
                ans.append(depths[row[0]] + hights[row[0]])
            elif row[1] > 0 and row[1] != q:
                ans.append(depths[row[1]] + hights[row[1]])
            else:
                ans.append(depths[q] - 1)
        return ans

    def visit(self, root: Optional[TreeNode], hights: list, depths: list, row_max: list, depth):
        if root is None:
            return
        if root.val > len(hights) - 1:
            hights += [-1] * (root.val - len(hights) + 1)
        if root.val > len(depths) - 1:
            depths += [-1] * (root.val - len(depths) + 1)
        if depth > len(row_max) - 1:
            row_max += [[0, 0] for _ in range(depth - len(row_max) + 1)]
        depths[root.val] = depth
        self.visit(root.left, hights, depths, row_max, depth + 1)
        self.visit(root.right, hights, depths, row_max, depth + 1)
        if root.left is None and root.right is None:
            hights[root.val] = 0
        if root.left:
            hights[root.val] = hights[root.left.val] + 1
        if root.right and hights[root.right.val] + 1 > hights[root.val]:
            hights[root.val] = hights[root.right.val] + 1
        if hights[row_max[depth][0]] < hights[root.val]:
            row_max[depth][0], row_max[depth][1] = root.val, row_max[depth][0]
        elif hights[row_max[depth][1]] < hights[root.val]:
            row_max[depth][1] = root.val

    # Problem No.828 Count Unique Characters of All Substrings of a Given String
    #
    # Let's define a function countUniqueChars(s) that returns the number of unique characters on s.
    #
    # For example, calling countUniqueChars(s) if s = "LEETCODE" then "L", "T", "C", "O", "D" are the unique characters
    # since they appear only once in s, therefore countUniqueChars(s) = 5.
    # Given a string s, return the sum of countUniqueChars(t) where t is a substring of s. The test cases are generated
    # such that the answer fits in a 32-bit integer.
    #
    # Notice that some substrings can be repeated so in this case you have to count the repeated ones too.
    #
    # Example 1:
    #   Input: s = "ABC"
    #   Output: 10
    #   Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
    #   Every substring is composed with only unique letters.
    #   Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10
    #
    # Example 2:
    #   Input: s = "ABA"
    #   Output: 8
    #   Explanation: The same as example 1, except countUniqueChars("ABA") = 1.
    #
    # Example 3:
    #   Input: s = "LEETCODE"
    #   Output: 92
    #
    # Constraints:
    #   1 <= s.length <= 105
    #   s consists of uppercase English letters only.
    def uniqueLetterString(self, s: str) -> int:
        last_two = {c: [-1, -1] for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
        diff = 0
        ans = 0
        for i, c in enumerate(s):
            diff += i - last_two[c][0] - (last_two[c][0] - last_two[c][1])
            last_two[c][1], last_two[c][0] = last_two[c][0], i
            ans += diff
        return ans

    # Problem No.863 All Nodes Distance K in Binary Tree
    #
    # Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the
    # values of all nodes that have a distance k from the target node.
    #
    # You can return the answer in any order.
    #
    # Example 1:
    #   Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
    #   Output: [7,4,1]
    #   Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
    #
    # Example 2:
    #   Input: root = [1], target = 1, k = 3
    #   Output: []
    #
    # Constraints:
    #   The number of nodes in the tree is in the range [1, 500].
    #   0 <= Node.val <= 500
    #   All the values Node.val are unique.
    #   target is the value of one of the nodes in the tree.
    #   0 <= k <= 1000
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        path = []
        self.find_path(root, target, path)
        ans = []
        for i, v in enumerate(path):
            left_dis = k - len(path) + i
            if left_dis < 0 or i == len(path) - 1:
                continue
            if path[i + 1] != v.left:
                ans += self.distance_x(v.left, left_dis)
            if path[i + 1] != v.right:
                ans += self.distance_x(v.right, left_dis)
        ans += self.distance_x(path[-1], k)
        if len(path) >= k + 1:
            ans.append(path[-k - 1].val)
        return list(set(ans))

    def find_path(self, root: TreeNode, target: TreeNode, path: list) -> bool:
        if root is None:
            return False
        path.append(root)
        if root.val == target.val:
            return True
        if self.find_path(root.left, target, path):
            return True
        if self.find_path(root.right, target, path):
            return True
        path.pop()
        return False

    def distance_x(self, root: TreeNode, x: int) -> List[int]:
        if root is None:
            return []
        if x == 0:
            return [root.val]
        a = self.distance_x(root.left, x - 1)
        b = self.distance_x(root.right, x - 1)
        return a + b

    # Problem No.909 Snakes and Ladders
    #
    # You are given an n x n integer matrix board where the cells are labeled from 1 to n^2 in a Boustrophedon style
    # starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.
    #
    # You start on square 1 of the board. In each move, starting from square curr, do the following:
    #
    # Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n^2)].
    # This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations,
    # regardless of the size of the board.
    # If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to
    # next.
    # The game ends when you reach the square n2.
    # A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or
    # ladder is board[r][c]. Squares 1 and n^2 do not have a snake or ladder.
    #
    # Note that you only take a snake or ladder at most once per move. If the destination to a snake or ladder is the
    # start of another snake or ladder, you do not follow the subsequent snake or ladder.
    #
    # For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow
    # the ladder to square 3, but do not follow the subsequent ladder to 4.
    # Return the least number of moves required to reach the square n2. If it is not possible to reach the square,
    # return -1.
    #
    # Example 1:
    #   Input: board = [
    #   [-1,-1,-1,-1,-1,-1],
    #   [-1,-1,-1,-1,-1,-1],
    #   [-1,-1,-1,-1,-1,-1],
    #   [-1,35,-1,-1,13,-1],
    #   [-1,-1,-1,-1,-1,-1],
    #   [-1,15,-1,-1,-1,-1]
    #   ]
    #   Output: 4
    #   Explanation:
    #   In the beginning, you start at square 1 (at row 5, column 0).
    #   You decide to move to square 2 and must take the ladder to square 15.
    #   You then decide to move to square 17 and must take the snake to square 13.
    #   You then decide to move to square 14 and must take the ladder to square 35.
    #   You then decide to move to square 36, ending the game.
    #   This is the lowest possible number of moves to reach the last square, so return 4.
    #
    # Example 2:
    #   Input: board = [[-1,-1],[-1,3]]
    #   Output: 1
    #
    # Constraints:
    #   n == board.length == board[i].length
    #   2 <= n <= 20
    #   grid[i][j] is either -1 or in the range [1, n2].
    #   The squares labeled 1 and n2 do not have any ladders or snakes.
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n, num = len(board), len(board) * len(board)
        end2start = [[] for _ in range(num)]
        start2end = [-1] * num
        for i in range(n):
            for j in range(n):
                index = (n - 1 - i) * n + (n - 1 - j if (n - 1 - i) % 2 else j)
                if board[i][j] - 1 >= 0:
                    end2start[board[i][j] - 1].append(index)
                start2end[index] = board[i][j] - 1
        waits = {num - 1}
        visited = {num - 1}
        step = 0
        while len(waits) > 0:
            step += 1
            new_waits = set()
            for end in waits:
                if start2end[end] in visited or start2end[end] < 0:
                    for i in range(end - 6, end):
                        if i in visited:
                            continue
                        if i == 0:
                            return step
                        new_waits.add(i)
                perv_list = end2start[end]
                assert isinstance(perv_list, list)
                for perv in perv_list:
                    for i in range(perv - 6, perv):
                        if i in visited:
                            continue
                        if i == 0:
                            return step
                        new_waits.add(i)
            print(step, new_waits)
            visited.update(new_waits)
            waits = new_waits
        return -1

    # Problem No.937 Reorder Data in Log Files
    #
    # You are given an array of logs. Each log is a space-delimited string of words, where the first word is the
    # identifier.
    #
    # There are two types of logs:
    #
    # Letter-logs: All words (except the identifier) consist of lowercase English letters.
    # Digit-logs: All words (except the identifier) consist of digits.
    # Reorder these logs so that:
    #
    # The letter-logs come before all digit-logs.
    # The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them
    # lexicographically by their identifiers.
    # The digit-logs maintain their relative ordering.
    # Return the final order of the logs.
    #
    # Example 1:
    #   Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    #   Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
    #   Explanation:
    #   The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
    #   The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".
    #
    # Example 2:
    #   Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
    #   Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
    #
    # Constraints:
    #   1 <= logs.length <= 100
    #   3 <= logs[i].length <= 100
    #   All the tokens of logs[i] are separated by a single space.
    #   logs[i] is guaranteed to have an identifier and at least one word after the identifier.

    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def get_key(item):
            gap = item.find(" ")
            if item[gap + 1] in "1234567890":
                # '{' is bigger than any lowercase letters
                return "{"
            else:
                return item[gap + 1:] + "  " + item[:gap]

        return sorted(logs, key=get_key)

    # Problem No.973 K Closest Points to Origin
    #
    # Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return
    # the k closest points to the origin (0, 0).
    #
    # The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)^2 + (y1 - y2)^2).
    #
    # You may return the answer in any order. The answer is guaranteed to be unique
    # (except for the order that it is in).
    #
    # Example 1:
    #   Input: points = [[1,3],[-2,2]], k = 1
    #   Output: [[-2,2]]
    #   Explanation:
    #   The distance between (1, 3) and the origin is sqrt(10).
    #   The distance between (-2, 2) and the origin is sqrt(8).
    #   Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
    #   We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
    #
    # Example 2:
    #   Input: points = [[3,3],[5,-1],[-2,4]], k = 2
    #   Output: [[3,3],[-2,4]]
    #   Explanation: The answer [[-2,4],[3,3]] would also be accepted.
    #
    # Constraints:
    #   1 <= k <= points.length <= 10^4
    #   -10^4 < xi, yi < 10^4

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        random.shuffle(points)
        self.sort(points, 0, len(points) - 1, k)
        return points[:k]

    def get_dis(self, p):
        return p[0] ** 2 + p[1] ** 2

    def sort(self, points: list, start: int, end: int, k: int):
        if start >= end:
            return
        mid_d = self.get_dis(points[start])
        low, high = start + 1, end
        while low <= high:
            if self.get_dis(points[low]) <= mid_d:
                low += 1
            else:
                points[low], points[high] = points[high], points[low]
                high -= 1
        points[start], points[high] = points[high], points[start]
        if low < k:
            self.sort(points, low, end, k)
        elif low > k:
            self.sort(points, start, low - 2, k)

    # Problem No.994 Rotting Oranges
    #
    # You are given an m x n grid where each cell can have one of three values:
    #
    # 0 representing an empty cell,
    # 1 representing a fresh orange, or
    # 2 representing a rotten orange.
    # Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
    #
    # Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible,
    # return -1.
    #
    # Example 1:
    #   Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
    #   Output: 4
    #
    # Example 2:
    #   Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
    #   Output: -1
    #   Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only
    #   happens 4-directionally.
    #
    # Example 3:
    #   Input: grid = [[0,2]]
    #   Output: 0
    #   Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
    #
    # Constraints:
    #   m == grid.length
    #   n == grid[i].length
    #   1 <= m, n <= 10
    #   grid[i][j] is 0, 1, or 2.
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def neighbors(_i):
            _i, _j = _i // n, _i % n
            if _i - 1 >= 0:
                yield (_i - 1) * n + _j
            if _i + 1 < m:
                yield (_i + 1) * n + _j
            if _j - 1 >= 0:
                yield _i * n + _j - 1
            if _j + 1 < n:
                yield _i * n + _j + 1

        rotten = set()
        total = minutes = 0
        for i, row in enumerate(grid):
            for j, d in enumerate(grid[i]):
                if d == 2:
                    rotten.add(i * n + j)
                if d == 1:
                    total += 1
        while total > 0 and len(rotten) > 0:
            minutes += 1
            new_rotten = set()
            for i in rotten:
                for ni in neighbors(i):
                    if grid[ni // n][ni % n] == 1:
                        grid[ni // n][ni % n] = 2
                        new_rotten.add(ni)
                        total -= 1
            rotten = new_rotten
        if total > 0:
            return -1
        return minutes

    # Problem No.1044 Longest Duplicate Substring
    #
    # Given a string s, consider all duplicated substrings: (contiguous) substrings of s that occur 2 or more times.
    # The occurrences may overlap.
    #
    # Return any duplicated substring that has the longest possible length. If s does not have a duplicated substring,
    # the answer is "".
    #
    # Example 1:
    #   Input: s = "banana"
    #   Output: "ana"
    #
    # Example 2:
    #   Input: s = "abcd"
    #   Output: ""
    #
    # Constraints:
    #   2 <= s.length <= 3 * 104
    #   s consists of lowercase English letters.
    def longestDupSubstring(self, s: str) -> str:
        int_s = [0] * len(s)
        for i in range(len(s)):
            int_s[i] = ord(s[i]) - ord('a')
        low, high = 1, len(s) - 1
        ans = ""
        while low <= high:
            mid = (high + low) // 2
            start = self.check(int_s, mid)
            if start >= 0:
                low = mid + 1
                ans = s[start:start + mid]
            else:
                high = mid - 1
        return ans

    def check(self, s: list, l: int) -> int:
        visited = defaultdict(list)
        MOD = 7 * 10 ** 9
        h = 0
        for i in range(l):
            h = (h * 26 + s[i]) % MOD
        high = 1
        for i in range(l - 1):
            high = (high * 26) % MOD
        visited[h].append(0)
        for i in range(1, len(s) - l + 1):
            h = ((h - s[i - 1] * high) * 26 + s[i + l - 1]) % MOD
            if h in visited:
                if any(not any(s[cand + j] != s[i + j] for j in range(l)) for cand in visited[h]):
                    return i
            visited[h].append(i)
        return -1
