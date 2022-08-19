package snowland

import (
	"math"
	"sort"
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
