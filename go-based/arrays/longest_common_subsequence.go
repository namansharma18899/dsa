package main

import "fmt"

func longestConsecutive(nums []int) int {
	if len(nums) == 1 {
		return 1
	}
	maxVal := nums[0]
	mapOFElements := make(map[int]int)
	for index := 0; index < len(nums); index++ {
		mapOFElements[nums[index]] = 1
		if nums[index] > maxVal {
			maxVal = nums[index]
		}
	}
	result := 0
	fmt.Println("mapxxx -> ", mapOFElements)
	for index := 0; index < maxVal+1; index++ {
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
