package snowland

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
