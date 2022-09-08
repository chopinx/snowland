package base

import (
	"errors"
	"math/rand"
)

type Node struct {
	Level int
	Right *DataNode
	Down  *DataNode
}

type DataNode struct {
	Node
	Value int
}

type SkipList struct {
	head  []*DataNode
	level int
	size  int
}

// NewSkipList Build and init a skip list with a given list
func NewSkipList(dataList ...int) *SkipList {
	skipList := &SkipList{
		head:  []*DataNode{},
		level: 1,
		size:  0,
	}
	for i := 0; i < len(dataList); i++ {
		skipList.Insert(dataList[i])
	}
	return skipList
}

func (s *SkipList) raiseLevel() {
	defer func() { s.level++ }()
	s.head = append(s.head, &DataNode{
		Node: Node{
			Level: s.level,
			Right: nil,
			Down:  s.head[s.level-1],
		},
		Value: s.head[0].Value,
	})
	lastNode := s.head[s.level]
	downNode := s.head[s.level-1].Right
	for downNode != nil {
		if rand.Int()%2 == 0 {
			newNode := &DataNode{
				Node: Node{
					Level: s.level,
					Right: lastNode.Right,
					Down:  downNode,
				},
				Value: downNode.Value,
			}
			lastNode.Right = newNode
			lastNode = newNode
		}
		downNode = downNode.Right
	}
}

func (s *SkipList) lowerLevel() {
	s.head = s.head[:s.level-1]
	s.level--
}

// Insert insert a data in O(log(n)) time cost
func (s *SkipList) Insert(data int) {
	defer func() { s.size++ }()
	if s.size+1 > 2<<(s.level-1) {
		s.raiseLevel()
	}
	if s.size == 0 {
		s.head = append(s.head, &DataNode{
			Node: Node{
				Level: 0,
				Right: nil,
				Down:  nil,
			},
			Value: data,
		})
		s.level = 1
		return
	}
	currLevel := s.level - 1
	currNode := s.head[s.level-1]
	prepNodeList := make([]*DataNode, s.level)
	if currNode.Value >= data {
		// data is smaller than the minimum value of current skip list
		upFlag := true
		for i := 0; i < s.level; i++ {
			prepNodeList[i] = &DataNode{
				Node: Node{
					Level: i,
					Right: nil,
					Down:  nil,
				},
				Value: data,
			}
			if i == 0 || (rand.Int()%2 == 0 && upFlag) {
				prepNodeList[i].Right = s.head[i]
			} else {
				upFlag = false
				prepNodeList[i].Right = s.head[i].Right
			}
			if i > 0 {
				prepNodeList[i].Down = prepNodeList[i-1]
			}
		}
		s.head = prepNodeList
		return
	}
	for currLevel >= 0 {
		for currNode.Right != nil && currNode.Right.Value < data {
			currNode = currNode.Right
		}
		prepNodeList[currLevel] = currNode
		currLevel--
		currNode = currNode.Down
	}
	var downNode *DataNode
	for i := 0; i < s.level; i++ {
		if i == 0 || rand.Int()%2 == 0 {
			newNode := &DataNode{
				Node: Node{
					Level: i,
					Right: prepNodeList[i].Right,
					Down:  downNode,
				},
				Value: data,
			}
			prepNodeList[i].Right = newNode
			downNode = newNode
		} else {
			break
		}
	}
}

// Remove search a data in skip list, and remove it if it exists
func (s *SkipList) Remove(data int) (err error) {
	defer func() {
		if err == nil {
			s.size--
		}
	}()
	if s.size <= 0 {
		err = errors.New("data not found")
		return
	}
	if s.size == 1 {
		if s.head[0].Value == data {
			s.head = s.head[:0]
		} else {
			err = errors.New("data not found")
		}
		return
	}
	currLevel := s.level - 1
	currNode := s.head[s.level-1]
	if currNode.Value == data {
		newHead := make([]*DataNode, s.level)
		newHead[0] = s.head[0].Right
		for i := 1; i < s.level; i++ {
			if s.head[i].Right != nil && s.head[i].Right.Down == newHead[i-1] {
				newHead[i] = s.head[i].Right
			} else {
				newHead[i] = &DataNode{
					Node: Node{
						Level: i,
						Right: s.head[i].Right,
						Down:  newHead[i-1],
					},
					Value: newHead[0].Value,
				}
			}
		}
		s.head = newHead
		return
	}
	prepNodeList := make([]*DataNode, s.level)
	found := false
	for currLevel >= 0 {
		for currNode.Right != nil && currNode.Right.Value < data {
			currNode = currNode.Right
		}
		if currNode.Right != nil && currNode.Right.Value == data {
			found = true
			currNode.Right = currNode.Right.Right
		}
		prepNodeList[currLevel] = currNode
		currLevel--
		currNode = currNode.Down
	}
	if !found {
		err = errors.New("data not found")
	}
	return
}

// Find search a data in skip list, and return if it exists
func (s *SkipList) Find(data int) bool {
	if s.size <= 0 {
		return false
	}
	currLevel := s.level - 1
	currNode := s.head[s.level-1]
	if currNode.Value == data {
		return true
	}
	for currLevel >= 0 {
		for currNode.Right != nil && currNode.Right.Value < data {
			currNode = currNode.Right
		}
		if currNode.Right != nil && currNode.Right.Value == data {
			return true
		}
		currLevel--
		currNode = currNode.Down
	}
	return false
}

func (s *SkipList) GetDataList() []int {
	if s.size <= 0 {
		return []int{}
	}
	dataList := make([]int, s.size)
	index := 0
	currNode := s.head[0]
	for currNode != nil {
		if index >= s.size {
			return dataList
		}
		dataList[index] = currNode.Value
		index++
		currNode = currNode.Right
	}
	return dataList
}

func (s *SkipList) Size() int {
	return s.size
}

func (s *SkipList) Check() bool {
	for _, node := range s.head {
		for node != nil {
			if node.Right != nil {
				if node.Right.Value < node.Value {
					return false
				}
			}
			currNode := node
			for currNode != nil {
				if currNode.Down != nil {
					if currNode.Down.Value != currNode.Value {
						return false
					}
				}
				currNode = currNode.Down
			}
			node = node.Right
		}
	}
	return true
}

func (s *SkipList) GetMin() (int, error) {
	if s.size <= 0 {
		return 0, errors.New("list is empty")
	}
	return s.head[0].Value, nil
}
