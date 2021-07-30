package main

import (
    "strings"
)

/*
CreditNum is the credit card's number

The IncompleteNumber element is the format string for incomplete number of the
credit card
*/
type CreditNum struct {
    Number       string
    IsIncomplete bool
    MissingCount int
}


func MakeCreditNum(number string, isIncomplete bool) (cn CreditNum){
    if isIncomplete || strings.Contains(number, "%d") {
        return CreditNum{ Number: number, IsIncomplete: true}
    } else {
        return CreditNum{ Number: number, IsIncomplete: false }
    }

    return CreditNum{ Number: number, IsIncomplete: false }
}

func (cn* CreditNum) LuhnValidate() bool {
    weights := strings.Split("2121212121212121", "")
    digits  := strings.Split(cn.Number, "%d")

}

func (cn* CreditNum) CheckNumber() bool {
    return false
}

func (cn* CreditNum) FindMissing() []string {
    return []string{"hehe"}
}

func main() {}
