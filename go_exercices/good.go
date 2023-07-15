package main

import (
	"fmt"
	"os"
	"example.com/go_exercices/filewriter"
)

func good() {
	var student1 string
	student1 = "John" // Correct assignment format
	var student2 string
	student2 = "Mary"

	var arr1 [5]int
	arr1 = [5]int{4,5,6,7,8}

	fmt.Printf("Hello, %s!\n", student1) // Correct printf usage
	filewriter.WriteToStream(os.Stdout, []byte(student2), len(student2))

	fmt.Println(arr1)

}

func main() {
	good()
}