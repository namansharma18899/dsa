package main

func productExceptSelf(nums []int) []int {
	mod := 1<<31 - 1 // Max value of 32-bit signed integer (2^31 - 1)
	result := make([]int, 0)
	// left prod, right prod
	leftProd := make([]int, len(nums))
	rightProd := make([]int, len(nums))
	prod := 1
	for index := 0; index < len(nums); index++ {
		leftProd[index] = prod
		prod *= nums[index]
	}
	prod = 1
	for index := len(nums) - 1; index >= 0; index-- {
		rightProd[index] = prod
		prod *= nums[index]
	}
	for index := 0; index < len(nums); index++ {
		res := (leftProd[index] * rightProd[index]) % mod
		result = append(result, res)
	}
	return result

}
