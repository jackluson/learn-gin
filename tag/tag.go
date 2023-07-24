package main

import (
	"encoding/json"
	"fmt"
	"reflect"
)

type Person struct {
	Name string `json:"name"`
	Age  int    `json:"age"`
	Addr string `json:"addr,omitempty"`
}

func main() {
	p1 := Person{
		Name: "Jack",
		Age:  22,
		Addr: "",
	}
	field := reflect.TypeOf(p1)
	name, _ := field.FieldByName("Name")
	fmt.Println(name.Tag.Get("json"))
	data1, err := json.Marshal(p1)
	if err != nil {
		panic(err)
	}
	fmt.Print("================\n")
	// p1 没有 Addr，就不会打印了
	fmt.Printf("%v\n", p1)
	fmt.Printf("%#v\n", p1)
	fmt.Printf("%T\n", p1)
	fmt.Printf("%s\n", data1)

	// ================

	p2 := Person{
		Name: "Jack",
		Age:  22,
		Addr: "China",
	}

	data2, err := json.Marshal(p2)
	if err != nil {
		panic(err)
	}

	// p2 则会打印所有
	fmt.Printf("%s\n", data2)
}
