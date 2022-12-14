package main

import (
	"math/rand"
	"sort"
)

// Problem No.1266 Minimum Time Visiting All Points
//
// On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in the order given by points.
// You can move according to these rules:
// 		In 1 second, you can either:
// 			move vertically by one unit,
// 			move horizontally by one unit, or
// 			move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
// 		You have to visit the points in the same order as they appear in the array.
// 		You are allowed to pass through points that appear later in the order, but these do not count as visits.
//
// Example 1:
// 		Input: points = [[1,1],[3,4],[-1,0]]
// 		Output: 7
// 		Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]
// 		Time from [1,1] to [3,4] = 3 seconds
// 		Time from [3,4] to [-1,0] = 4 seconds
// 		Total time = 7 seconds
//
// Example 2:
// 		Input: points = [[3,2],[-2,2]]
// 		Output: 5
//
// Constraints:
// 		points.length == n
// 		1 <= n <= 100
// 		points[i].length == 2
// 		-1000 <= points[i][0], points[i][1] <= 1000
//
// Solution:
// for any two points with integer coordinates a=(xa,ya) and b=(xb,yb), you can always move from a to b in n steps,
// where n=min(abs(xa-xb),abs(ya-yb)). Because when you take a step, you're either descending the distance in x-axis,
// nor descending the distance in y-axis, nor descending both, and one unit one step in one second.
func minTimeToVisitAllPoints(points [][]int) int {
	time := 0
	for i := 1; i < len(points); i++ {
		smallX, bigX := points[i][0], points[i-1][0]
		if smallX > bigX {
			smallX, bigX = bigX, smallX
		}
		smallY, bigY := points[i][1], points[i-1][1]
		if smallY > bigY {
			smallY, bigY = bigY, smallY
		}
		smallDiff, bigDiff := bigX-smallX, bigY-smallY
		if bigDiff < smallDiff {
			smallDiff, bigDiff = bigDiff, smallDiff
		}
		time += bigDiff
	}
	return time
}

// Problem No.1925 Count Square Sum Triples
//
// A square triple (a,b,c) is a triple where a, b, and c are integers and a^2 + b^2 = c^2.
// Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.
//
// Example 1:
// 		Input: n = 5
// 		Output: 2
// 		Explanation: The square triples are (3,4,5) and (4,3,5).
//
// Example 2:
// 		Input: n = 10
// 		Output: 4
// 		Explanation: The square triples are (3,4,5), (4,3,5), (6,8,10), and (8,6,10).
//
// Constraints:
// 		1 <= n <= 250
func countTriples(n int) int {
	hashLen := 4 * n
	squares := make([][]int, hashLen)
	for i := 1; i <= n; i++ {
		square := i * i
		hash := square % hashLen
		if squares[hash] == nil {
			squares[hash] = []int{square}
		} else {
			squares[hash] = append(squares[hash], square)
		}
	}
	count := 0
	maxSquare := n * n
	for a := 1; a <= n; a++ {
		for b := a; b <= n; b++ {
			squareSum := a*a + b*b
			if squareSum > maxSquare {
				break
			}
			hash := squareSum % hashLen
			if squares[hash] != nil {
				if fastFind(squares[hash], 0, len(squares[hash])-1, squareSum) {
					count += 2
					if a == b {
						count--
					}
				}
			}
		}
	}
	return count
}

func fastFind(nums []int, start int, end int, target int) bool {
	if end <= start {
		return nums[start] == target
	}
	mid := (start + end) / 2
	if nums[mid] == target {
		return true
	} else if nums[mid] > target {
		return fastFind(nums, start, mid-1, target)
	} else {
		return fastFind(nums, mid+1, end, target)
	}
}

// Problem No.2171 Removing Minimum Number of Magic Beans
//
// You are given an array of positive integers beans, where each integer represents the number of magic beans found in a particular magic bag.
// Remove any number of beans (possibly none) from each bag such that the number of beans in each remaining non-empty bag (still containing at least one bean) is equal. Once a bean has been removed from a bag, you are not allowed to return it to any of the bags.
// Return the minimum number of magic beans that you have to remove.
//
// Example 1:
// 		Input: beans = [4,1,6,5]
// 		Output: 4
// 		Explanation:
// 		- We remove 1 bean from the bag with only 1 bean.
// 		This results in the remaining bags: [4,0,6,5]
// 		- Then we remove 2 beans from the bag with 6 beans.
// 		This results in the remaining bags: [4,0,4,5]
// 		- Then we remove 1 bean from the bag with 5 beans.
// 		This results in the remaining bags: [4,0,4,4]
// 		We removed a total of 1 + 2 + 1 = 4 beans to make the remaining non-empty bags have an equal number of beans.
// 		There are no other solutions that remove 4 beans or fewer.
//
// Example 2:
// 		Input: beans = [2,10,3,2]
// 		Output: 7
// 		Explanation:
// 		- We remove 2 beans from one of the bags with 2 beans.
// 		This results in the remaining bags: [0,10,3,2]
// 		- Then we remove 2 beans from the other bag with 2 beans.
// 		This results in the remaining bags: [0,10,3,0]
// 		- Then we remove 3 beans from the bag with 3 beans.
// 		This results in the remaining bags: [0,10,0,0]
// 		We removed a total of 2 + 2 + 3 = 7 beans to make the remaining non-empty bags have an equal number of beans.
// 		There are no other solutions that removes 7 beans or fewer.
//
// Constraints:
// 		1 <= beans.length <= 10^5
// 		1 <= beans[i] <= 10^5
//
// Solution:
//
// Assume we want to descend each bag's bean into K, we have to split all bags to 3 groups,
// the number of beans in the bag is bigger than K as group one,
// the number of beans in the bag is equals to K as group two,
// and the number of beans in the bag is smaller than K as group three.
// We have to remove the beans in bags which belong to group one, until all bogs in groups one have exactly K beans.
// And then we have to remove the beans in bags which belong to group three, all of them.
// So when can calculate the number of beans have to be removed for each possible K, and find out in which the number of beans being removed is minimal.
func minimumRemoval(beans []int) int64 {
	sort.Ints(beans)
	beansSum := int64(0)
	for _, v := range beans {
		beansSum += int64(v)
	}
	minRemove := beansSum
	for i := 0; i < len(beans); i++ {
		curr := beansSum - int64(beans[i])*int64(len(beans)-i)
		if curr < minRemove {
			minRemove = curr
		}
	}
	return minRemove
}

// hackerrank Problem
func minGreaterArr(arr []int32) []int32 {
	fastSort(arr, 0, len(arr)-1)
	sum, sumA := 0, 0
	for i := 0; i < len(arr); i++ {
		sum += int(arr[i])
	}
	for i := len(arr) - 1; i >= 0; i-- {
		sumA += int(arr[i])
		if sumA*2 > sum {
			return arr[i:]
		}
	}
	return arr
}

func fastSort(arr []int32, start int, end int) {
	if start >= end {
		return
	}
	index := rand.Int()%(end-start+1) + start
	low, high := start+1, end
	arr[start], arr[index] = arr[index], arr[start]
	for low <= high {
		if arr[low] < arr[start] {
			low++
		} else {
			arr[low], arr[high] = arr[high], arr[low]
			high--
		}
	}
	fastSort(arr, start, high)
	fastSort(arr, low, end)
}

// Problem No.96 Unique Binary Search Trees
//
// Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
//
// Example 1:
// 		Input: n = 3
// 		Output: 5
//
// Example 2:
// 		Input: n = 1
// 		Output: 1
//
// Constraints:
// 		1 <= n <= 19
//
// Solving Time Cost: 20 minutes
func numTrees(n int) int {
	if n <= 1 {
		return 1
	}
	ans := make([]int, n+1)
	ans[0], ans[1] = 1, 1
	for i := 2; i <= n; i++ {
		for j := 0; j < i/2; j++ {
			ans[i] += ans[j] * ans[i-1-j]
		}
		ans[i] *= 2
		if i%2 == 1 {
			ans[i] += ans[i/2] * ans[i/2]
		}
		// fmt.Printf("n=%d, ans=%d\n", i, ans[i])
	}
	return ans[n]
}

// Problem No.452 Minimum Number of Arrows to Burst Balloons
//
// There are some spherical balloons taped onto a flat wall that represents the XY-plane.
// The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon
// whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.
// Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis.
// A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.
//
// Given the array points, return the minimum number of arrows that must be shot to burst all balloons.
//
// Example 1:
// 		Input: points = [[10,16],[2,8],[1,6],[7,12]]
// 		Output: 2
// 		Explanation: The balloons can be burst by 2 arrows:
// 		- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
// 		- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
//
// Example 2:
// 		Input: points = [[1,2],[3,4],[5,6],[7,8]]
// 		Output: 4
// 		Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.
//
// Example 3:
// 		Input: points = [[1,2],[2,3],[3,4],[4,5]]
// 		Output: 2
// 		Explanation: The balloons can be burst by 2 arrows:
// 			- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
// 			- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
//
// Constraints:
// 		1 <= points.length <= 10^5
// 		points[i].length == 2
// 		-2^31 <= xstart < xend <= 2^31 - 1
func findMinArrowShots(points [][]int) int {
	return findMinArrowShots1(points)
}

func findMinArrowShots1(points [][]int) int {
	left := LeftList{
		Points: points,
		Indexs: make([]int, len(points)),
	}
	for i := 0; i < len(left.Indexs); i++ {
		left.Indexs[i] = i
	}
	sort.Sort(left)
	rightList := []int{points[left.Indexs[0]][1]}
	for i := 1; i < len(points); i++ {
		if points[left.Indexs[i]][0] > rightList[len(rightList)-1] {
			rightList = append(rightList, points[left.Indexs[i]][1])
		} else if rightList[len(rightList)-1] > points[left.Indexs[i]][1] {
			rightList[len(rightList)-1] = points[left.Indexs[i]][1]
		}
	}
	return len(rightList)
}

type LeftList struct {
	Points [][]int
	Indexs []int
}

func (l LeftList) Len() int {
	return len(l.Points)
}

func (l LeftList) Less(i, j int) bool {
	return l.Points[l.Indexs[i]][0] < l.Points[l.Indexs[j]][0]
}

func (l LeftList) Swap(i, j int) {
	l.Indexs[i], l.Indexs[j] = l.Indexs[j], l.Indexs[i]
}

type RightList struct {
	Points [][]int
	Indexs []int
}

func (l RightList) Len() int {
	return len(l.Points)
}

func (l RightList) Less(i, j int) bool {
	return l.Points[l.Indexs[i]][1] < l.Points[l.Indexs[j]][1]
}

func (l RightList) Swap(i, j int) {
	l.Indexs[i], l.Indexs[j] = l.Indexs[j], l.Indexs[i]
}

func findMinArrowShots2(points [][]int) int {
	right := RightList{
		Points: points,
		Indexs: make([]int, len(points)),
	}
	for i := 0; i < len(right.Indexs); i++ {
		right.Indexs[i] = i
	}
	sort.Sort(right)
	// fmt.Printf("rightIndex: %v", right.Indexs)
	left := LeftList{
		Points: points,
		Indexs: make([]int, len(points)),
	}
	for i := 0; i < len(left.Indexs); i++ {
		left.Indexs[i] = i
	}
	sort.Sort(left)
	// fmt.Printf("leftIndex: %v", left.Indexs)
	visited := make(map[int]int)
	ans, j := 0, 0
	for i := 0; i < len(right.Indexs); i++ {
		cycleIndex := right.Indexs[i]
		if _, ok := visited[cycleIndex]; ok {
			continue
		}
		for j < len(points) && points[left.Indexs[j]][0] <= points[cycleIndex][1] {
			visited[left.Indexs[j]] = 0
			j++
		}
		// fmt.Printf("visited: %v\n", visited)
		ans++
		if len(visited) == len(points) {
			break
		}
	}
	return ans
}

// Problem No.764 Largest Plus Sign
//
// You are given an integer n. You have an n x n binary grid grid
// with all values initially 1's except for some indices given in the array mines.
// The ith element of the array mines is defined as mines[i] = [xi, yi] where grid[xi][yi] == 0.
// Return the order of the largest axis-aligned plus sign of 1's contained in grid. If there is none, return 0.
// An axis-aligned plus sign of 1's of order k has some center grid[r][c] == 1 along with four arms of
// length k - 1 going up, down, left, and right, and made of 1's.
// Note that there could be 0's or 1's beyond the arms of the plus sign,
// only the relevant area of the plus sign is checked for 1's.
//
// Example 1:
// 		Input: n = 5, mines = [[4,2]]
// 		Output: 2
// 		Explanation: In the above grid, the largest plus sign can only be of order 2. One of them is shown.
//
// Example 2:
// 		Input: n = 1, mines = [[0,0]]
// 		Output: 0
// 		Explanation: There is no plus sign, so return 0.
//
// Constraints:
// 		1 <= n <= 500
// 		1 <= mines.length <= 5000
// 		0 <= xi, yi < n
// 		All the pairs (xi, yi) are unique.
func orderOfLargestPlusSign(n int, mines [][]int) int {
	// transform the row to 1's block
	rows := make([][]int, n)
	cols := make([][]int, n)
	for i := 0; i < n; i++ {
		rows[i] = []int{-1, n}
	}
	for i := 0; i < n; i++ {
		cols[i] = []int{-1, n}
	}
	for _, m := range mines {
		rows[m[0]] = append(rows[m[0]], m[1])
		cols[m[1]] = append(cols[m[1]], m[0])
	}
	for i := 0; i < n; i++ {
		sort.Ints(rows[i])
		sort.Ints(cols[i])
	}
	ans := 0
	for r := 0; r < n; r++ {
		row := rows[r]
		if r+1 <= ans || (n-r) <= ans {
			continue
		}
		for i := 1; i < len(row); i++ {
			currC, lastC := row[i], row[i-1]
			for maxOrder := (currC - lastC) / 2; maxOrder > ans; maxOrder-- {
				c := lastC + maxOrder
				lastRIndex := findBlock(cols[c], r, 0, len(cols[c])-1)
				lastR, currR := cols[c][lastRIndex], cols[c][lastRIndex+1]
				// fmt.Printf("(%d, %d), r(%d, %d), c(%d, %d), min=%d\n", r, c, lastR, currR, lastC, currC, min(min(currR-r, r-lastR), maxOrder))
				if min(min(currR-r, r-lastR), maxOrder) > ans {
					ans = min(min(currR-r, r-lastR), maxOrder)
				}
				if c == currC-maxOrder {
					continue
				}
				c = currC - maxOrder
				lastRIndex = findBlock(cols[c], r, 0, len(cols[c])-1)
				lastR, currR = cols[c][lastRIndex], cols[c][lastRIndex+1]
				// fmt.Printf("(%d, %d), r(%d, %d), c(%d, %d), min=%d\n", r, c, lastR, currR, lastC, currC, min(min(currR-r, r-lastR), maxOrder))
				if min(min(currR-r, r-lastR), maxOrder) > ans {
					ans = min(min(currR-r, r-lastR), maxOrder)
				}
			}
		}
	}
	return ans
}

func min(a int, b int) int {
	if a < b {
		return a
	}
	return b
}

func findBlock(arr []int, target int, start int, end int) int {
	if end <= start+1 {
		return start
	}
	mid := (start + end) / 2
	if arr[mid] < target {
		return findBlock(arr, target, mid, end)
	} else if arr[mid] > target {
		return findBlock(arr, target, start, mid)
	} else {
		return mid
	}
}

// Problem No.1930 Unique Length-3 Palindromic Subsequences
//
// Given a string s, return the number of unique palindromes of length three that are a subsequence of s.
// Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.
// A palindrome is a string that reads the same forwards and backwards.
// A subsequence of a string is a new string generated from the original string with some characters (can be none)
// deleted without changing the relative order of the remaining characters.
// For example, "ace" is a subsequence of "abcde".
//
// Example 1:
// 		Input: s = "aabca"
// 		Output: 3
// 		Explanation: The 3 palindromic subsequences of length 3 are:
// 		- "aba" (subsequence of "aabca")
// 		- "aaa" (subsequence of "aabca")
// 		- "aca" (subsequence of "aabca")
//
// Example 2:
// 		Input: s = "adc"
// 		Output: 0
// 		Explanation: There are no palindromic subsequences of length 3 in "adc".
//
// Example 3:
// 		Input: s = "bbcbaba"
// 		Output: 4
// 		Explanation: The 4 palindromic subsequences of length 3 are:
// 		- "bbb" (subsequence of "bbcbaba")
// 		- "bcb" (subsequence of "bbcbaba")
// 		- "bab" (subsequence of "bbcbaba")
// 		- "aba" (subsequence of "bbcbaba")
//
// Constraints:
// 		3 <= s.length <= 10^5
// 		s consists of only lowercase English letters
func countPalindromicSubsequence(s string) int {
	// go through the string and mark the first and the last index of each letter
	maxIndex := make([]int, 26)
	minIndex := make([]int, 26)
	midLetters := make([]map[int]int, 26)
	for i := 0; i < len(maxIndex); i++ {
		maxIndex[i] = -1
		minIndex[i] = -1
		midLetters[i] = make(map[int]int)
	}
	for i, c := range s {
		if minIndex[c-'a'] < 0 {
			minIndex[c-'a'] = i
		}
		maxIndex[c-'a'] = i
	}
	for i, c := range s {
		for j := 0; j < len(maxIndex); j++ {
			if i > minIndex[j] && i < maxIndex[j] {
				midLetters[j][int(c-'a')] = 0
			}
		}
	}
	ans := 0
	for i := 0; i < len(midLetters); i++ {
		ans += len(midLetters[i])
	}
	return ans
}

func countPalindromicSubsequence2(s string) int {
	// you can reduce the memory usage by indexing all unique letters showed in the string
	// but the memory cost is already O(1)
	aheadCnt := make([][]int, 26)
	for i := 0; i < 26; i++ {
		aheadCnt[i] = make([]int, 27)
	}
	for _, c := range s {
		for j := 0; j < 26; j++ {
			if aheadCnt[j][c-'a'] == 0 {
				aheadCnt[j][c-'a'] = aheadCnt[j][26] // mark the count of the jth letter ahead of the letter c
			}
			if j == int(c-'a') {
				aheadCnt[j][26]++ // count letter c until so far
			}
		}
	}
	ans := 0
	for i := 0; i < 26; i++ {
		for j := 0; j < 26; j++ {
			if aheadCnt[i][j] > 0 && aheadCnt[i][j] < aheadCnt[i][26] {
				if i == j && aheadCnt[i][26] <= 2 {
					continue // a length-3 palindromic subsequences need at least three same letters
				}
				// if the count of the ith letter ahead of the jth letter smaller the total count of the ith letter ahead,
				// they should be length-3 palindromic subsequences
				ans++
			}
		}
	}
	return ans
}

// Problem No.376 Wiggle Subsequence
//
// A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between
// positive and negative. The first difference (if one exists) may be either positive or negative.
// A sequence with one element and a sequence with two non-equal elements are trivially wiggle sequences.
//
// For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3)
// alternate between positive and negative.
// In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences.
// The first is not because its first two differences are positive, and the second is not because its last difference is zero.
// A subsequence is obtained by deleting some elements (possibly zero) from the original sequence,
// leaving the remaining elements in their original order.
//
// Given an integer array nums, return the length of the longest wiggle subsequence of nums.
//
// Example 1:
// 		Input: nums = [1,7,4,9,2,5]
// 		Output: 6
// 		Explanation: The entire sequence is a wiggle sequence with differences (6, -3, 5, -7, 3).
//
// Example 2:
// 		Input: nums = [1,17,5,10,13,15,10,5,16,8]
// 		Output: 7
// 		Explanation: There are several subsequences that achieve this length.
// 		One is [1, 17, 10, 13, 10, 16, 8] with differences (16, -7, 3, -3, 6, -8).
//
// Example 3:
// 		Input: nums = [1,2,3,4,5,6,7,8,9]
// 		Output: 2
//
// Constraints:
// 		1 <= nums.length <= 1000
// 		0 <= nums[i] <= 1000
func wiggleMaxLength(nums []int) int {
	if len(nums) <= 1 {
		return len(nums)
	}
	start := 1
	for start < len(nums) {
		if nums[start]-nums[0] != 0 {
			break
		}
		start++
	}
	if start >= len(nums) {
		return 1
	}
	count, diff := 2, nums[start]-nums[0]
	for i := start + 1; i < len(nums); i++ {
		if nums[i]-nums[i-1] != 0 {
			if (nums[i]-nums[i-1])*diff < 0 {
				count++
			}
			diff = nums[i] - nums[i-1]
		}
	}
	return count
}

func wiggleMaxLength2(nums []int) int {
	upLen, downLen := 1, 1
	for i := 1; i < len(nums); i++ {
		if nums[i] < nums[i-1] {
			downLen = upLen + 1
		}
		if nums[i] > nums[i-1] {
			upLen = downLen + 1
		}
	}
	if upLen > downLen {
		return upLen
	}
	return downLen
}

// Problem No.1898 Maximum Number of Removable Characters
//
// You are given two strings s and p where p is a subsequence of s. You are also given a distinct 0-indexed integer
// array removable containing a subset of indices of s (s is also 0-indexed).
//
// You want to choose an integer k (0 <= k <= removable.length) such that, after removing k characters from s using the
// first k indices in removable, p is still a subsequence of s. More formally, you will mark the character at
// s[removable[i]] for each 0 <= i < k, then remove all marked characters and check if p is still a subsequence.
//
// Return the maximum k you can choose such that p is still a subsequence of s after the removals.
//
// A subsequence of a string is a new string generated from the original string with some characters (can be none)
// deleted without changing the relative order of the remaining characters.
//
// Example 1:
// 		Input: s = "abcacb", p = "ab", removable = [3,1,0]
// 		Output: 2
// 		Explanation: After removing the characters at indices 3 and 1, "abcacb" becomes "accb".
// 		"ab" is a subsequence of "accb".
// 		If we remove the characters at indices 3, 1, and 0, "abcacb" becomes "ccb", and "ab" is no longer a subsequence.
// 		Hence, the maximum k is 2.
//
// Example 2:
// 		Input: s = "abcbddddd", p = "abcd", removable = [3,2,1,4,5,6]
// 		Output: 1
// 		Explanation: After removing the character at index 3, "abcbddddd" becomes "abcddddd".
// 		"abcd" is a subsequence of "abcddddd".
//
// Example 3:
// 		Input: s = "abcab", p = "abc", removable = [0,1,2,3,4]
// 		Output: 0
// 		Explanation: If you remove the first index in the array removable, "abc" is no longer a subsequence.
//
// Constraints:
// 		1 <= p.length <= s.length <= 105
// 		0 <= removable.length < s.length
// 		0 <= removable[i] < s.length
// 		p is a subsequence of s.
// 		s and p both consist of lowercase English letters.
// 		The elements in removable are distinct.
func maximumRemovals(s string, p string, removable []int) int {
	mask := make([]int, len(s))
	for i := 0; i < len(removable); i++ {
		mask[removable[i]] = i + 1
	}
	start, end := 0, len(removable)
	for start < end {
		mid := (start + end) / 2
		if isSubs(s, p, mask, mid) {
			if start == mid {
				if isSubs(s, p, mask, end) {
					start++
				}
				break
			}
			start = mid
		} else {
			end = mid - 1
		}
	}
	return start
}

func isSubs(s string, p string, mask []int, limit int) bool {
	for i, j := 0, 0; i < len(s); i++ {
		if s[i] == p[j] && (mask[i] == 0 || mask[i] > limit) {
			j++
			if j >= len(p) {
				return true
			}
		}
	}
	return false
}

// 2410. Maximum Matching of Players With Trainers
//
// You are given a 0-indexed integer array players, where players[i] represents the ability of the ith player.
// You are also given a 0-indexed integer array trainers, where trainers[j] represents the training capacity of the
// jth trainer.
//
// The ith player can match with the jth trainer if the player's ability is less than or equal to the trainer's
// training capacity. Additionally, the ith player can be matched with at most one trainer, and the jth trainer can be
// matched with at most one player.
//
// Return the maximum number of matchings between players and trainers that satisfy these conditions.
//
// Example 1:
// 		Input: players = [4,7,9], trainers = [8,2,5,8]
// 		Output: 2
// 		Explanation:
// 		One of the ways we can form two matchings is as follows:
// 		- players[0] can be matched with trainers[0] since 4 <= 8.
// 		- players[1] can be matched with trainers[3] since 7 <= 8.
// 		It can be proven that 2 is the maximum number of matchings that can be formed.
//
// Example 2:
// 		Input: players = [1,1,1], trainers = [10]
// 		Output: 1
// 		Explanation:
// 		The trainer can be matched with any of the 3 players.
// 		Each player can only be matched with one trainer, so the maximum answer is 1.
//
// Constraints:
// 		1 <= players.length, trainers.length <= 10^5
// 		1 <= players[i], trainers[j] <= 10^9
func matchPlayersAndTrainers(players []int, trainers []int) int {
	sort.Ints(players)
	sort.Ints(trainers)
	j := 0
	for i := 0; i < len(trainers) && j < len(players); i++ {
		if trainers[i] >= players[j] {
			j++
		}
	}
	return j
}

// Problem No.1186 Maximum Subarray Sum with One Deletion
//
// Given an array of integers, return the maximum sum for a non-empty subarray (contiguous elements) with at most one
// element deletion. In other words, you want to choose a subarray and optionally delete one element from it so that
// there is still at least one element left and the sum of the remaining elements is maximum possible.
//
// Note that the subarray needs to be non-empty after deleting one element.
//
// Example 1:
// 		Input: arr = [1,-2,0,3]
// 		Output: 4
// 		Explanation: Because we can choose [1, -2, 0, 3] and drop -2, thus the subarray [1, 0, 3] becomes the maximum value.
//
// Example 2:
// 		Input: arr = [1,-2,-2,3]
// 		Output: 3
// 		Explanation: We just choose [3] and it's the maximum sum.
//
// Example 3:
// 		Input: arr = [-1,-1,-1,-1]
// 		Output: -1
// 		Explanation: The final subarray needs to be non-empty. You can't choose [-1] and delete -1 from it, then get an empty subarray to make the sum equals to 0.
//
// Constraints:
// 		1 <= arr.length <= 10^5
// 		-10^4 <= arr[i] <= 10^4
//
// Solution
//
// We can use dynamic programming to solve this problem.
// We can turn this problem into another problem as follows.
// Find a subarray A(i) that consists of the first i+1 elements of the original array, and then get the maximum subarray
// (which is the suffix of the A(i)) sum with one deletion (or without deletion), we denote them as S(i,0) and S(i, 1).
// we go through every possible L1 and get the maximum answer of them. And that will be the answer to our original
// problem.
//
// The new problem has an optimal substructure and lapping over sub-problem. If we get the S(i, 0) and the S(i, 1) of
// the A(i), we can easily get the S(i+1, 0) and the S(i+1, 1)of the A(i+1) by following equation:
// 		S(i+1, 0) = max(S(i,0), S(i,0)+a(i), a(i))
// 		S(i+1, 1) = max(S(i,0), S(i,1)+a(i))
//
// Then, we can easily get out solution of the original problem:
// def function
// 		S(0, 0) = arr[0]
// 		S(0, 1) = 0
// 		ans = S(0, 0)
// 		for i from 1 to len(arr)
// 			S(i, 0) = max(S(i-1, 0)+arr[i], arr[i])
// 			S(i, 1) = max(S(i-1, 0), S(i-1, 1)+arr[i])
// 			ans = max(S(i, 0), S(i, 1)) if ans < max(S(i, 0), S(i, 1))
// 		return ans
func maximumSum(arr []int) int {
	ans, deleted, noDeleted := arr[0], 0, arr[0]
	for i := 1; i < len(arr); i++ {
		deleted = max(noDeleted, deleted+arr[i])
		noDeleted = max(arr[i], noDeleted+arr[i])
		ans = max(max(deleted, noDeleted), ans)
	}
	return ans
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// Problem No.1262 Greatest Sum Divisible by Three
//
// Given an integer array nums, return the maximum possible sum of elements of the array such that it is divisible by
// three.
//
// Example 1:
// 		Input: nums = [3,6,5,1,8]
// 		Output: 18
// 		Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
//
// Example 2:
// 		Input: nums = [4]
// 		Output: 0
// 		Explanation: Since 4 is not divisible by 3, do not pick any number.
//
// Example 3:
// 		Input: nums = [1,2,3,4,4]
// 		Output: 12
// 		Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
//
// Constraints:
// 		1 <= nums.length <= 4 * 10^4
// 		1 <= nums[i] <= 10^4
func maxSumDivThree(nums []int) int {
	maxTable := [][]int{{0, 0, 0}, {0, 0, 0}}
	for j, num := range nums {
		last, curr := (j+1)%2, j%2
		for i := 0; i < 3; i++ {
			remainder := (i + num) % 3
			if maxTable[last][i]%3 == i && maxTable[last][remainder] < maxTable[last][i]+num {
				maxTable[curr][remainder] = maxTable[last][i] + num
			} else {
				maxTable[curr][remainder] = maxTable[last][remainder]
			}
		}
	}
	if maxTable[0][0] > maxTable[1][0] {
		return maxTable[0][0]
	}
	return maxTable[1][0]
}

// Problem No.837 New 21 Game
//
// Alice plays the following game, loosely based on the card game "21".
//
// Alice starts with 0 points and draws numbers while she has less than k points. During each draw, she gains an integer
// number of points randomly from the range [1, maxPts], where maxPts is an integer. Each draw is independent and the
// outcomes have equal probabilities.
//
// Alice stops drawing numbers when she gets k or more points.
//
// Return the probability that Alice has n or fewer points.
//
// Answers within 10-5 of the actual answer are considered accepted.
//
//
//
// Example 1:
// 		Input: n = 10, k = 1, maxPts = 10
// 		Output: 1.00000
// 		Explanation: Alice gets a single card, then stops.
//
// Example 2:
// 		Input: n = 6, k = 1, maxPts = 10
// 		Output: 0.60000
// 		Explanation: Alice gets a single card, then stops.
// 		In 6 out of 10 possibilities, she is at or below 6 points.
//
// Example 3:
// 		Input: n = 21, k = 17, maxPts = 10
// 		Output: 0.73278
//
// Constraints:
// 		0 <= k <= n <= 10^4
// 		1 <= maxPts <= 10^4
func new21Game(n int, k int, maxPts int) float64 {
	if n-k+1 >= maxPts || k == 0 {
		return 1
	}
	ps := make([]float64, n+1)
	ps[0] = 1
	W, pSum, ans := float64(maxPts), 1.0, 0.0
	for i := 1; i <= n; i++ {
		ps[i] = pSum / W
		if i < k {
			pSum += ps[i]
		} else {
			ans += ps[i]
		}
		if i >= maxPts {
			pSum -= ps[i-maxPts]
		}
	}
	return ans
}
