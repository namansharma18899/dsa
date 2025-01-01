package main

import (
	"fmt"
	"sort"
	"strings"
	"unicode"
)

// TODO: MAJOR ISSUE --> CHAR VALUES OVERLAP, thus causing duplication for ex:  13.7:[duh ill]
var letters = map[string]int{
	"A": 503,
	"B": 509,
	"C": 521,
	"D": 523,
	"E": 541,
	"F": 547,
	"G": 557,
	"H": 563,
	"I": 569,
	"J": 571,
	"K": 577,
	"L": 587,
	"M": 593,
	"N": 599,
	"O": 601,
	"P": 607,
	"Q": 613,
	"R": 617,
	"S": 619,
	"T": 631,
	"U": 641,
	"V": 643,
	"W": 647,
	"X": 653,
	"Y": 659,
	"Z": 661,
}

func getHash(s string) float32 {
	sum := float32(0)
	for _, char := range s {
		char = unicode.ToUpper(char)
		sum += float32(letters[string(char)])
	}
	sum = float32(sum) / float32((10 * len(s)))
	sum += float32(len(s))
	return float32(sum)
}

// func groupAnagrams(strs []string) [][]string {
// 	mapOfAna := make(map[float32][]string)
// 	for _, each := range strs {
// 		hashVal := getHash(each)
// 		mapOfAna[hashVal] = append(mapOfAna[hashVal], each)
// 		// if _, present := mapOfAna[hashVal]; present {
// 		// } else {
// 		// 	app
// 		// }
// 	}
// 	var result [][]string
// 	for _, val := range mapOfAna {
// 		result = append(result, val)
// 	}
// 	return result
// }

func GroupAnagrams(strs []string) [][]string {
	// Map to store anagram groups
	anagramMap := make(map[string][]string)

	// Process each string
	for _, s := range strs {
		// Convert string to sorted form to use as key
		key := sortString(s)

		// Add string to its anagram group
		anagramMap[key] = append(anagramMap[key], s)
	}

	// Convert map values to result slice
	result := make([][]string, 0, len(anagramMap))
	for _, group := range anagramMap {
		result = append(result, group)
	}

	return result
}

// Helper function to sort characters in a string
func sortString(s string) string {
	// Convert string to rune slice for sorting
	chars := strings.Split(s, "")
	sort.Strings(chars)
	return strings.Join(chars, "")
}

// Alternative approach using character count
func groupAnagrams(strs []string) [][]string {
	// Map to store anagram groups using character count as key
	anagramMap := make(map[[26]int][]string)

	// Process each string
	for _, s := range strs {
		// Create character count array
		count := [26]int{}
		for _, c := range s {
			count[c-'a']++
		}

		// Add string to its anagram group
		anagramMap[count] = append(anagramMap[count], s)
	}

	// Convert map values to result slice
	result := make([][]string, 0, len(anagramMap))
	for _, group := range anagramMap {
		result = append(result, group)
	}

	return result
}

func GA() {
	testcases := [6]string{"eat", "tea", "tan", "ate", "nat", "bat"}
	fmt.Println(groupAnagrams(testcases[:]))
}
