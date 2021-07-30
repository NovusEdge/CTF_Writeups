package main

import (
    "fmt"
    "strconv"
)

/*
CreditCard is the credit card's number

The IncompleteNumber element is the format string for incomplete number of the
credit card

If there's missing numbers, we use "*" to denote the respective missing number.
eg: 543210******1234

PS: the thing is a multiple of 123457
*/
type CreditCard struct {
    Number       string
}


func (c* CreditCard) LuhnValidate() bool {
    weights := "2121212121212121"
    digits  := c.Number

	return _luhnChecksum(digits, weights)
}


func (c* CreditCard) FindMissing() []string {
    number := c.Number
    var tempCard CreditCard
    var res []string

    // strings.ReplaceAll(number, "******", "%d")

    for i := 999999; i > 111111; i-- {
        newNum := fmt.Sprintf(number, i)
        // fmt.Println(newNum)
        tempCard.Number = newNum

        if tempCard.LuhnValidate() {
            res = append(res, tempCard.Number)
        }
    }

    return res
}


func _luhnChecksum(number string, weights string) bool {
    var sum int
    // fmt.Println(len(number), len(weights))
    for i := 0; i < len(number); i++ {
        n, _ := strconv.Atoi(string(number[i]))
        w, _ := strconv.Atoi(string(weights[i]))

        tempSum := n*w

        if tempSum >= 10 {
            sum += tempSum % 10 + int(tempSum / 10)
        }
    }
    return sum % 10 == 0
}


func main() {

    c := CreditCard{Number: "543210%d1234"}
    possible := c.FindMissing()

    for _, num := range possible{
        val, _ := strconv.Atoi(num)
        if val % 123457 == 0 {
            fmt.Println(val)
        }
    }
}
