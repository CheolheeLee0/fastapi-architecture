package main

import (
	"fmt"
	"time"
)

func main() {
	// Number of arithmetic operations to perform
	numOperations := 100_000_000

	// Addition
	startTime := time.Now()
	result := 0
	for i := 0; i < numOperations; i++ {
		result += 1
	}
	endTime := time.Now()
	fmt.Printf("Time taken for 100 million additions: %.4f seconds\n", endTime.Sub(startTime).Seconds())

	// Subtraction
	startTime = time.Now()
	result = numOperations
	for i := 0; i < numOperations; i++ {
		result -= 1
	}
	endTime = time.Now()
	fmt.Printf("Time taken for 100 million subtractions: %.4f seconds\n", endTime.Sub(startTime).Seconds())

	// Multiplication
	startTime = time.Now()
	result = 1
	for i := 0; i < numOperations; i++ {
		result *= 1
	}
	endTime = time.Now()
	fmt.Printf("Time taken for 100 million multiplications: %.4f seconds\n", endTime.Sub(startTime).Seconds())

	// Division
	startTime = time.Now()
	result = numOperations
	for i := 0; i < numOperations; i++ {
		result /= 1
	}
	endTime = time.Now()
	fmt.Printf("Time taken for 100 million divisions: %.4f seconds\n", endTime.Sub(startTime).Seconds())
}


// Time taken for 100 million additions: 0.0405 seconds
// Time taken for 100 million subtractions: 0.0343 seconds
// Time taken for 100 million multiplications: 0.0305 seconds
// Time taken for 100 million divisions: 0.0294 seconds