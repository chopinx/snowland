package snowland

import "testing"

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
