package snowland

import (
	"fmt"
	"math"
	"sort"
	"strconv"
	"strings"
)

// Problem No.939 Minimum Area Rectangle
type xCoord int
type yCoord int

type XCoords []xCoord

func (xs XCoords) Less(i, j int) bool {
	return xs[i] < xs[j]
}
func (xs XCoords) Len() int {
	return len(xs)
}

func (xs XCoords) Swap(i, j int) {
	tmp := xs[j]
	xs[j] = xs[i]
	xs[i] = tmp
}

type YCoords []yCoord

func (xs YCoords) Less(i, j int) bool {
	return xs[i] < xs[j]
}
func (xs YCoords) Len() int {
	return len(xs)
}

func (xs YCoords) Swap(i, j int) {
	tmp := xs[j]
	xs[j] = xs[i]
	xs[i] = tmp
}

type PointsPool struct {
	points   [][]int
	pointSet map[xCoord]map[yCoord]bool
	XAxisMap map[yCoord]XCoords
	YAxisMap map[xCoord]YCoords
}

func minAreaRect(points [][]int) int {
	pool := NewPointsPool(points)
	minArea := 0
	for y, xCoords := range pool.XAxisMap {
		// iterate through all points by y-axis, get a set of points for each y value
		if len(xCoords) < 2 {
			// if the points with same y are less than 2, there is no chance to get a rectangle
			continue
		}
		for i := range xCoords {
			x := xCoords[i]
			for j := i + 1; j < len(xCoords); j++ {
				// iterate through all other points with the same y coordinate as current point
				xRight := xCoords[j]
				xLen := xRight - x
				yCoordsInX := pool.GetYAxisPoints(x)
				for k := range yCoordsInX {
					// iterate through all other points with the same x coordinate as current point
					yDown := yCoordsInX[k]
					if yDown >= y || !pool.Check(xRight, yDown) {
						// if you get three the vertices of a rectangle,
						// then you can calculate the coordinates of the last vertex
						// so check if it exists
						continue
					}
					yLen := y - yDown
					area := int(xLen) * int(yLen)
					if area < minArea || minArea == 0 {
						minArea = area
					}
					if minArea == 1 {
						return minArea
					}
				}
			}
		}
	}
	return minArea
}

func NewPointsPool(points [][]int) *PointsPool {
	pool := &PointsPool{
		points:   points,
		pointSet: make(map[xCoord]map[yCoord]bool),
		XAxisMap: map[yCoord]XCoords{},
		YAxisMap: map[xCoord]YCoords{},
	}
	pool.Init(points)
	return pool
}

// Init points pool with a list of points
func (p *PointsPool) Init(points [][]int) {
	for i := range points {
		x, y := xCoord(points[i][0]), yCoord(points[i][1])
		if pl, ok := p.pointSet[x]; ok {
			pl[y] = true
		} else {
			p.pointSet[x] = make(map[yCoord]bool)
			p.pointSet[x][y] = true
		}

		if _, ok := p.YAxisMap[x]; !ok {
			p.YAxisMap[x] = make([]yCoord, 0)
		}
		p.YAxisMap[x] = append(p.YAxisMap[x], y)
		if _, ok := p.XAxisMap[y]; !ok {
			p.XAxisMap[y] = make([]xCoord, 0)
		}
		p.XAxisMap[y] = append(p.XAxisMap[y], x)
	}
	for _, xCoords := range p.XAxisMap {
		sort.Sort(xCoords)
	}
	for _, yCoords := range p.YAxisMap {
		sort.Sort(yCoords)
	}
}

// Check if the specific point is inside the pool
func (p *PointsPool) Check(x xCoord, y yCoord) bool {
	if _, ok := p.pointSet[x]; !ok {
		return false
	}
	if _, ok := p.pointSet[x][y]; !ok {
		return false
	}
	return true
}

// GetXAxisPoints func find all points which have the given y coordinate, and return their x coordinates
func (p *PointsPool) GetXAxisPoints(y yCoord) XCoords {
	if _, ok := p.XAxisMap[y]; !ok {
		return []xCoord{}
	}
	return p.XAxisMap[y]
}

// GetYAxisPoints func find all points which have the given x coordinate, and return their y coordinates
func (p *PointsPool) GetYAxisPoints(x xCoord) YCoords {
	if _, ok := p.YAxisMap[x]; !ok {
		return []yCoord{}
	}
	return p.YAxisMap[x]
}

// Problem No.239 Sliding Window Maximum

func maxSlidingWindow(nums []int, k int) []int {
	return TmpTableMaxSlidingWindow{}.maxSlidingWindow(nums, k)
}

type MaxSlidingWindow interface {
	maxSlidingWindow([]int, int) []int
}

type TmpTableMaxSlidingWindow struct {
}

func (TmpTableMaxSlidingWindow) maxSlidingWindow(nums []int, k int) []int {
	// fmt.Println(nums)
	maxList := make([]int, len(nums))
	maxList[0] = nums[0]
	tmpTable := make([]int, len(nums))
	tmpTable[0] = nums[0]
	for i := 1; i < len(nums); i++ {
		tmpTable[i] = math.MinInt
	}
	for i := 1; i < len(nums); i++ {
		n := nums[i]
		if (i >= k && n > tmpTable[i-k+1]) || (i < k && n > tmpTable[0]) {
			maxList[i] = n
		} else if i >= k {
			maxList[i] = tmpTable[i-k+1]
		} else {
			maxList[i] = tmpTable[0]
		}
		for j := 0; i-j >= 0 && j < k; j++ {
			if tmpTable[i-j] < n {
				tmpTable[i-j] = n
			} else {
				break
			}
		}
		// fmt.Printf("i=%d, tmp: %v\t", i, tmpTable)
		// fmt.Printf("max: %v\n", maxList)
	}
	return maxList[k-1:]
}

type HeapMaxSlidingWindow struct {
}

func (m HeapMaxSlidingWindow) maxSlidingWindow(nums []int, k int) []int {
	// TODO implement the algorithm with a red-black tree
	return nil
}

// Problem No.1984 Minimum Difference Between Highest and Lowest of K Scores.
//
// I think if we want to minimize the difference between the largest score and the lowest score of any k students,
// we should select k adjacent elements in the increasing ordered list,
// such as the block array[i:i+k-1] in the ordered list. So we should sort the integer array in increasing order first.
// We will keep a variable named MinDiff initialized with the difference between the largest score and
// the lowest score of the entire scores array which is bigger than any possible differences.
// Then, we can go through the echo element Si with index i in the ordered list,
// which corresponds to the block array[i:i+k-1]. For k scores in the block array[i:i+k-1],
// the difference between the largest score and the lowest score is array[i+k-1]-array[i].
// If the max difference within the block array[i:i+k-1] is smaller than the MinDiff,
// replace the value of MinDiff with the smaller one.
// After the traverse, we will get the result.
func minimumDifference(nums []int, k int) int {
	sort.Ints(nums)
	minDiff := nums[len(nums)-1] - nums[0]
	for i := 0; i < len(nums)-k+1; i++ {
		if nums[i+k-1]-nums[i] < minDiff {
			minDiff = nums[i+k-1] - nums[i]
		}
	}
	return minDiff
}

// Problem No.1019 Next Greater Node In Linked List
//
// First, we should go through the echo elements in the linked list from its head. Meanwhile,
// we should keep a new linked list for all elements whose greater node haven't been found yet,
// which named WaitList. Obviously, WaitList is increasing ordered.
// During the traverse, for element u, if its value is greater than the one right before it,
// we should go through the WaitList until the next node's value is not greater than u.
// All nodes  in the WaitList that we went through in this iteration found their greater node now,
// node u. And we set node u to be the new head of the WaitList which followed by the rest nodes left in the WaitList.
// On the other hand, for element u, if its value is not greater than the one right before it,
// we just need to add it to the head of the WaitList.
// After the traverse, we will get all needed result.

type ListNode struct {
	Val  int
	Next *ListNode
}

type ListWait struct {
	Node  *ListNode
	Index int
	Next  *ListWait
}

func nextLargerNodes(head *ListNode) []int {
	node := head.Next
	result := []int{0}
	waitList := &ListWait{head, 0, nil}
	index := 1
	for node != nil {
		if node.Val > waitList.Node.Val {
			subNode := waitList
			for subNode != nil {
				if subNode.Node.Val < node.Val {
					result[subNode.Index] = node.Val
					waitList = subNode.Next
					subNode = subNode.Next
				} else {
					break
				}
			}
		}
		waitList = &ListWait{node, index, waitList}
		result = append(result, 0)
		index++
		node = node.Next
	}
	return result
}

// Problem No.726 Number of Atoms
//
func countOfAtoms(formula string) string {
	var flagList []int
	stack := make([]int, 0)
	parenthesesMap := make(map[int]int)
	for i := 0; i < len(formula); i++ {
		if formula[i] >= 'A' && formula[i] <= 'Z' {
			flagList = append(flagList, i)
		}
		if formula[i] == '(' {
			flagList = append(flagList, i)
			stack = append(stack, len(flagList)-1)
		}
		if formula[i] == ')' {
			flagList = append(flagList, i)
			parenthesesMap[stack[len(stack)-1]] = len(flagList) - 1
			stack = stack[:len(stack)-1]
		}
		if formula[i] >= '0' && formula[i] <= '9' && (formula[i-1] < '0' || formula[i-1] > '9') {
			flagList = append(flagList, i)
		}
	}
	flagList = append(flagList, len(formula))
	countMap := count(formula, flagList, 0, parenthesesMap)
	var atomList []string
	for k := range countMap {
		atomList = append(atomList, k)
	}
	sort.Strings(atomList)
	var result strings.Builder
	for i := range atomList {
		_, _ = fmt.Fprint(&result, atomList[i])
		if countMap[atomList[i]] > 1 {
			_, _ = fmt.Fprint(&result, strconv.Itoa(countMap[atomList[i]]))
		}
	}
	return result.String()
}

func count(formula string, flagList []int, flagOffset int, parenthesesMap map[int]int) map[string]int {
	countMap := make(map[string]int)
	for i := 0; i < len(flagList)-1 && flagList[i] < len(formula); i++ {
		key := formula[flagList[i]:flagList[i+1]]
		nextKey := ""
		if i+1 < len(flagList)-1 {
			nextKey = formula[flagList[i+1]:flagList[i+2]]
		}
		if key[0] >= 'A' && key[0] <= 'Z' {
			if _, ok := countMap[key]; ok {
				countMap[key] += 1
			} else {
				countMap[key] = 1
			}
			if len(nextKey) > 0 && nextKey[0] >= '0' && nextKey[0] <= '9' {
				times, _ := strconv.Atoi(nextKey)
				countMap[key] += times - 1
				i++
			}
		} else if key[0] == '(' {
			rightParenthesesFlagIndex := parenthesesMap[i+flagOffset] - flagOffset
			subMap := count(formula, flagList[i+1:rightParenthesesFlagIndex+2], flagOffset+i+1, parenthesesMap)
			nextIndex := flagList[rightParenthesesFlagIndex] + 1
			i = rightParenthesesFlagIndex
			if nextIndex < len(formula) && formula[nextIndex] >= '0' && formula[nextIndex] <= '9' {
				nextKey = formula[flagList[rightParenthesesFlagIndex]+1 : flagList[rightParenthesesFlagIndex+2]]
				times, _ := strconv.Atoi(nextKey)
				for k := range subMap {
					subMap[k] *= times
				}
				i++
			}
			for k, subV := range subMap {
				if _, ok := countMap[k]; ok {
					countMap[k] += subV
				} else {
					countMap[k] = subV
				}
			}

		}
	}
	return countMap
}

// Problem No.1615 Maximal Network Rank
//
// There is an infrastructure of n cities with some number of roads connecting these cities.
// Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.
//
// The network rank of two different cities is defined as the total number of directly connected roads to either city.
// If a road is directly connected to both cities, it is only counted once.
//
// The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.
//
// Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.
//
// The degree of a city is the number of roads connected to it.
// For any pair of different cities, such as a and b, the degree of them are Da and Db,
// the rank of the pair must be neither Da+Db nor Da+Db, which depends on if there is a bidirectional road between them.
// So we can sort cities by their degree in descending order. Then we can get the top 2 cities with the highest degree.
// Assume the sum of the degree of the top 2 cities is D,
// the maximal network rank of the entire infrastructure is neither D nor D-1,
// depends on if there is a bidirectional road between the top 2 cities.
// There are maybe more than one pairs of cities, whose sum of degree equals to D,
// we have to check each of them to find out if there is any pair with no bidirectional road.
// If it's yes, then the answer is D, otherwise it's D-1
func maximalNetworkRank(n int, roads [][]int) int {
	degrees := make([]int, n)
	roadMap := make(map[int]map[int]bool)
	maxDegreeList := make([]int, 0)
	maxDegree, secondDegree := 0, 0
	secondDegreeList := make([]int, 0)
	for i := 0; i < len(roads); i++ {
		degrees[roads[i][0]]++
		degrees[roads[i][1]]++
		smaller, bigger := roads[i][0], roads[i][1]
		if smaller > bigger {
			smaller, bigger = bigger, smaller
		}
		if _, ok := roadMap[smaller]; !ok {
			roadMap[smaller] = make(map[int]bool)
		}
		roadMap[smaller][bigger] = true
	}
	for i := 0; i < len(degrees); i++ {
		currDegree := degrees[i]
		if currDegree > maxDegree {
			secondDegree = maxDegree
			maxDegree = currDegree
			secondDegreeList = maxDegreeList
			maxDegreeList = []int{i}
		} else if currDegree == maxDegree {
			maxDegreeList = append(maxDegreeList, i)
		} else if currDegree > secondDegree {
			secondDegree = currDegree
			secondDegreeList = []int{i}
		} else if currDegree == secondDegree {
			secondDegreeList = append(secondDegreeList, i)
		}
	}
	if len(maxDegreeList) > 1 {
		for i := 0; i < len(maxDegreeList); i++ {
			for j := i + 1; j < len(maxDegreeList); j++ {
				smaller, bigger := maxDegreeList[i], maxDegreeList[j]
				if smaller > bigger {
					smaller, bigger = bigger, smaller
				}
				if _, ok := roadMap[smaller]; !ok {
					return maxDegree * 2
				}
				if _, ok := roadMap[smaller][bigger]; !ok {
					return maxDegree * 2
				}
			}
		}
		return maxDegree*2 - 1
	} else {
		for i := 0; i < len(secondDegreeList); i++ {
			smaller, bigger := maxDegreeList[0], secondDegreeList[i]
			if smaller > bigger {
				smaller, bigger = bigger, smaller
			}
			if _, ok := roadMap[smaller]; !ok {
				return maxDegree + secondDegree
			}
			if _, ok := roadMap[smaller][bigger]; !ok {
				return maxDegree + secondDegree
			}
		}
		return maxDegree + secondDegree - 1
	}
}

// Problem No.378 Kth Smallest Element in a Sorted Matrix
//
// Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.
// Note that it is the kth smallest element in the sorted order, not the kth distinct element.
// You must find a solution with a memory complexity better than O(n2).
//
// Example 1:
//	Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
// 	Output: 13
// 	Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
//
// Example 2:
// Input: matrix = [[-5]], k = 1
// Output: -5
//
// Constraints:
// 	n == matrix.length == matrix[i].length
// 	1 <= n <= 300
// 	-10^9 <= matrix[i][j] <= 10^9
// 	All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
// 	1 <= k <= n2
func kthSmallest(matrix [][]int, k int) int {
	var h Heap
	n := len(matrix)
	if k <= n*n/2 {
		minHeap := &MinHeap{
			BaseHeap{
				Matrix:    matrix,
				IndexList: []int{0},
				N:         n,
			},
		}
		minHeap.Heap = minHeap
		h = minHeap
	} else {
		maxHeap := &MaxHeap{
			BaseHeap{
				Matrix:    matrix,
				IndexList: []int{0},
				N:         n,
			},
		}
		maxHeap.Heap = maxHeap
		h = maxHeap
		k = n*n + 1 - k
	}
	size := 0
	visitedMap := map[int]bool{0: true}
	for true {
		index, value := h.Pop()
		size++
		if size == k {
			return value
		}
		tryPush(visitedMap, index+1, h)
		tryPush(visitedMap, index+n, h)
		tryPush(visitedMap, index+n+1, h)
	}
	return 0
}

func tryPush(visitedMap map[int]bool, index int, h Heap) {
	if index < h.GetN()*h.GetN() && !isVisited(visitedMap, index) {
		h.Push(index)
		visitedMap[index] = true
	}
}

func isVisited(visitedMap map[int]bool, index int) bool {
	_, ok := visitedMap[index]
	return ok
}

type Heap interface {
	Len() int
	Less(i, j int) bool
	Swap(i, j int)
	Push(int)
	Pop() (index int, value int)
	GetValue(int) int
	GetN() int
}

type BaseHeap struct {
	Heap
	Matrix    [][]int
	IndexList []int
	N         int
}

func (h BaseHeap) GetN() int {
	return h.N
}

type MaxHeap struct {
	BaseHeap
}

type MinHeap struct {
	BaseHeap
}

func (h MaxHeap) GetValue(index int) int {
	return h.Matrix[h.GetN()-1-index/h.GetN()][h.GetN()-1-index%h.GetN()]
}

func (h MinHeap) GetValue(index int) int {
	return h.Matrix[index/h.GetN()][index%h.GetN()]
}

func (h MaxHeap) Less(i, j int) bool {
	return h.GetValue(h.IndexList[i]) > h.GetValue(h.IndexList[j])
}

func (h BaseHeap) Len() int { return len(h.IndexList) }
func (h MinHeap) Less(i, j int) bool {
	return h.GetValue(h.IndexList[i]) < h.GetValue(h.IndexList[j])
}
func (h BaseHeap) Swap(i, j int) { h.IndexList[i], h.IndexList[j] = h.IndexList[j], h.IndexList[i] }

func (h *BaseHeap) Push(x int) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	h.IndexList = append(h.IndexList, x)
	currIndex := len(h.IndexList) - 1
	for currIndex > 0 && h.Heap.Less(currIndex, (currIndex-1)/2) {
		h.Heap.Swap(currIndex, (currIndex-1)/2)
		currIndex = (currIndex - 1) / 2
	}
}

func (h *BaseHeap) Pop() (index int, value int) {
	old := h.IndexList
	n := len(old)
	index, value = old[0], h.Heap.GetValue(old[0])
	old[0] = old[n-1]
	h.IndexList = old[0 : n-1]
	for i := 0; i < len(h.IndexList); {
		left := i*2 + 1
		smaller := i*2 + 2
		if smaller >= len(h.IndexList) || h.Heap.Less(left, smaller) {
			smaller = left
		}
		if smaller >= len(h.IndexList) || !h.Heap.Less(smaller, i) {
			break
		}
		h.Heap.Swap(i, smaller)
		i = smaller
	}
	return index, value
}

// Problem No.2206. Divide Array Into Equal Pairs
//
// You are given an integer array nums consisting of 2 * n integers.
// You need to divide nums into n pairs such that:
// 	Each element belongs to exactly one pair.
// 	The elements present in a pair are equal.
// 	Return true if nums can be divided into n pairs, otherwise return false.
//
// Example 1:
//
// Input: nums = [3,2,3,2,2,2]
// Output: true
// Explanation:
// There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
// If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.
// Example 2:
//
// Input: nums = [1,2,3,4]
// Output: false
// Explanation:
// There is no way to divide nums into 4 / 2 = 2 pairs such that the pairs satisfy every condition.
//
//
// Constraints:
//
// nums.length == 2 * n
// 1 <= n <= 500
// 1 <= nums[i] <= 500
func divideArray(nums []int) bool {
	bitMap := make([]int, 501/strconv.IntSize+1)
	for i := 0; i < len(nums); i++ {
		bitMap[nums[i]/strconv.IntSize] = bitMap[nums[i]/strconv.IntSize] ^ 1<<(nums[i]%strconv.IntSize)
	}
	for i := 0; i < len(bitMap); i++ {
		if bitMap[i] != 0 {
			return false
		}
	}
	return true
}
