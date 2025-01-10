package main

import (
	"reflect"
	"testing"
)

// Function to test
func twoSum(numbers []int, target int) []int {
	result := make([]int, 2)
	left, right := 0, len(numbers)-1
	for left < right {
		total := numbers[left] + numbers[right]
		if total == target {
			result[0] = left + 1
			result[1] = right + 1
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

func TestSumEqualsTarget(t *testing.T) {
	// Define test cases
	testCases := []struct {
		name     string
		numbers  []int
		target   int
		expected []int
	}{
		{
			name:     "Empty slice",
			numbers:  []int{2, 7, 11, 15},
			target:   9,
			expected: []int{1, 2},
		},
		{
			name:     "-ve ",
			numbers:  []int{-1, 0},
			target:   -1,
			expected: []int{1, 2},
		},
	}

	// Iterate through test cases
	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			result := twoSum(tc.numbers, tc.target)
			if isEqual := reflect.DeepEqual(result, tc.expected); !isEqual {
				t.Errorf("For numbers %v and target %d, expected %v but got %v", tc.numbers, tc.target, tc.expected, result)
			}
		})
	}
}
