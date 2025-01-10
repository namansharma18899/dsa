package main

import "fmt"

func main() {
	input := []string{
		// "A man, a plan, a canal: Panama",
		// "naman",
		// "N     a     m  a         N",
		"1001",
		// "0P",
	}
	for _, eachSString := range input {
		fmt.Println(isPalindrome(eachSString))
	}
}
