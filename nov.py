import sys
from collections import defaultdict, Counter
from functools import lru_cache
from typing import List


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
            ans = min(ans, k - 1 + 1 + j + 1 + self.racecar(target - low + (2 ** j - 1)))
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
            start = self.search(products, start, len(products) - 1, searchWord[:i + 1])
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


if __name__ == '__main__':
    a = [[i * 5 + j for j in range(5)] for i in range(5)]
    print(a)
    print(a[:][0])
    print([r[0] for r in a])
    print(a[0])
