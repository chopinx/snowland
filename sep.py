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
