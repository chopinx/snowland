

from functools import lru_cache


class Solution():
    # Problem No.2100 Find Good Days to Rob the Bank
    # 
    # You and a gang of thieves are planning on robbing a bank. You are given a 0-indexed integer array security, 
    # where security[i] is the number of guards on duty on the ith day. The days are numbered starting from 0. You are 
    # also given an integer time.
    # 
    # The ith day is a good day to rob the bank if:
    # 
    # There are at least time days before and after the ith day,
    # The number of guards at the bank for the time days before i are non-increasing, and
    # The number of guards at the bank for the time days after i are non-decreasing.
    # More formally, this means day i is a good day to rob the bank if and only if 
    # security[i - time] >= security[i - time + 1] >= ... >= security[i] <= ... <= security[i + time - 1] <= 
    # security[i + time].
    # 
    # Return a list of all days (0-indexed) that are good days to rob the bank. The order that the days are returned in 
    # does not matter.
    # 
    # Example 1:
    #   Input: security = [5,3,3,3,5,6,2], time = 2
    #   Output: [2,3]
    #   Explanation:
    #   On day 2, we have security[0] >= security[1] >= security[2] <= security[3] <= security[4].
    #   On day 3, we have security[1] >= security[2] >= security[3] <= security[4] <= security[5].
    #   No other days satisfy this condition, so days 2 and 3 are the only good days to rob the bank.
    # 
    # Example 2:
    #   Input: security = [1,1,1,1,1], time = 0
    #   Output: [0,1,2,3,4]
    #   Explanation:
    #   Since time equals 0, every day is a good day to rob the bank, so return every day.
    # 
    # Example 3:
    #   Input: security = [1,2,3,4,5,6], time = 2
    #   Output: []
    #   Explanation:
    #   No day has 2 days before it that have a non-increasing number of guards.
    #   Thus, no day is a good day to rob the bank, so return an empty list.
    # 
    # Constraints:
    #   1 <= security.length <= 10^5
    #   0 <= security[i], time <= 10^5
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        non_inc = [1] * len(security)
        non_dec = [1] * len(security)
        for i in range(1,len(security)):
            if security[i] <= security[i-1]:
                non_inc[i] = non_inc[i-1] + 1
            if security[-1-i] <= security[-i]:
                non_dec[-1-i] = non_dec[-i] + 1
        ans = []
        for i in range(time, len(security)-1-time):
            if non_inc[i] - 1 >= time and non_dec[i] -1 <= time:
                ans.append(i)
        return ans

    # Problem No.135 Candy
    #
    # There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
    # 
    # You are giving candies to these children subjected to the following requirements:
    # 
    # Each child must have at least one candy.
    # Children with a higher rating get more candies than their neighbors.
    # Return the minimum number of candies you need to have to distribute the candies to the children.
    # 
    # Example 1:
    #   Input: ratings = [1,0,2]
    #   Output: 5
    #   Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
    # 
    # Example 2:
    #   Input: ratings = [1,2,2]
    #   Output: 4
    #   Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
    #   The third child gets 1 candy because it satisfies the above two conditions.
    # 
    # Constraints:
    #   n == ratings.length
    #   1 <= n <= 2 * 10^4
    #   0 <= ratings[i] <= 2 * 10^4
    def candy(self, ratings: List[int]) -> int:
        @lru_cache(None)
        def sub_candy(base: int, start:int):
            if start == len(ratings) - 1:
                return base, base
            if ratings[start] > ratings[start+1]:
                sub_sum , sub_base = sub_candy(1, start+1)
                if sub_base >= base:
                    return sub_sum + sub_base + 1, sub_base + 1
                else:
                    return sub_sum + base, base
            elif ratings[start] < ratings[start+1]: 
                sub_sum , sub_base = sub_candy(base + 1, start+1)
                return sub_sum + base, base
            else:
                sub_sum , sub_base = sub_candy(1, start+1)
                return sub_sum + base, base

        return sub_candy(1, 0)[0]