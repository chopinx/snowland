from typing import Optional, List


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __hash__(self):
        return hash(self.val)

    def __eq__(self, other):
        return self.val == other.val


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

    # Problem No.138 Copy List with Random Pointer
    #
    # A linked list of length n is given such that each node contains an additional random pointer, which could point
    # to any node in the list, or null.
    #
    # Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node
    # has its value set to the value of its corresponding original node. Both the next and random pointer of the new
    # nodes should point to new nodes in the copied list such that the pointers in the original list and copied list
    # represent the same list state. None of the pointers in the new list should point to nodes in the original list.
    #
    # For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding
    # two nodes x and y in the copied list, x.random --> y.
    #
    # Return the head of the copied linked list.
    #
    # The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of
    # [val, random_index] where:
    #
    # val: an integer representing Node.val
    # random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does
    # not point to any node.
    # Your code will only be given the head of the original linked list.
    #
    # Example 1:
    #   Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
    #   Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
    #
    # Example 2:
    #   Input: head = [[1,1],[2,1]]
    #   Output: [[1,1],[2,1]]
    #
    # Example 3:
    #   Input: head = [[3,null],[3,0],[3,null]]
    #   Output: [[3,null],[3,0],[3,null]]
    #
    # Constraints:
    #   0 <= n <= 1000
    #   -10^4 <= Node.val <= 10^4
    #   Node.random is null or is pointing to some node in the linked list.
    """
    # Definition for a Node.
    class Node:
        def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
            self.val = int(x)
            self.next = next
            self.random = random
    """

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_list = []

        node_map = {}
        curr = head
        # get node list and node map
        while curr is not None:
            node_list.append(curr)
            node_map[curr] = len(node_list) - 1
            curr = curr.next
        print(node_list)

        new_node_list = [Node(0) for _ in range(len(node_list))]
        new_head = new_node_list[0]
        for i in range(len(node_list)):
            new_node_list[i].val = node_list[i].val
            if i < len(node_list) - 1:
                new_node_list[i].next = new_node_list[i + 1]

        # get random list
        random_list = [-1 for _ in range(len(node_list))]
        for i in range(len(node_list)):
            curr = node_list[i]
            if curr.random is not None:
                new_node_list[i].random = new_node_list[node_map[curr.random]]

        return new_head

    # Problem No.140 Word Break II
    #
    # Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is
    # a valid dictionary word. Return all such possible sentences in any order.
    #
    # Note that the same word in the dictionary may be reused multiple times in the segmentation.
    #
    # Example 1:
    #   Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
    #   Output: ["cats and dog","cat sand dog"]
    #
    # Example 2:
    #   Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
    #   Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
    #   Explanation: Note that you are allowed to reuse a dictionary word.
    #
    # Example 3:
    #   Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
    #   utput: []
    #
    # Constraints:
    #   1 <= s.length <= 20
    #   1 <= wordDict.length <= 1000
    #   1 <= wordDict[i].length <= 10
    #   s and wordDict[i] consist of only lowercase English letters.
    #   All the strings of wordDict are unique.
    def wordBreak(self, s: str, wordDict: 'List[str]') -> 'List[str]':
        completed, uncompleted = {"": ""}, {"": ""}
        word_set = set(wordDict)
        for c in s:
            new_c, new_unc = {}, {}
            for sub_s in completed.keys():
                if c in word_set:
                    new_c[(sub_s + " " + c).strip()] = c
                else:
                    new_unc[(sub_s + " " + c).strip()] = c
                new_word = completed[sub_s] + c
                if new_word in word_set:
                    new_c[(sub_s.removesuffix(completed[sub_s]) + new_word).strip()] = new_word
                else:
                    new_unc[(sub_s.removesuffix(completed[sub_s]) + new_word).strip()] = new_word
            for sub_s in uncompleted.keys():
                new_word = uncompleted[sub_s] + c
                if new_word in word_set:
                    new_c[(sub_s.removesuffix(uncompleted[sub_s]) + new_word).strip()] = new_word
                else:
                    new_unc[(sub_s.removesuffix(uncompleted[sub_s]) + new_word).strip()] = new_word
            completed, uncompleted = new_c, new_unc
        return list(completed.keys())


from collections import OrderedDict


class LRUCache:
    # Problem No.146 LRU Cache
    #
    # Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
    #
    # Implement the LRUCache class:
    #
    # LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    # int get(int key) Return the value of the key if the key exists, otherwise return -1.
    # void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to
    # the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
    # The functions get and put must each run in O(1) average time complexity.
    #
    # Example 1:
    #   Input
    #   ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    #   [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    #   Output
    #   [null, null, null, 1, null, -1, null, -1, 3, 4]
    #
    #   Explanation
    #   LRUCache lRUCache = new LRUCache(2);
    #   lRUCache.put(1, 1); // cache is {1=1}
    #   lRUCache.put(2, 2); // cache is {1=1, 2=2}
    #   lRUCache.get(1);    // return 1
    #   lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    #   lRUCache.get(2);    // returns -1 (not found)
    #   lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    #   lRUCache.get(1);    // return -1 (not found)
    #   lRUCache.get(3);    // return 3
    #   lRUCache.get(4);    // return 4
    #
    # Constraints:
    #   1 <= capacity <= 3000
    #   0 <= key <= 10^4
    #   0 <= value <= 10^5
    #   At most 2 * 10^5 calls will be made to get and put.
    #
    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)
    def __init__(self, capacity: int):
        self.kv = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.kv:
            return -1
        self.kv.move_to_end(key)
        return self.kv[key]

    def put(self, key: int, value: int) -> None:
        if self.kv.get(key) is not None:
            self.kv.move_to_end(key)
        self.kv[key] = value
        if len(self.kv) > self.capacity:
            self.kv.popitem(last=False)
