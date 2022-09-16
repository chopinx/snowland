package snowland

import (
	"math/rand"
	"reflect"
	"testing"
)

func Test_minTimeToVisitAllPoints(t *testing.T) {
	type args struct {
		points [][]int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "sample",
			args: args{
				points: [][]int{{1, 1}, {3, 4}, {-1, 0}},
			},
			want: 7,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := minTimeToVisitAllPoints(tt.args.points); got != tt.want {
				t.Errorf("minTimeToVisitAllPoints() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_countTriples(t *testing.T) {
	type args struct {
		n int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{name: "sample", args: args{5}, want: 2},
		{name: "sample", args: args{10}, want: 4},
		{name: "sample", args: args{25}, want: 16},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := countTriples(tt.args.n); got != tt.want {
				t.Errorf("countTriples() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_minimumRemoval(t *testing.T) {
	type args struct {
		beans []int
	}
	tests := []struct {
		name string
		args args
		want int64
	}{
		{
			name: "sample",
			args: args{
				beans: []int{4, 1, 5, 6},
			},
			want: 4,
		},
		{
			name: "sample",
			args: args{
				beans: []int{2, 10, 3, 2},
			},
			want: 7,
		},
		{
			name: "sample",
			args: args{
				beans: []int{60, 60},
			},
			want: 0,
		},
		{
			name: "sample",
			args: args{
				beans: []int{43, 44, 45, 46, 47},
			},
			want: 10,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := minimumRemoval(tt.args.beans); got != tt.want {
				t.Errorf("minimumRemoval() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_minGreaterArr(t *testing.T) {
	type args struct {
		arr []int32
	}
	arr := make([]int32, 10000000)
	for i := 0; i < len(arr); i++ {
		arr[i] = rand.Int31()
	}
	tests := []struct {
		name string
		args args
		want []int32
	}{
		{
			name: "sample",
			args: args{
				arr: []int32{5, 4, 6, 3, 2, 1, 9, 8},
			},
			want: []int32{6, 8, 9},
		},
		{
			name: "sample",
			args: args{
				arr: arr,
			},
			want: []int32{5, 6},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := minGreaterArr(tt.args.arr); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("minGreaterArr() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_numTrees(t *testing.T) {
	type args struct {
		n int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "sample",
			args: args{3},
			want: 5,
		},
		{
			name: "sample",
			args: args{1},
			want: 1,
		},
		{
			name: "sample",
			args: args{4},
			want: 14,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := numTrees(tt.args.n); got != tt.want {
				t.Errorf("numTrees() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_findMinArrowShots(t *testing.T) {
	type args struct {
		points [][]int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "sample",
			args: args{[][]int{{0, 1}}},
			want: 1,
		},
		{
			name: "sample",
			args: args{[][]int{{0, 1}, {2, 3}}},
			want: 2,
		},
		{
			name: "sample",
			args: args{[][]int{{0, 1}, {1, 2}}},
			want: 1,
		},
		{
			name: "sample",
			args: args{[][]int{{0, 1}, {0, 2}, {1, 2}, {2, 3}, {2, 4}, {3, 4}}},
			want: 2,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := findMinArrowShots(tt.args.points); got != tt.want {
				t.Errorf("findMinArrowShots() = %v, want %v", got, tt.want)
			}
		})
	}
}
