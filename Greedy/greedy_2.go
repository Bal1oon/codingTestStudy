package main

import "fmt"

func main() {
	var n, m int
	fmt.Scan(&n, &m)

	cards := make([][]int, n)
	for i := 0; i < n; i++ {
		cards[i] = make([]int, m)
		for j := 0; j < m; j++ {
			fmt.Scan(&cards[i][j])
		}
	}

	s := solution(n, m, cards)
	fmt.Println(s)
}

func solution(n int, m int, cards [][]int) int {
	maxVal := 0
	for i := 0; i < n; i++ {
		minVal := cards[i][0]
		for j := 0; j < n; j++ {
			if minVal > cards[i][j] {
				minVal = cards[i][j]
			}
		}
		if maxVal < minVal {
			maxVal = minVal
		}
	}
	return maxVal
}
