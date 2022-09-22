package main

import (
	"reflect"
	"testing"
)

func Test_minAreaRect(t *testing.T) {
	type args struct {
		points [][]int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "case1",
			args: args{
				points: [][]int{{1, 1}, {1, 3}, {3, 1}, {3, 3}, {2, 2}},
			},
			want: 4,
		},
		{
			name: "case1",
			args: args{
				points: [][]int{{1, 1}, {1, 3}, {3, 1}, {3, 3}, {2, 2}, {2, 1}, {3, 2}},
			},
			want: 1,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := minAreaRect(tt.args.points); got != tt.want {
				t.Errorf("minAreaRect() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestNewPointsPool(t *testing.T) {
	type args struct {
		points [][]int
	}
	tests := []struct {
		name string
		args args
		want *PointsPool
	}{
		{
			name: "case1",
			args: args{
				points: [][]int{{1, 1}, {0, 0}, {1, 0}, {0, 1}},
			},
			want: &PointsPool{
				points: [][]int{{1, 1}, {0, 0}, {1, 0}, {0, 1}},
				pointSet: map[xCoord]map[yCoord]bool{
					1: {1: true, 0: true},
					0: {0: true, 1: true},
				},
				XAxisMap: map[yCoord]XCoords{0: {0, 1}, 1: {0, 1}},
				YAxisMap: map[xCoord]YCoords{0: {0, 1}, 1: {0, 1}},
			},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := NewPointsPool(tt.args.points); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("NewPointsPool() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestPointsPool_Check(t *testing.T) {
	type fields struct {
		points   [][]int
		pointSet map[xCoord]map[yCoord]bool
		xAxisMap map[yCoord]XCoords
		yAxisMap map[xCoord]YCoords
	}
	type args struct {
		x xCoord
		y yCoord
	}
	baseFields := fields{
		points: [][]int{{1, 1}, {0, 0}, {1, 0}, {0, 1}},
		pointSet: map[xCoord]map[yCoord]bool{
			1: {1: true, 0: true},
			0: {0: true, 1: true},
		},
		xAxisMap: map[yCoord]XCoords{0: {0, 1}, 1: {0, 1}},
		yAxisMap: map[xCoord]YCoords{0: {0, 1}, 1: {0, 1}},
	}
	tests := []struct {
		name   string
		fields fields
		args   args
		want   bool
	}{
		{
			name:   "case1",
			fields: baseFields,
			args: args{
				x: 1,
				y: 1,
			},
			want: true,
		},
		{
			name:   "case2",
			fields: baseFields,
			args: args{
				x: 0,
				y: 1,
			},
			want: true,
		},
		{
			name:   "case3",
			fields: baseFields,
			args: args{
				x: 2,
				y: 1,
			},
			want: false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			p := &PointsPool{
				points:   tt.fields.points,
				pointSet: tt.fields.pointSet,
				XAxisMap: tt.fields.xAxisMap,
				YAxisMap: tt.fields.yAxisMap,
			}
			if got := p.Check(tt.args.x, tt.args.y); got != tt.want {
				t.Errorf("Check() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestPointsPool_GetXAxisPoints(t *testing.T) {
	type fields struct {
		points   [][]int
		pointSet map[xCoord]map[yCoord]bool
		xAxisMap map[yCoord]XCoords
		yAxisMap map[xCoord]YCoords
	}
	type args struct {
		y yCoord
	}
	baseFields := fields{
		points: [][]int{{1, 1}, {0, 0}, {1, 0}, {0, 1}},
		pointSet: map[xCoord]map[yCoord]bool{
			1: {1: true, 0: true},
			0: {0: true, 1: true},
		},
		xAxisMap: map[yCoord]XCoords{0: {0, 1}, 1: {0, 1}},
		yAxisMap: map[xCoord]YCoords{0: {0, 1}, 1: {0, 1}},
	}
	tests := []struct {
		name   string
		fields fields
		args   args
		want   XCoords
	}{
		{
			name:   "case1",
			fields: baseFields,
			args: args{
				y: 0,
			},
			want: XCoords{0, 1},
		},
		{
			name:   "case2",
			fields: baseFields,
			args: args{
				y: 1,
			},
			want: XCoords{0, 1},
		},
		{
			name:   "case3",
			fields: baseFields,
			args: args{
				y: 2,
			},
			want: XCoords{},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			p := &PointsPool{
				points:   tt.fields.points,
				pointSet: tt.fields.pointSet,
				XAxisMap: tt.fields.xAxisMap,
				YAxisMap: tt.fields.yAxisMap,
			}
			if got := p.GetXAxisPoints(tt.args.y); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("GetXAxisPoints() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestPointsPool_GetYAxisPoints(t *testing.T) {
	type fields struct {
		points   [][]int
		pointSet map[xCoord]map[yCoord]bool
		xAxisMap map[yCoord]XCoords
		yAxisMap map[xCoord]YCoords
	}
	type args struct {
		x xCoord
	}
	baseFields := fields{
		points: [][]int{{1, 1}, {0, 0}, {1, 0}, {0, 1}},
		pointSet: map[xCoord]map[yCoord]bool{
			1: {1: true, 0: true},
			0: {0: true, 1: true},
		},
		xAxisMap: map[yCoord]XCoords{0: {0, 1}, 1: {1, 0}},
		yAxisMap: map[xCoord]YCoords{0: {0, 1}, 1: {1, 0}},
	}
	tests := []struct {
		name   string
		fields fields
		args   args
		want   YCoords
	}{
		{
			name:   "case1",
			fields: baseFields,
			args: args{
				x: 0,
			},
			want: YCoords{0, 1},
		},
		{
			name:   "case2",
			fields: baseFields,
			args: args{
				x: 1,
			},
			want: YCoords{1, 0},
		},
		{
			name:   "case3",
			fields: baseFields,
			args: args{
				x: 2,
			},
			want: YCoords{},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			p := &PointsPool{
				points:   tt.fields.points,
				pointSet: tt.fields.pointSet,
				XAxisMap: tt.fields.xAxisMap,
				YAxisMap: tt.fields.yAxisMap,
			}
			if got := p.GetYAxisPoints(tt.args.x); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("GetYAxisPoints() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_maxSlidingWindow(t *testing.T) {
	type args struct {
		nums []int
		k    int
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		{
			name: "case1",
			args: args{
				nums: []int{1},
				k:    1,
			},
			want: []int{1},
		}, {
			name: "case2",
			args: args{
				nums: []int{1, 3, -1, -3, 5, 3, 6, 7},
				k:    3,
			},
			want: []int{3, 3, 5, 5, 6, 7},
		}, {
			name: "case3",
			args: args{
				nums: []int{1, 3, 1, 2, 0, 5},
				k:    3,
			},
			want: []int{3, 3, 2, 5},
		}, {
			name: "case4",
			args: args{
				nums: []int{1, 2, 3, 4, 5, 6, 7, 8},
				k:    3,
			},
			want: []int{3, 4, 5, 6, 7, 8},
		}, {
			name: "case5",
			args: args{
				nums: []int{1, -1},
				k:    1,
			},
			want: []int{1, -1},
		}, {
			name: "case6",
			args: args{
				nums: []int{7, 2, 4},
				k:    2,
			},
			want: []int{7, 4},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := maxSlidingWindow(tt.args.nums, tt.args.k); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("maxSlidingWindow() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_minimumDifference(t *testing.T) {
	type args struct {
		nums []int
		k    int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "single",
			args: args{
				nums: []int{9},
				k:    1,
			},
			want: 0,
		},
		{
			name: "sample",
			args: args{
				nums: []int{1, 2, 4, 8},
				k:    2,
			},
			want: 1,
		},
		{
			name: "sample",
			args: args{
				nums: []int{1, 9, 4, 8},
				k:    3,
			},
			want: 5,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := minimumDifference(tt.args.nums, tt.args.k); got != tt.want {
				t.Errorf("minimumDifference() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_nextLargerNodes(t *testing.T) {
	type args struct {
		head *ListNode
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		{
			name: "sample",
			args: args{
				head: &ListNode{2, &ListNode{1, &ListNode{5, nil}}},
			},
			want: []int{5, 5, 0},
		},
		{
			name: "sample1",
			args: args{
				head: &ListNode{2, &ListNode{7, &ListNode{4, &ListNode{3, &ListNode{5, &ListNode{9, nil}}}}}},
			},
			want: []int{7, 9, 5, 5, 9, 0},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := nextLargerNodes(tt.args.head); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("nextLargerNodes() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_count(t *testing.T) {
	type args struct {
		formula        string
		flagList       []int
		flagOffset     int
		parenthesesMap map[int]int
	}
	tests := []struct {
		name string
		args args
		want map[string]int
	}{
		{
			name: "sample",
			args: args{
				formula:        "H2O",
				flagList:       []int{0, 1, 2, 3},
				parenthesesMap: map[int]int{},
			},
			want: map[string]int{"H": 2, "O": 1},
		},
		{
			name: "sample2",
			args: args{
				formula:        "H2O2",
				flagList:       []int{0, 1, 2, 3, 4},
				parenthesesMap: map[int]int{},
			},
			want: map[string]int{"H": 2, "O": 2},
		},
		{
			name: "sample3",
			args: args{
				formula:        "Mg(OH)2",
				flagList:       []int{0, 2, 3, 4, 5, 6, 7},
				parenthesesMap: map[int]int{1: 4},
			},
			want: map[string]int{"H": 2, "O": 2, "Mg": 1},
		},
		{
			name: "sample3",
			args: args{
				formula:        "Na5(OH)2(CO3)2",
				flagList:       []int{0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14},
				parenthesesMap: map[int]int{2: 5, 7: 11},
			},
			want: map[string]int{"H": 2, "O": 8, "Na": 5, "C": 2},
		},
		{
			name: "sample3",
			args: args{
				formula:        "Na5(C(OH)2)2",
				flagList:       []int{0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12},
				parenthesesMap: map[int]int{2: 9, 4: 7},
			},
			want: map[string]int{"H": 4, "O": 4, "Na": 5, "C": 2},
		},
		{
			name: "sample3",
			args: args{
				formula:        "Na5(S(C(OH)2)2)2",
				flagList:       []int{0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16},
				parenthesesMap: map[int]int{2: 13, 4: 11, 6: 9},
			},
			want: map[string]int{"H": 8, "O": 8, "Na": 5, "C": 4, "S": 2},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := count(tt.args.formula, tt.args.flagList, tt.args.flagOffset, tt.args.parenthesesMap); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("count() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_countOfAtoms(t *testing.T) {
	type args struct {
		formula string
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		{
			name: "sample",
			args: args{
				formula: "H2O",
			},
			want: "H2O",
		},
		{
			name: "sample2",
			args: args{
				formula: "Mg(H2O)N",
			},
			want: "H2MgNO",
		},
		{
			name: "sample2",
			args: args{
				formula: "Na5(S(C(OH)2)2)2",
			},
			want: "C4H8Na5O8S2",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := countOfAtoms(tt.args.formula); got != tt.want {
				t.Errorf("countOfAtoms() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_maximalNetworkRank(t *testing.T) {
	type args struct {
		n     int
		roads [][]int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "sample1",
			args: args{
				n:     4,
				roads: [][]int{{0, 1}, {0, 3}, {1, 2}, {1, 3}},
			},
			want: 4,
		},
		{
			name: "sample1",
			args: args{
				n:     5,
				roads: [][]int{{0, 1}, {0, 3}, {1, 2}, {1, 3}, {2, 3}, {2, 4}},
			},
			want: 5,
		},
		{
			name: "sample2",
			args: args{
				n:     8,
				roads: [][]int{{0, 1}, {1, 2}, {2, 3}, {2, 4}, {5, 6}, {5, 7}},
			},
			want: 5,
		},
		{
			name: "sample2",
			args: args{
				n:     8,
				roads: [][]int{{0, 1}, {1, 2}, {2, 3}, {2, 4}, {5, 6}, {5, 7}},
			},
			want: 5,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := maximalNetworkRank(tt.args.n, tt.args.roads); got != tt.want {
				t.Errorf("maximalNetworkRank() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_kthSmallest(t *testing.T) {
	type args struct {
		matrix [][]int
		k      int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "sample",
			args: args{matrix: [][]int{{5}}, k: 1},
			want: 5,
		},
		{
			name: "sample1",
			args: args{matrix: [][]int{{1, 5, 9}, {10, 11, 13}, {12, 13, 15}}, k: 8},
			want: 13,
		},
		{
			name: "sample1",
			args: args{matrix: [][]int{{1, 5, 9}, {10, 11, 13}, {12, 13, 15}}, k: 6},
			want: 12,
		},
		{
			name: "sample1",
			args: args{matrix: [][]int{{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, {11, 12, 13, 14, 15}, {16, 17, 18, 19, 20}, {21, 22, 23, 24, 25}}, k: 5},
			want: 5,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := kthSmallest(tt.args.matrix, tt.args.k); got != tt.want {
				t.Errorf("kthSmallest() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_divideArray(t *testing.T) {
	type args struct {
		nums []int
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "sample",
			args: args{[]int{1, 2, 3, 4}},
			want: false,
		},
		{
			name: "sample",
			args: args{[]int{1, 2, 2, 1, 3, 3}},
			want: true,
		},
		{
			name: "badCase",
			args: args{[]int{9, 9, 19, 10, 9, 12, 2, 12, 3, 3, 11, 5, 8, 4, 13, 6, 2, 11, 9, 19, 11, 15, 9, 17, 15, 12, 5, 14, 12, 16, 18, 16, 10, 3, 8, 9, 16, 20, 2, 4, 16, 12, 11, 14, 20, 16, 2, 18, 17, 20, 3, 13, 16, 17, 1, 1, 11, 20, 20, 4}},
			want: false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := divideArray(tt.args.nums); got != tt.want {
				t.Errorf("divideArray() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_decodeAtIndex(t *testing.T) {
	type args struct {
		s string
		k int
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		{
			name: "sample",
			args: args{
				s: "abc",
				k: 1,
			},
			want: "a",
		},
		{
			name: "sample",
			args: args{
				s: "a23",
				k: 6,
			},
			want: "a",
		},
		{
			name: "sample",
			args: args{
				s: "leet2code34",
				k: 30,
			},
			want: "e",
		},
		{
			name: "sample",
			args: args{
				s: "leet2code34",
				k: 37,
			},
			want: "l",
		},
		{
			name: "singleLetter",
			args: args{
				s: "a32543532",
				k: 100,
			},
			want: "a",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := decodeAtIndex(tt.args.s, tt.args.k); got != tt.want {
				t.Errorf("decodeAtIndex() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_isPrefixOfWord(t *testing.T) {
	type args struct {
		sentence   string
		searchWord string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "sample",
			args: args{sentence: "i love you", searchWord: "you"},
			want: 3,
		},
		{
			name: "sample",
			args: args{sentence: "i love you", searchWord: "your"},
			want: -1,
		},
		{
			name: "sample",
			args: args{sentence: "i love you and your family", searchWord: "you"},
			want: 3,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := isPrefixOfWord(tt.args.sentence, tt.args.searchWord); got != tt.want {
				t.Errorf("isPrefixOfWord() = %v, want %v", got, tt.want)
			}
		})
	}
}
