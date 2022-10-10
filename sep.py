class Solution:
    # Problem No.1881 Maximum Value after Insertion
    #
    # You are given a very large integer n, represented as a string, and an integer digit x. The digits in n and the
    # digit x are in the inclusive range [1, 9], and n may represent a negative number.
    #
    # You want to maximize n's numerical value by inserting x anywhere in the decimal representation of n. You cannot
    # insert x to the left of the negative sign.
    #
    # For example, if n = 73 and x = 6, it would be best to insert it between 7 and 3, making n = 763.
    # If n = -55 and x = 2, it would be best to insert it before the first 5, making n = -255.
    # Return a string representing the maximum value of n after the insertion.
    #
    # Example 1:
    #   Input: n = "99", x = 9
    #   Output: "999"
    #   Explanation: The result is the same regardless of where you insert 9.
    #
    # Example 2:
    #   Input: n = "-13", x = 2
    #   Output: "-123"
    #   Explanation: You can make n one of {-213, -123, -132}, and the largest of those three is -123.
    #
    # Constraints:
    #   1 <= n.length <= 10^5
    #   1 <= x <= 9
    #   The digits in n are in the range [1, 9].
    #   n is a valid representation of an integer.
    #   In the case of a negative n, it will begin with '-'.
    def maxValue(self, n: str, x: int) -> str:
        str_x = str(x)
        for index in range(len(n)):
            if (n[index] < str_x, n[index] > str_x)[n[0] == '-']:
                return n[:index] + str_x + n[index:]
        return n + str_x

    # Problem No.2063 Vowels of All Substrings
    #
    # Given a string word, return the sum of the number of vowels ('a', 'e', 'i', 'o', and 'u') in every substring of
    # word.
    #
    # A substring is a contiguous (non-empty) sequence of characters within a string.
    #
    # Note: Due to the large constraints, the answer may not fit in a signed 32-bit integer. Please be careful during
    # the calculations.
    #
    # Example 1:
    #   Input: word = "aba"
    #   Output: 6
    #   Explanation:
    #   All possible substrings are: "a", "ab", "aba", "b", "ba", and "a".
    #       - "b" has 0 vowels in it
    #       - "a", "ab", "ba", and "a" have 1 vowel each
    #       - "aba" has 2 vowels in it
    #   Hence, the total sum of vowels = 0 + 1 + 1 + 1 + 1 + 2 = 6.
    #
    # Example 2:
    #   Input: word = "abc"
    #   Output: 3
    #   Explanation:
    #   All possible substrings are: "a", "ab", "abc", "b", "bc", and "c".
    #       - "a", "ab", and "abc" have 1 vowel each
    #       - "b", "bc", and "c" have 0 vowels each
    #   Hence, the total sum of vowels = 1 + 1 + 1 + 0 + 0 + 0 = 3.
    #
    # Example 3:
    #   Input: word = "ltcd"
    #   Output: 0
    #   Explanation: There are no vowels in any substring of "ltcd".
    #
    # Constraints:
    #   1 <= word.length <= 10^5
    #   word consists of lowercase English letters.
    def countVowels(self, word: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        sum = 0
        for i in range(len(word)):
            if word[i] in vowels:
                sum += (i + 1) * (len(word) - i)
        return sum

    # Problem No.49 Group Anagrams
    #
    # Given an array of strings strs, group the anagrams together. You can return the answer in any order.
    #
    # An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using
    # all the original letters exactly once.
    #
    # Example 1:
    #   Input: strs = ["eat","tea","tan","ate","nat","bat"]
    #   Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    #
    # Example 2:
    #   Input: strs = [""]
    #   Output: [[""]]
    #
    # Example 3:
    #   Input: strs = ["a"]
    #   Output: [["a"]]
    #
    # Constraints:
    #   1 <= strs.length <= 10^4
    #   0 <= strs[i].length <= 100
    #   strs[i] consists of lowercase English letters.
    def groupAnagrams(self, strs: list) -> list:
        res_map = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if res_map.get(sorted_word) is None:
                res_map[sorted_word] = [word]
            else:
                res_map[sorted_word].append(word)
        return list(res_map.values())

    # Problem No.127 Word Ladder
    #
    # A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words
    # beginWord -> s1 -> s2 -> ... -> sk such that:
    #
    # Every adjacent pair of words differs by a single letter.
    # Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
    # sk == endWord
    # Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest
    # transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
    #
    #
    #
    # Example 1:
    #   Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
    #   Output: 5
    #   Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words
    #   long.
    #
    # Example 2:
    #   Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
    #   Output: 0
    #   Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
    #
    # Constraints:
    #   1 <= beginWord.length <= 10
    #   endWord.length == beginWord.length
    #   1 <= wordList.length <= 5000
    #   wordList[i].length == beginWord.length
    #   beginWord, endWord, and wordList[i] consist of lowercase English letters.
    #   beginWord != endWord
    #   All the words in wordList are unique.
    def ladderLength(self, beginWord: str, endWord: str, wordList: list) -> int:

        def left(_word: str, _i: int):
            return _word[:_i] + _word[_i + 1:]

        index = [{} for _ in range(len(beginWord))]
        for word in wordList:
            for i in range(len(beginWord)):
                if index[i].get(left(word, i)) is None:
                    index[i][left(word, i)] = [word]
                else:
                    index[i][left(word, i)].append(word)

        if endWord not in wordList:
            return 0
        b_wait_list = {beginWord}
        b_visited = {beginWord}
        e_wait_list = {endWord}
        e_visited = {endWord}
        ans = 1
        while len(b_wait_list) > 0 and len(e_wait_list) > 0:
            b_wait_set = set()
            ans += 1
            for curr in b_wait_list:
                for i in range(len(beginWord)):
                    for word in index[i].get(left(curr, i), []):
                        if word not in b_visited:
                            b_visited.add(word)
                            b_wait_set.add(word)
                        if word in e_wait_list:
                            return ans
            b_wait_list = b_wait_set

            if len(b_wait_list) < len(e_wait_list):
                e_wait_set = set()
                ans += 1
                for curr in e_wait_list:
                    for i in range(len(beginWord)):
                        for word in index[i].get(left(curr, i), []):
                            if word not in e_visited:
                                e_visited.add(word)
                                e_wait_set.add(word)
                            if word in b_wait_list:
                                return ans
                e_wait_list = e_wait_set
        return 0
