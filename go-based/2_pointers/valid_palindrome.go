package main

import (
	"unicode"
)

func isPalindrome(s string) bool {
	rightP := len(s) - 1
	leftP := 0
	for leftP < rightP {
		// Loop until we reach a valid character to compare
		for leftP < rightP && !(unicode.IsLetter(rune(s[leftP]))) || !(unicode.IsDigit(rune(s[leftP]))) {
			leftP++
		}
		for leftP < rightP && !(unicode.IsLetter(rune(s[rightP]))) || !(unicode.IsDigit(rune(s[rightP]))) {
			rightP--
		}
		if unicode.ToLower(rune(s[leftP])) != unicode.ToLower(rune(s[rightP])) {
			return false
		}
		leftP++
		rightP--
	}
	return true
}
