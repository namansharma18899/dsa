package main

import (
	"sort"
)

func topKFrequent(nums []int, k int) []int {
	sort.Ints(nums)
	frequencyMap := make(map[int][]int)
	prev := nums[0]
	counter := 1
	result := make([]int, 0)

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
	for index := len(nums); index >= 0; index-- {
		if k <= 0 {
			break
		}
		if val, isThere := frequencyMap[index]; isThere {
			for j := 0; j < len(val); j++ {
				if k <= 0 {
					break
				}
				result = append(result, val[j])
				k--
			}
		}
	}
	return result
}
