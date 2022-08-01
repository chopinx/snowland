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
				XAxisMap: map[yCoord]xCoords{0: {0, 1}, 1: {0, 1}},
				YAxisMap: map[xCoord]yCoords{0: {0, 1}, 1: {0, 1}},
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
		xAxisMap map[yCoord]xCoords
		yAxisMap map[xCoord]yCoords
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
		xAxisMap: map[yCoord]xCoords{0: {0, 1}, 1: {0, 1}},
		yAxisMap: map[xCoord]yCoords{0: {0, 1}, 1: {0, 1}},
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
		xAxisMap map[yCoord]xCoords
		yAxisMap map[xCoord]yCoords
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
		xAxisMap: map[yCoord]xCoords{0: {0, 1}, 1: {0, 1}},
		yAxisMap: map[xCoord]yCoords{0: {0, 1}, 1: {0, 1}},
	}
	tests := []struct {
		name   string
		fields fields
		args   args
		want   xCoords
	}{
		{
			name:   "case1",
			fields: baseFields,
			args: args{
				y: 0,
			},
			want: xCoords{0, 1},
		},
		{
			name:   "case2",
			fields: baseFields,
			args: args{
				y: 1,
			},
			want: xCoords{0, 1},
		},
		{
			name:   "case3",
			fields: baseFields,
			args: args{
				y: 2,
			},
			want: xCoords{},
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
		xAxisMap map[yCoord]xCoords
		yAxisMap map[xCoord]yCoords
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
		xAxisMap: map[yCoord]xCoords{0: {0, 1}, 1: {1, 0}},
		yAxisMap: map[xCoord]yCoords{0: {0, 1}, 1: {1, 0}},
	}
	tests := []struct {
		name   string
		fields fields
		args   args
		want   yCoords
	}{
		{
			name:   "case1",
			fields: baseFields,
			args: args{
				x: 0,
			},
			want: yCoords{0, 1},
		},
		{
			name:   "case2",
			fields: baseFields,
			args: args{
				x: 1,
			},
			want: yCoords{1, 0},
		},
		{
			name:   "case3",
			fields: baseFields,
			args: args{
				x: 2,
			},
			want: yCoords{},
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
