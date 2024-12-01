package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	// Open the input file
	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}
	defer file.Close()

	// Slices to store the integers
	var first []int
	var second []int

	// Scanner to read the file line by line
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		// Read the current line
		line := scanner.Text()

		// Split the line by spaces (handle variable spacing with strings.Fields)
		splits := strings.Fields(line)
		if len(splits) != 2 {
			fmt.Println("Unexpected line format:", line)
			continue
		}

		// Convert the strings to integers
		firstnum, err1 := strconv.Atoi(splits[0])
		secondnum, err2 := strconv.Atoi(splits[1])
		if err1 != nil || err2 != nil {
			fmt.Println("Error converting numbers:", line)
			continue
		}

		// Append to respective slices
		first = append(first, firstnum)
		second = append(second, secondnum)
	}

	// Check for errors during scanning
	if err := scanner.Err(); err != nil {
		fmt.Println("Error scanning file:", err)
		return
	}
	// PART 1
	// Print the results
	// sort.Slice(first, func(i, j int) bool {
	// 	return first[i] < first[j]
	// })
	// sort.Slice(second, func(i, j int) bool {
	// 	return second[i] < second[j]
	// })
	n := len(first)
	res := 0
	// for i := 0; i < n; i++ {
	// 	res = res + int(math.Abs(float64(first[i] - second[i])))
	// }
	// fmt.Println(res)
	count := map[int]int{}
	for i := 0; i < n; i++ {
		count[second[i]]++
	}
	for i := 0; i < n; i++ {
		res += count[first[i]] * first[i]

	}
	fmt.Println(res)
}
