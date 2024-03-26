package main

import (
	"fmt"
	"sort"
)

func solution(n int, m int, k int, nums []int) int {
	var result int = 0
	sort.Slice(nums, func(i, j int) bool {
		return nums[i] > nums[j]
	})

	result += nums[0] * int(m/k) * k
	result += nums[1] * (m % k)

	return result
}

func main() {
	var n, m, k int
	fmt.Scan(&n, &m, &k)

	nums := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&nums[i])
	}

	var s int = solution(n, m, k, nums)
	fmt.Println(s)
}
