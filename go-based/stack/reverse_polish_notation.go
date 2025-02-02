package main

import "strconv"

// Define Value as an interface that Node can also implement
type Value interface{}

// Expression placeholder type
type Expression struct {
	// Define expression-related fields if needed
	op string
}

// Define Node where val1 and val2 can be either a Value or another Node
type CustomNode struct {
	val1       Value
	val2       Value
	expression Expression
}

// Function to check if a string is an integer
func calculate(a, b int, op string) int32 {
	switch op {
	case "+":
		return int32(a + b)
	case "*":
		return int32(a * b)
	case "/":
		if b != 0 {
			return int32(b / a)
		}
		return 0 // Handle division by zero safely
	default:
		return 0 // Default case for unsupported operators
	}
}

func evalRPN(tokens []string) int {
	stack := make([]int, 0)
	result := 0
	for index, val := range tokens {
		intVal, err := strconv.Atoi(val)
		if err != nil {
			stack = append(stack, intVal)
		} else {
			l1, l2 := stack[len(stack)-1], stack[len(stack)-2]
			stack = stack[:len(stack)-2]
			valRes := int(calculate(l1, l2, val))
			stack = append(stack, valRes)
			if index == len(tokens)-1 {
				return valRes
			}
		}
	}
	return result
}
