package main

func productExceptSelf(nums []int) []int {
	mul := 1
	two_count := 0
	for _, val := range nums {
		if val != 0 {
			mul *= val
		} else {
			two_count++
		}
	}
	if two_count > 1 {
		arr := make([]int, len(nums))
		return arr
	}
	result := make([]int, 0)
	if two_count == 1 {
		for _, val := range nums {
			if val == 0 {
				result = append(result, mul)
			} else {
				result = append(result, val)
			}
		}
	} else {
		for _, val := range nums {
			V := val
			if val < 0 && mul > 0 {
				V = V * -1
			}
			result = append(result, mul/V)
		}
	}
	return result
}
