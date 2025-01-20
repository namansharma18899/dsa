package main

import "math"

type Node struct {
	Val  int
	Prev *Node
	Min  int
}

type MinStack struct {
	head *Node
}

func Constructor() MinStack {
	return MinStack{
		head: &Node{
			Min: math.MaxInt32,
		},
	}
}

func (this *MinStack) Push(val int) {
	min := Min(this.head.Min, val)
	this.head = &Node{
		Val:  val,
		Prev: this.head,
		Min:  min,
	}
}

func (this *MinStack) Pop() {
	this.head = this.head.Prev
}

func (this *MinStack) Top() int {
	return this.head.Val
}

func (this *MinStack) GetMin() int {
	return this.head.Min
}

func Min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */
