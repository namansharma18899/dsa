package main

func getHash(s string) float32 {
	sum := float32(0)
	for _, char := range s {
		sum += float32(char) // Convert the character to its ASCII value and add to sum
	}
	sum = float32(sum) / float32((10 * len(s)))
	sum += float32(len(s))
	return float32(sum)
}

func groupAnagrams(strs []string) [][]string {
	mapOfAna := make(map[float32][]string)
	for _, each := range strs {
		hashVal := getHash(each)
		mapOfAna[hashVal] = append(mapOfAna[hashVal], each)
		// if _, present := mapOfAna[hashVal]; present {
		// } else {
		// 	app
		// }
	}
	var result [][]string
	for _, val := range mapOfAna {
		result = append(result, val)
	}
	return result
}

func main() {
	testcases := [6]string{"eat", "tea", "tan", "ate", "nat", "bat"}
	groupAnagrams(testcases[:])
}
