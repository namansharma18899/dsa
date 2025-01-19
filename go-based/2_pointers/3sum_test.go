package main

import (
	"reflect"
	"sort"
	"testing"
)

func findtwoSum(numbers []int, target int, p1, p2 int) []int {
	result := make([]int, 2)
	left, right := 0, len(numbers)-1
	for left < right {
		total := numbers[left] + numbers[right]
		if total == target {
			result[0] = left
			result[1] = right
			return result
		}
		if total > target {
			right--
		} else {
			left++
		}
	}
	return nil
}

// Function to test
func threeSum(numbers []int) [][]int {
	// sort the array
	RESULT := make([][]int, 0)
	sort.Ints(numbers)
	index := 0
	for {
		if index > len(numbers)-3 {
			break
		}
		if index > 0 && numbers[index-1] == numbers[index] {
			index++
			continue
		} else {
			result := []int{numbers[index], 0, 0}
			p1, p2 := index+1, len(numbers)-1
			res := findtwoSum(numbers, numbers[index], p1, p2)
			result[0] = res[0]
			result[1] = res[1]
			RESULT = append(RESULT, result)
		}
	}
	return RESULT
}

func TestThreeSum(t *testing.T) {
	// Define test cases
	testCases := []struct {
		name     string
		numbers  []int
		expected [][]int
	}{
		{
			name:    "Empty slice",
			numbers: []int{2, 7, 11, 15},
			expected: [][]int{
				{-1, -1, 2},
				{-1, 0, 1},
			}},
		{
			name:    "-ve ",
			numbers: []int{-1, 0},
			expected: [][]int{
				{-1, -1, 2},
				{-1, 0, 1},
			}},
	}

	// Iterate through test cases
	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := threeSum(tc.numbers)
			if isEqual := reflect.DeepEqual(result, tc.expected); !isEqual {
				t.Errorf("For numbers %v and target %d, expected %v but got %v", tc.numbers, tc.expected, result)
			}
		})
	}
}
