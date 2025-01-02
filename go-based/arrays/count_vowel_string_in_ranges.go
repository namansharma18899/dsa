package main

func isVowel(c byte) bool {
	return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
}

func vowelStrings(words []string, queries [][]int) []int {
	n := len(words)
	prefix := make([]int, n)

	for idx, word := range words {
		prefix[idx] = 0
		if idx > 0 {
			prefix[idx] = prefix[idx-1]
		}
		// Here we are finding Prefix Sum...while finding vowels
		if isVowel(word[0]) && isVowel(word[len(word)-1]) {
			prefix[idx]++
		}
	}
	sols := make([]int, len(queries))
	for idx, query := range queries {
		l := query[0]
		r := query[1]
		if l == 0 {
			sols[idx] = prefix[r]
			continue
		}
		// Core logix
		sols[idx] = prefix[r] - prefix[l-1]
	}
	return sols
}
