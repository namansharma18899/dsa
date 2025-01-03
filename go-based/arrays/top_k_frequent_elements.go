package main

import (
	"sort"
)

func topKFrequent(nums []int, k int) []int {
	sort.Ints(nums)
	frequencyMap := make(map[int][]int)
	prev := nums[0]
	counter := 1
	for index := 1; index < len(nums); index++ {
		if nums[index] == prev {
			counter++
		} else {
			frequencyMap[counter] = append(frequencyMap[counter], prev)
			prev = nums[index]
			counter = 1
		}
	}
	// for the last element
	frequencyMap[counter] = append(frequencyMap[counter], prev)
	for index := len(nums) - 1; index > 0; index-- {
		if val, isThere := frequencyMap[index]; isThere {

		}
	}
}
