package main

import "fmt"

func longestConsecutive(nums []int) int {
	// Logic, if a number before me exists, then the subsequence is valid
	if len(nums) <= 1 {
		return len(nums)
	}
	maxVal := nums[0]
	minVal := nums[0]
	mapOFElements := make(map[int]int)
	for index := 0; index < len(nums); index++ {
		mapOFElements[nums[index]] = 1
		if nums[index] > maxVal {
			maxVal = nums[index]
		}
		if nums[index] < minVal {
			minVal = nums[index]
		}
	}
	result := 0
	for index := minVal; index < maxVal+1; index++ {
		if mapOFElements[index] > 0 {
			if mapOFElements[index-1] > 0 {
				mapOFElements[index] += mapOFElements[index-1]
			}
		}
		if mapOFElements[index] > result {
			result = mapOFElements[index]
		}
	}
	fmt.Println("map -> ", mapOFElements)

	return result
}
