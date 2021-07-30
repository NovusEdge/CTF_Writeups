package main

import (
    "fmt"
    "strings"
)

func main() {

    stuff := `123123%d%d1293`
    splitted := strings.Split(stuff, "%d")
    fmt.Println(splitted)
}
