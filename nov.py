import sys
from collections import defaultdict, Counter
from functools import lru_cache
from typing import List


# Problem No.348 Design Tic-Tac-Toe
#
# Assume the following rules are for the tic-tac-toe game on an n x n board between two players:
#
# A move is guaranteed to be valid and is placed on an empty block.
# Once a winning condition is reached, no more moves are allowed.
# A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
# Implement the TicTacToe class:
#
# TicTacToe(int n) Initializes the object the size of the board n.
# int move(int row, int col, int player) Indicates that the player with id player plays at the cell (row, col) of the
# board. The move is guaranteed to be a valid move, and the two players alternate in making moves. Return
# 0 if there is no winner after the move,
# 1 if player 1 is the winner after the move, or
# 2 if player 2 is the winner after the move.
#
# Example 1:
#   Input
#   ["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
#   [[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
#   Output
#   [null, 0, 0, 0, 0, 0, 0, 1]
#
#   Explanation
#   TicTacToe ticTacToe = new TicTacToe(3);
#   Assume that player 1 is "X" and player 2 is "O" in the board.
#   ticTacToe.move(0, 0, 1); // return 0 (no one wins)
#   |X| | |
#   | | | |    // Player 1 makes a move at (0, 0).
#   | | | |
#
#   ticTacToe.move(0, 2, 2); // return 0 (no one wins)
#   |X| |O|
#   | | | |    // Player 2 makes a move at (0, 2).
#   | | | |
#
#   ticTacToe.move(2, 2, 1); // return 0 (no one wins)
#   |X| |O|
#   | | | |    // Player 1 makes a move at (2, 2).
#   | | |X|
#
#   ticTacToe.move(1, 1, 2); // return 0 (no one wins)
#   |X| |O|
#   | |O| |    // Player 2 makes a move at (1, 1).
#   | | |X|
#
#   ticTacToe.move(2, 0, 1); // return 0 (no one wins)
#   |X| |O|
#   | |O| |    // Player 1 makes a move at (2, 0).
#   |X| |X|
#
#   ticTacToe.move(1, 0, 2); // return 0 (no one wins)
#   |X| |O|
#   |O|O| |    // Player 2 makes a move at (1, 0).
#   |X| |X|
#
#   ticTacToe.move(2, 1, 1); // return 1 (player 1 wins)
#   |X| |O|
#   |O|O| |    // Player 1 makes a move at (2, 1).
#   |X|X|X|
#
#
# Constraints:
#   2 <= n <= 100
#   player is 1 or 2.
#   0 <= row, col < n
#   (row, col) are unique for each different call to move.
#   At most n^2 calls will be made to move.
#
# Follow-up: Could you do better than O(n^2) per move() operation?
class TicTacToe:

    # Your TicTacToe object will be instantiated and called as such:
    # obj = TicTacToe(n)
    # param_1 = obj.move(row,col,player)

    def __init__(self, n: int):
        self.n = n
        self.horizontal, self.vertical, self.diagonal = [
            [0] * n, [0] * n], [[0] * n, [0] * n], [[0, 0], [0, 0]]

    def move(self, row: int, col: int, player: int) -> int:
        cnt = self.horizontal[player -
                              1][col] = self.horizontal[player - 1][col] + 1
        if cnt == self.n:
            return player
        cnt = self.vertical[player -
                            1][row] = self.vertical[player - 1][row] + 1
        if cnt == self.n:
            return player
        if row == col:
            cnt = self.diagonal[player -
                                1][0] = self.diagonal[player - 1][0] + 1
            if cnt == self.n:
                return player
        if row + col == self.n - 1:
            cnt = self.diagonal[player -
                                1][1] = self.diagonal[player - 1][1] + 1
            if cnt == self.n:
                return player
        return 0


class Solution:
    # Problem No.1152 Analyze User Website Visit Pattern
    #
    # You are given two string arrays username and website and an integer array timestamp. All the given arrays are of
    # the same length and the tuple [username[i], website[i], timestamp[i]] indicates that the user username[i] visited
    # the website website[i] at time timestamp[i].
    #
    # A pattern is a list of three websites (not necessarily distinct).
    #
    # For example, ["home", "away", "love"], ["leetcode", "love", "leetcode"], and ["luffy", "luffy", "luffy"] are all
    # patterns.
    # The score of a pattern is the number of users that visited all the websites in the pattern in the same order they
    # appeared in the pattern.
    #
    # For example, if the pattern is ["home", "away", "love"], the score is the number of users x such that x visited
    # "home" then visited "away" and visited "love" after that.
    # Similarly, if the pattern is ["leetcode", "love", "leetcode"], the score is the number of users x such that x
    # visited "leetcode" then visited "love" and visited "leetcode" one more time after that.
    # Also, if the pattern is ["luffy", "luffy", "luffy"], the score is the number of users x such that x visited
    # "luffy" three different times at different timestamps.
    # Return the pattern with the largest score. If there is more than one pattern with the same largest score,
    # return the lexicographically smallest such pattern.
    #
    # Example 1:
    #   Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"],
    #   timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home",
    #   "about", "career"]
    #   Output: ["home","about","career"]
    #   Explanation: The tuples in this example are:
    #   ["joe","home",1],["joe","about",2],["joe","career",3],["james","home",4],["james","cart",5],["james","maps",6],
    #   ["james","home",7],["mary","home",8],["mary","about",9], and ["mary","career",10].
    #   The pattern ("home", "about", "career") has score 2 (joe and mary).
    #   The pattern ("home", "cart", "maps") has score 1 (james).
    #   The pattern ("home", "cart", "home") has score 1 (james).
    #   The pattern ("home", "maps", "home") has score 1 (james).
    #   The pattern ("cart", "maps", "home") has score 1 (james).
    #   The pattern ("home", "home", "home") has score 0 (no user visited home 3 times).
    #
    # Example 2:
    #   Input: username = ["ua","ua","ua","ub","ub","ub"], timestamp = [1,2,3,4,5,6], website = ["a","b","a","a","b",
    #   "c"]
    #   Output: ["a","b","a"]
    #
    # Constraints:
    #   3 <= username.length <= 50
    #   1 <= username[i].length <= 10
    #   timestamp.length == username.length
    #   1 <= timestamp[i] <= 10^9
    #   website.length == username.length
    #   1 <= website[i].length <= 10
    #   username[i] and website[i] consist of lowercase English letters.
    #   It is guaranteed that there is at least one user who visited at least three websites.
    #   All the tuples [username[i], timestamp[i], website[i]] are unique.
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        users = defaultdict(list)
        for i in range(len(username)):
            users[username[i]].append((website[i], timestamp[i]))
        pattern_cnt = Counter()
        for user, view in users.items():
            webs = [x[0] for x in sorted(view, key=lambda x: x[1])]
            # print(webs)
            pattern_cnt.update(set(self.all_patterns(webs)))
        ps = pattern_cnt.most_common(len(pattern_cnt))
        # print(ps)
        ans = ps[0][0]
        p = 1
        while p < len(ps) and ps[p][1] == ps[0][1]:
            if ps[p][0] < ans:
                ans = ps[p][0]
            p += 1
        return list(ans[:])

    def all_patterns(self, webs: list):
        for i in range(len(webs) - 2):
            for j in range(i + 2, len(webs)):
                for k in range(i + 1, j):
                    yield webs[i], webs[k], webs[j]

    # Problem No.818 Race Car
    #
    # Your car starts at position 0 and speed +1 on an infinite number line. Your car can go into negative positions.
    # Your car drives automatically according to a sequence of instructions 'A' (accelerate) and 'R' (reverse):
    #
    # When you get an instruction 'A', your car does the following:
    # position += speed
    # speed *= 2
    # When you get an instruction 'R', your car does the following:
    # If your speed is positive then speed = -1
    # otherwise speed = 1
    # Your position stays the same.
    # For example, after commands "AAR", your car goes to positions 0 --> 1 --> 3 --> 3, and your speed goes to
    # 1 --> 2 --> 4 --> -1.
    #
    # Given a target position target, return the length of the shortest sequence of instructions to get there.
    #
    # Example 1:
    #   Input: target = 3
    #   Output: 2
    #   Explanation:
    #   The shortest instruction sequence is "AA".
    #   Your position goes from 0 --> 1 --> 3.
    #
    # Example 2:
    #   Input: target = 6
    #   Output: 5
    #   Explanation:
    #   The shortest instruction sequence is "AAARA".
    #   Your position goes from 0 --> 1 --> 3 --> 7 --> 7 --> 6.
    #
    # Constraints:
    #   1 <= target <= 10^4
    def racecar(self, target: int) -> int:
        """
        DP bottom-up
        :param target:
        :return:
        """
        dp = [sys.maxsize] * (target + 3)
        dp[0], dp[1], dp[2] = 0, 1, 4
        x = 2
        for t in range(3, len(dp)):
            if t == 2 ** x - 1:
                dp[t], x = x, x + 1
                continue
            # from left
            low, high = 2 ** (x - 1) - 1, 2 ** x - 1
            dp[t] = min(dp[t], x + 1 + dp[high - t])
            k = 0
            while low - (2 ** k - 1) >= 0:
                dp[t] = min(dp[t], x - 1 + k + 2 + dp[t - low + (2 ** k - 1)])
                k += 1
        return dp[target]

    @lru_cache(None)
    def racecar1(self, target: int) -> int:
        """
        DP top-down
        :param target:
        :return:
        """
        k = 0
        while 2 ** k < target + 1:
            k += 1
        if target + 1 == 2 ** k:
            return k
        low, high = 2 ** (k - 1) - 1, 2 ** k - 1
        j = 0
        ans = k + 1 + self.racecar(high - target)
        while low - (2 ** j - 1) > 0:
            ans = min(ans, k - 1 + 1 + j + 1 +
                      self.racecar(target - low + (2 ** j - 1)))
            j += 1
        return ans

    def racecar2(self, target: int) -> int:
        """
        BFS
        :param target:
        :return:
        """
        nodes = [(0, 1, 0)]
        visited = {(0, 1)}
        start, step = 0, 0
        while True:
            p, s, ans = nodes[start]
            # A
            n_p, n_s = p + s, 2 * s
            if n_p == target:
                return ans + 1
            if 0 <= n_p < target * 2 and (n_p, n_s) not in visited:
                nodes.append((n_p, n_s, ans + 1))
                visited.add((n_p, n_s))
            # R
            n_p, n_s = p, 1 if s < 0 else -1
            if n_p == target:
                return ans + 1
            if 0 <= n_p < target * 2 and (n_p, n_s) not in visited:
                nodes.append((n_p, n_s, ans + 1))
                visited.add((n_p, n_s))
            if n_p == target:
                return ans + 1
            start += 1

    # Problem No.1268 Search Suggestions System
    #
    # You are given an array of strings products and a string searchWord.
    #
    # Design a system that suggests at most three product names from products after each character of searchWord is
    # typed. Suggested products should have common prefix with searchWord. If there are more than three products with a
    # common prefix return the three lexicographically minimums products.
    #
    # Return a list of lists of the suggested products after each character of searchWord is typed.
    #
    # Example 1:
    #   Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
    #   Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],
    #   ["mouse","mousepad"],["mouse","mousepad"]]
    #   Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
    #   After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
    #   After typing mou, mous and mouse the system suggests ["mouse","mousepad"].
    #
    # Example 2:
    #   Input: products = ["havana"], searchWord = "havana"
    #   Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
    #   Explanation: The only word "havana" will be always suggested while typing the search word.
    #
    # Constraints:
    #   1 <= products.length <= 1000
    #   1 <= products[i].length <= 3000
    #   1 <= sum(products[i].length) <= 2 * 104
    #   All the strings of products are unique.
    #   products[i] consists of lowercase English letters.
    #   1 <= searchWord.length <= 1000
    #   searchWord consists of lowercase English letters.
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        start = 0
        ans = []
        for i in range(len(searchWord)):
            start = self.search(products, start, len(
                products) - 1, searchWord[:i + 1])
            ans.append([])
            for j in range(3):
                if start + j >= len(products):
                    continue
                if len(products[start + j]) >= i + 1 and products[start + j][:i + 1] == searchWord[:i + 1]:
                    ans[-1].append(products[start + j])
        return ans

    def search(self, array: List[str], start: int, end: int, target: str):
        if start == end:
            return start
        mid = (start + end) // 2
        if target <= array[mid]:
            return self.search(array, start, mid, target)
        else:
            return self.search(array, mid + 1, end, target)

    # Problem No.1567 Maximum Length of Subarray With Positive Product
    #
    # Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is
    # positive.
    #
    # A subarray of an array is a consecutive sequence of zero or more values taken out of that array.
    #
    # Return the maximum length of a subarray with positive product.
    #
    # Example 1:
    #   Input: nums = [1,-2,-3,4]
    #   Output: 4
    #   Explanation: The array nums already has a positive product of 24.
    #
    # Example 2:
    #   Input: nums = [0,1,-2,-3,-4]
    #   Output: 3
    #   Explanation: The longest subarray with positive product is [1,-2,-3] which has a product of 6.
    #   Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.
    #
    # Example 3:
    #   Input: nums = [-1,-2,-3,0,1]
    #   Output: 2
    #   Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3].
    #
    # Constraints:
    #   1 <= nums.length <= 10^5
    #   -10^9 <= nums[i] <= 10^9
    def getMaxLen(self, nums: List[int]) -> int:
        even, odd, ans = 0, 0, 0
        for n in nums:
            if n > 0:
                even, odd = even + 1, odd + 1 if odd > 0 else odd
            elif n < 0:
                even, odd = odd + 1 if odd > 0 else 0, even + 1
            else:
                even, odd = 0, 0
            ans = max(ans, even)
        return ans

    # Problem No.2472 Maximum Number of Non-overlapping Palindrome Substrings
    #
    # You are given a string s and a positive integer k.
    #
    # Select a set of non-overlapping substrings from the string s that satisfy the following conditions:
    #
    # The length of each substring is at least k.
    # Each substring is a palindrome.
    # Return the maximum number of substrings in an optimal selection.
    #
    # A substring is a contiguous sequence of characters within a string.
    #
    # Example 1:
    #   Input: s = "abaccdbbd", k = 3
    #   Output: 2
    #   Explanation: We can select the substrings underlined in s = "abaccdbbd". Both "aba" and "dbbd" are palindromes
    #   and have a length of at least k = 3.
    #   It can be shown that we cannot find a selection with more than two valid substrings.
    #
    # Example 2:
    #   Input: s = "adbcda", k = 2
    #   Output: 0
    #   Explanation: There is no palindrome substring of length at least 2 in the string.
    #
    # Constraints:
    #   1 <= k <= s.length <= 2000
    #   s consists of lowercase English letters.
    def maxPalindromes(self, s: str, k: int) -> int:
        if k == 1:
            return len(s)
        dp = [0] * (len(s) + 1)
        letters = defaultdict(list)
        for i in range(0, len(s)):
            letters[s[i]].append(i)
            if i < k - 1:
                continue
            dp[i] = dp[i - 1]
            if len(letters[s[i]]) > 1:
                for j in letters[s[i]][::-1]:
                    if i - j + 1 < k:
                        continue
                    if dp[j - 1] + 1 <= dp[i]:
                        break
                    if self.isPalindrom(s[j:i + 1]):
                        dp[i] = max(dp[i], dp[j - 1] + 1)
                        break
        return dp[-2]

    @lru_cache(None)
    def isPalindrom(self, s: str):
        if len(s) == 1 or (len(s) == 2 and s[0] == s[1]):
            return True
        return s[0] == s[-1] and self.isPalindrom(s[1:-1])

    # Problem No.399 Evaluate Division
    #
    # You are given an array of variable pairs equations and an array of real numbers values, where
    # equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that
    # represents a single variable.
    #
    # You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the
    # answer for Cj / Dj = ?.
    #
    # Return the answers to all queries. If a single answer cannot be determined, return -1.0.
    #
    # Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero
    # and that there is no contradiction.
    #
    # Example 1:
    #   Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],
    #   ["a","a"],["x","x"]]
    #   Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
    #   Explanation:
    #   Given: a / b = 2.0, b / c = 3.0
    #   queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
    #   return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
    #
    # Example 2:
    #   Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],
    #   ["bc","cd"],["cd","bc"]]
    #   Output: [3.75000,0.40000,5.00000,0.20000]
    #
    # Example 3:
    #   Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
    #   Output: [0.50000,2.00000,-1.00000,-1.00000]
    #
    # Constraints:
    #   1 <= equations.length <= 20
    #   equations[i].length == 2
    #   1 <= Ai.length, Bi.length <= 5
    #   values.length == equations.length
    #   0.0 < values[i] <= 20.0
    #   1 <= queries.length <= 20
    #   queries[i].length == 2
    #   1 <= Cj.length, Dj.length <= 5
    #   Ai, Bi, Cj, Dj consist of lower case English letters and digits.
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        data = defaultdict(dict)
        for i, eq in enumerate(equations):
            data[eq[0]][eq[1]] = values[i]
            data[eq[1]][eq[0]] = 1.0 / values[i]
            data[eq[0]][eq[0]] = data[eq[1]][eq[1]] = 1.0
        ans = []
        for q in queries:
            ans.append(self.calc(q[0], q[1], data))
        return ans

    def calc(self, src, des, data):
        res = data.get(src, {}).get(des, None)
        if res:
            return res
        visited = {src}
        waits = {(src, n) for n in data[src].keys()}
        while len(waits) > 0:
            prev, curr = waits.pop()
            data[src][curr] = data[src][prev] * data[prev][curr]
            data[curr][src] = 1.0 / data[src][curr]
            if curr == des:
                return data[src][curr]
            visited.add(curr)
            for n in data[curr].keys():
                if n not in visited:
                    waits.add((curr, n))
        return -1.0

    # Problem No.1864 Minimum Number of Swaps to Make the Binary String Alternating
    #
    # Given a binary string s, return the minimum number of character swaps to make it alternating, or -1 if it is
    # impossible.
    #
    # The string is called alternating if no two adjacent characters are equal. For example, the strings "010" and
    # "1010" are alternating, while the string "0100" is not.
    #
    # Any two characters may be swapped, even if they are not adjacent.
    #
    # Example 1:
    #   Input: s = "111000"
    #   Output: 1
    #   Explanation: Swap positions 1 and 4: "111000" -> "101010"
    #   The string is now alternating.
    #
    # Example 2:
    #   Input: s = "010"
    #   Output: 0
    #   Explanation: The string is already alternating, no swaps are needed.
    #
    # Example 3:
    #   Input: s = "1110"
    #   Output: -1
    #
    # Constraints:
    #   1 <= s.length <= 1000
    #   s[i] is either '0' or '1'.
    def minSwaps(self, s: str) -> int:
        cnt_0, cnt_1 = [0, 0], [0, 0]
        for i, c in s:
            if c == '0':
                cnt_0[i % 2] += 1
            else:
                cnt_1[i % 2] += 1
        if sum(cnt_0) == sum(cnt_1) + 1:
            return cnt_0[1]
        elif sum(cnt_1) == sum(cnt_0) + 1:
            return cnt_1[1]
        elif sum(cnt_0) == sum(cnt_1):
            return min(cnt_0)
        return -1

    # Problem No.2055 Plates Between Candles
    #
    # There is a long table with a line of plates and candles arranged on top of it. You are given a 0-indexed string s
    # consisting of characters '*' and '|' only, where a '*' represents a plate and a '|' represents a candle.
    #
    # You are also given a 0-indexed 2D integer array queries where queries[i] = [left_i, right_i] denotes the substring
    # s[left_i...right_i] (inclusive). For each query, you need to find the number of plates between candles that are in
    # the substring. A plate is considered between candles if there is at least one candle to its left and at least one
    # candle to its right in the substring.
    #
    # For example, s = "||**||**|*", and a query [3, 8] denotes the substring "*||**|". The number of plates between
    # candles in this substring is 2, as each of the two plates has at least one candle in the substring to its left
    # and right.
    # Return an integer array answer where answer[i] is the answer to the ith query.
    #
    # Example 1:
    #   ex-1
    #   Input: s = "**|**|***|", queries = [[2,5],[5,9]]
    #   Output: [2,3]
    #   Explanation:
    #   - queries[0] has two plates between candles.
    #   - queries[1] has three plates between candles.
    #
    # Example 2:
    #   ex-2
    #   Input: s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
    #   Output: [9,0,0,0,0]
    #   Explanation:
    #   - queries[0] has nine plates between candles.
    #   - The other queries have zero plates between candles.
    #
    # Constraints:
    #   3 <= s.length <= 105
    #   s consists of '*' and '|' characters.
    #   1 <= queries.length <= 105
    #   queries[i].length == 2
    #   0 <= left_i <= right_i < s.length
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        left_cnt = [0] * len(s)
        plates_cnt = 0
        first_p, last_p = [-1] * (len(s) + 1), [len(s)] * (len(s) + 1)
        j = -1
        for i, c in enumerate(s):
            if c == '|':
                left_cnt[i] = plates_cnt
                last_p[i] = i
                j += 1
                while j < len(s) and s[j] != '|':
                    j += 1
                first_p[i] = j
            else:
                last_p[i] = last_p[i - 1]
                first_p[i] = first_p[i - 1]
                plates_cnt += 1
        ans = []
        for q in queries:
            left, right = q[0], q[1]
            if left <= first_p[left] < last_p[right] <= right:
                ans.append(left_cnt[last_p[right]] - left_cnt[first_p[left]])
            else:
                ans.append(0)
        return ans

    # Problem No.2214 Minimum Health to Beat Game
    #
    # You are playing a game that has n levels numbered from 0 to n - 1. You are given a 0-indexed integer array damage
    # where damage[i] is the amount of health you will lose to complete the ith level.
    #
    # You are also given an integer armor. You may use your armor ability at most once during the game on any level
    # which will protect you from at most armor damage.
    #
    # You must complete the levels in order and your health must be greater than 0 at all times to beat the game.
    #
    # Return the minimum health you need to start with to beat the game.
    #
    # Example 1:
    #   Input: damage = [2,7,4,3], armor = 4
    #   Output: 13
    #   Explanation: One optimal way to beat the game starting at 13 health is:
    #   On round 1, take 2 damage. You have 13 - 2 = 11 health.
    #   On round 2, take 7 damage. You have 11 - 7 = 4 health.
    #   On round 3, use your armor to protect you from 4 damage. You have 4 - 0 = 4 health.
    #   On round 4, take 3 damage. You have 4 - 3 = 1 health.
    #   Note that 13 is the minimum health you need to start with to beat the game.
    # 
    # Example 2:
    #   Input: damage = [2,5,3,4], armor = 7
    #   Output: 10
    #   Explanation: One optimal way to beat the game starting at 10 health is:
    #   On round 1, take 2 damage. You have 10 - 2 = 8 health.
    #   On round 2, use your armor to protect you from 5 damage. You have 8 - 0 = 8 health.
    #   On round 3, take 3 damage. You have 8 - 3 = 5 health.
    #   On round 4, take 4 damage. You have 5 - 4 = 1 health.
    #   Note that 10 is the minimum health you need to start with to beat the game.
    # 
    # Example 3:
    #   Input: damage = [3,3,3], armor = 0
    #   Output: 10
    #   Explanation: One optimal way to beat the game starting at 10 health is:
    #   On round 1, take 3 damage. You have 10 - 3 = 7 health.
    #   On round 2, take 3 damage. You have 7 - 3 = 4 health.
    #   On round 3, take 3 damage. You have 4 - 3 = 1 health.
    #   Note that you did not use your armor ability.
    #
    # Constraints:
    #   n == damage.length
    #   1 <= n <= 10^5
    #   0 <= damage[i] <= 10^5
    #   0 <= armor <= 10^5
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        left_damage, ds = [0] * len(damage), 0 
        for i in range(len(damage)):
            ds += damage[-i-1]
            left_damage[-i-1] = ds
        @lru_cache(None)
        def dp(start: int, a: int):
            if a == 0:
                return left_damage[start] + 1
            if start == len(damage) - 1:
                return max(damage[-1] - a + 1, 1)
            return min(dp(start+1, a)+damage[start], dp(start+1, 0)+max(0, damage[start]-a))
        return dp(0, armor)

    def minimumHealth2(self, damage: List[int], armor: int) -> int:
        return sum(damage) + 1 - min(armor, max(damage)) 
 


if __name__ == '__main__':
    size = 1000
    x = 1
    pass
