package main

import (
	"fmt"
	"strings"
)

func isWordVowel(word string) bool {
	vowels := "aeiouAEIOU"
	if strings.ContainsRune(vowels, rune(word[0])) {
		return strings.ContainsRune(vowels, rune(word[len(word)-1]))
	} else {
		return false
	}
}
func vowelStrings(words []string, queries [][]int) []int {
	var result []int
	var prefixSum []int
	var isVowelArr []int
	// vowelBoolArr := make([]int, 0)
	for _, eachWord := range words {
		// prefix[i+1] = prefix[i] + words[i]
		if isWordVowel(eachWord) {
			isVowelArr = append(isVowelArr, 1)
		} else {
			isVowelArr = append(isVowelArr, 0)
		}
	}
	prefixSum = append(prefixSum, isVowelArr[0])
	for i := 1; i < len(isVowelArr); i++ {
		prefixSum = append(prefixSum, (prefixSum[i-1] + isVowelArr[i]))
	}
	fmt.Println(isVowelArr)
	for i := range queries {
		result = append(result, prefixSum[queries[i][1]]-prefixSum[queries[i][0]]+isVowelArr[queries[i][0]])
	}
	return result
}
