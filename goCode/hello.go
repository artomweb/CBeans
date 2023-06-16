package main

import "fmt"
import "time"
import "sort"



func partition(number float64, memo map[float64][]float64) []float64 {
	if _, ok := memo[number]; ok {
		return memo[number]
	}

	answer := make([]float64, 0)
	answer = append(answer, number)

	for x := 1; x < int(number*2); x++ {
		remainingNumber := number - float64(x)/2

		if remainingNumber < float64(x)/2 {
			break
		}

		for _, y := range partition(remainingNumber, memo) {
			temp := []float64{float64(x) / 2}
			temp = append(temp, y...)
			answer = append(answer, temp...)
		}
	}

	memo[number] = answer
	return answer
}

func main() {
    start := time.Now()

    n := 2
	fmt.Printf("Partitions of %d\n", n)

	number := 2.0
	memo := make(map[float64]map[float64]bool)
	result := partition(number, memo)

	fmt.Println("Answer: ", result)

    elapsed := time.Since(start)
    fmt.Printf("Took %s\n", elapsed)
}