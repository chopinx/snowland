package base

import (
	"math/rand"
	"reflect"
	"sort"
	"testing"
)

func TestNewSkipList(t *testing.T) {
	type args struct {
		dataList []int
	}
	dataList1 := make([]int, 10000)
	for i := range dataList1 {
		dataList1[i] = rand.Int() % 10000
	}
	orderedList := make([]int, 10000)
	copy(orderedList, dataList1)
	sort.Ints(orderedList)
	tests := []struct {
		name string
		args args
		want []int
	}{
		{
			name: "simple",
			args: args{
				dataList: []int{3, 4, 2, 5, 1},
			},
			want: []int{1, 2, 3, 4, 5},
		},
		{
			name: "dataList1",
			args: args{
				dataList: dataList1,
			},
			want: orderedList,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := NewSkipList(tt.args.dataList...).GetDataList(); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("NewSkipList() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestSkipList_Find(t *testing.T) {
	type args struct {
		data int
	}
	tests := []struct {
		name     string
		dataList []int
		args     args
		want     bool
	}{
		{
			name:     "sample",
			dataList: []int{4, 3, 5, 2, 1},
			args:     args{3},
			want:     true,
		},
		{
			name:     "sample",
			dataList: []int{4, 3, 5, 2, 1},
			args:     args{8},
			want:     false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			s := NewSkipList(tt.dataList...)
			if got := s.Find(tt.args.data); got != tt.want {
				t.Errorf("Find() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestSkipList_Insert(t *testing.T) {
	type fields struct {
		head  []*DataNode
		level int
		size  int
	}
	type args struct {
		data int
	}
	tests := []struct {
		name   string
		fields fields
		args   args
		want   []int
	}{
		{
			name: "sample",
			fields: fields{
				head: []*DataNode{
					{Value: 0, Node: Node{
						Right: &DataNode{Value: 2, Node: Node{
							Right: nil,
						}}}}},
				level: 1,
				size:  2,
			},
			args: args{
				data: 1,
			},
			want: []int{0, 1, 2},
		},
		{
			name: "front insert",
			fields: fields{
				head: []*DataNode{
					{Value: 1, Node: Node{
						Right: &DataNode{Value: 2, Node: Node{
							Right: nil,
						}}}}},
				level: 1,
				size:  2,
			},
			args: args{
				data: 0,
			},
			want: []int{0, 1, 2},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			s := &SkipList{
				head:  tt.fields.head,
				level: tt.fields.level,
				size:  tt.fields.size,
			}
			s.Insert(tt.args.data)
			if got := s.GetDataList(); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("GetDataList() = %v, want %v", got, tt.want)
			}

		})
	}
}

func TestSkipList_Remove(t *testing.T) {
	type args struct {
		data int
	}
	tests := []struct {
		name         string
		dataList     []int
		args         args
		wantErr      bool
		wantDataList []int
	}{
		{
			name:     "sample",
			dataList: []int{4, 3, 5, 2, 1},
			args: args{
				data: 2,
			},
			wantErr:      false,
			wantDataList: []int{1, 3, 4, 5},
		},
		{
			name:     "sample",
			dataList: []int{4, 3, 5, 2, 1},
			args: args{
				data: 6,
			},
			wantErr:      true,
			wantDataList: []int{1, 2, 3, 4, 5},
		},
		{
			name:     "sample",
			dataList: []int{4},
			args: args{
				data: 4,
			},
			wantErr:      false,
			wantDataList: []int{},
		},
		{
			name:     "sample",
			dataList: []int{},
			args: args{
				data: 4,
			},
			wantErr:      true,
			wantDataList: []int{},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			s := NewSkipList(tt.dataList...)
			err := s.Remove(tt.args.data)
			if (err != nil) != tt.wantErr {
				t.Errorf("Remove() error = %v, wantErr %v", err, tt.wantErr)
			}
			if !reflect.DeepEqual(s.GetDataList(), tt.wantDataList) {
				t.Errorf("Remove() dataList = %v, wantDataList %v", s.GetDataList(), tt.wantDataList)
			}
		})
	}
}

func TestSkipList_Operating(t *testing.T) {
	myMap := make(map[int]interface{})
	mySkipList := NewSkipList()
	for i := 0; i < 10000; i++ {
		data := rand.Int() % 10000
		myMap[data] = nil
		ok := mySkipList.Find(data)
		if !ok {
			mySkipList.Insert(data)
			if !mySkipList.Check() {
				t.Errorf("skipList.Check() = %v, want %v", mySkipList.Check(), true)
			}
		}
		if mySkipList.Size() != len(myMap) {
			t.Errorf("skipList.Size() = %d, want %d", mySkipList.Size(), len(myMap))
			return
		}
		dataList2 := make([]int, 0)
		for k := range myMap {
			dataList2 = append(dataList2, k)
		}
		sort.Ints(dataList2)
		if !reflect.DeepEqual(mySkipList.GetDataList(), dataList2) {
			t.Errorf("mySkipList.GetDataList() = %v, \nwant %v, data = %d", mySkipList.GetDataList(), dataList2, data)
			return
		}
		data = rand.Int() % 1000
		if _, ok := myMap[data]; ok != mySkipList.Find(data) {
			t.Errorf("mySkipList.Find(%d) = %v, want %v", data, mySkipList.Find(data), ok)
			return
		}
		delete(myMap, data)
		err := mySkipList.Remove(data)
		if !mySkipList.Check() {
			if !mySkipList.Check() {
				t.Errorf("skipList.Check() = %v, want %v, size = %d, data = %d, err = %v", mySkipList.Check(), true, mySkipList.Size(), data, err)
			}
		}
		if mySkipList.Size() != len(myMap) {
			t.Errorf("skipList.Size() = %d, want %d", mySkipList.Size(), len(myMap))
			return
		}
		dataList2 = make([]int, 0)
		for k := range myMap {
			dataList2 = append(dataList2, k)
		}
		sort.Ints(dataList2)
		if !reflect.DeepEqual(mySkipList.GetDataList(), dataList2) {
			t.Errorf("mySkipList.GetDataList() = %v, \nwant %v, data = %d", mySkipList.GetDataList(), dataList2, data)
			return
		}
	}
}

func TestSkipList_TimeCost(t *testing.T) {
	mySkipList := NewSkipList()
	for i := 0; i < 1000000; i++ {
		data := rand.Int() % 100000
		if !mySkipList.Find(data) {
			mySkipList.Insert(data)
		}
		data = rand.Int() % 100000
		_ = mySkipList.Remove(data)
	}
}

func TestMap_TimeCost(t *testing.T) {
	mySkipList := make(map[int]interface{})
	for i := 0; i < 1000000; i++ {
		data := rand.Int() % 100000
		mySkipList[data] = nil
		data = rand.Int() % 100000
		delete(mySkipList, data)
	}
}
