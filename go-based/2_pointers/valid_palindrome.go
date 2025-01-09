package main

func isPalindrome(s string) bool {
	pointer2 := len(s) - 1
	for index := 0; index < len(s)-1; index++ {
		if index >= pointer2 {
			break
		}
		if s[index] != s[pointer2] {
			return false
		}
		pointer2--
	}
	return true
}
