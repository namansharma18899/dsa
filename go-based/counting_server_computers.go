package main

func countServers(grid [][]int) int {
	rows, cols := len(grid), len(grid[0])
	dynamicArray := make([][]int, rows) // Create a slice for rows
	for i := 0; i < rows; i++ {
		dynamicArray[i] = make([]int, cols) // Create a slice for each column
	}
	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			dynamicArray[i][j] = i + j
		}
	}
	return 0
}
