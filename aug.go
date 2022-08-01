package snowland

import (
	"sort"
)

type xCoord int
type yCoord int

type xCoords []xCoord

func (xs xCoords) Less(i, j int) bool {
	return xs[i] < xs[j]
}
func (xs xCoords) Len() int {
	return len(xs)
}

func (xs xCoords) Swap(i, j int) {
	tmp := xs[j]
	xs[j] = xs[i]
	xs[i] = tmp
}

type yCoords []yCoord

func (xs yCoords) Less(i, j int) bool {
	return xs[i] < xs[j]
}
func (xs yCoords) Len() int {
	return len(xs)
}

func (xs yCoords) Swap(i, j int) {
	tmp := xs[j]
	xs[j] = xs[i]
	xs[i] = tmp
}

type PointsPool struct {
	points   [][]int
	pointSet map[xCoord]map[yCoord]bool
	XAxisMap map[yCoord]xCoords
	YAxisMap map[xCoord]yCoords
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
		XAxisMap: map[yCoord]xCoords{},
		YAxisMap: map[xCoord]yCoords{},
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
func (p *PointsPool) GetXAxisPoints(y yCoord) []xCoord {
	if _, ok := p.XAxisMap[y]; !ok {
		return []xCoord{}
	}
	return p.XAxisMap[y]
}

// GetYAxisPoints func find all points which have the given x coordinate, and return their y coordinates
func (p *PointsPool) GetYAxisPoints(x xCoord) []yCoord {
	if _, ok := p.YAxisMap[x]; !ok {
		return []yCoord{}
	}
	return p.YAxisMap[x]
}
