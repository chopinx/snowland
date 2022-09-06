package snowland

import "sort"

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
// where n=max(abs(xa-xb),abs(ya-yb)). Because when you take a step, you're either descending the distance in x-axis,
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
