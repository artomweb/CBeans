package main

import (
	"fmt";
	"time";
	"sort"
)

func partition(number float64) [][]float64 {
	memo := make(map[float64][][]float64)

	var partitionHelper func(float64) [][]float64
	partitionHelper = func(num float64) [][]float64 {
		if partitions, ok := memo[num]; ok {
			return partitions
		}

		answer := [][]float64{{num}}

		partitionSet := make(map[string]bool) // Track unique partitions

		for x := 0.5; x <= num/2; x += 0.5 {
			remainingNumber := num - x

			for _, y := range partitionHelper(remainingNumber) {
				partition := make([]float64, len(y)+1)
				partition[0] = x
				copy(partition[1:], y)
				sort.Float64s(partition) // Sort the partition before checking uniqueness

				partitionKey := fmt.Sprintf("%v", partition)
				if !partitionSet[partitionKey] {
					partitionSet[partitionKey] = true
					answer = append(answer, partition)
				}
			}
		}

		memo[num] = answer
		return answer
	}

	return partitionHelper(number)
}

func main() {
	n := 15
	start := time.Now()
	partitions := partition(float64(n))
	elapsed := time.Since(start)
	fmt.Println(partitions)
	_ = partitions

    fmt.Printf("Took %s\n", elapsed)
}
