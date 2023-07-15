package main

import "fmt"

func false() {
    var studentVar_1 string
    studentVar_1 := "John"  // Incorrect assignment format
    var studentVar2 string = "Mary"
    fmt.Printf("Hello, %s!\n", studentVar2)  // Correct printf usage
    println(studentVar2)  // Incorrect usage of println
}
