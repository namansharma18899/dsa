package main

import "fmt"

func main() {
	// testcases := [6]string{"eat",[[0,2],[1,4],[1,1]] "tea",[[0,2],[1,4],[1,1]] "tan", "ate", "nat", "bat"}
	// GA()
	// matrix := [][]int{
	// 	{0, 2},
	// 	{1, 4},
	// 	{1, 1},
	// }
	// vowelStrings([]string{"aba", "bcb", "ece", "aa", "e"}, matrix)
	nums := []int{4, 0, -4, -2, 2, 5, 2, 0, -8, -8, -8, -8, -1, 7, 4, 5, 5, -4, 6, 6, -3}
	fmt.Println(longestConsecutive(nums))
}
