package main

import "fmt"

type testcase struct {
	numbers  []int
	target   int
	expected []int
}

func main() {
	testcases := []testcase{
		testcase{
			numbers:  []int{2, 7, 11, 15},
			target:   9,
			expected: []int{1, 2},
		},
	}
	for _, tcase := range testcases {
		fmt.Println(twoSum(tcase.numbers, tcase.target))
	}
}
