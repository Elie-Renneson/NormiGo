package filewriter

import (
	"fmt"
	"os"
)

func WriteToStream(file *os.File, buffer []byte, n int) {
	_, err := file.Write(buffer[:n])
	if err != nil {
		fmt.Println("Error writing to stream:", err)
	}
}
