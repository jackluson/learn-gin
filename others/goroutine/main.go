/*
 * Desc:
 * File: /main.go
 * Project: goroutine
 * File Created: Thursday, 31st August 2023 6:15:20 pm
 * Author: luxuemin2108@gmail.com
 * -----
 * Copyright (c) 2023 Camel Lu
 */

package main

import (
	"fmt"
	"sync"
)

func A(i int) {
	fmt.Println("我是A", i)
}
func SyncWaitGroupWay() {
	var wg sync.WaitGroup
	fmt.Println("我是main") // 1
	wg.Add(1)
	// go A(1)
	go func(i int) {
		defer wg.Done()
		A(i)                        // 2
		fmt.Println("after finish") // 3

	}(1)
	wg.Wait()
	fmt.Println("执行完了") // 3
}

func SyncCondWay() {
	var locker = new(sync.Mutex)
	var cond = sync.NewCond(locker)
	var done bool = false
	fmt.Println("我是main")
	cond.L.Lock()
	go func(i int) {
		A(i)
		fmt.Println("finish")
		done = true
		cond.Signal()
	}(1)
	fmt.Println("start wait", done)
	if !done {
		fmt.Println("waiting")
		cond.Wait()
		cond.L.Unlock()
	}
	fmt.Println("finished wait", done)
	fmt.Println("执行完了")
}

func Fn(i int) {
	fmt.Println("我是A", i)
	// defer func() { //在panic后声明defer,不能捕获异常
	// 	if err := recover(); err != nil {
	// 		fmt.Println("恢复", err)
	// 	} else {
	// 		fmt.Println("没有异常")
	// 	}
	// 	// fmt.Println("defer")

	// }()
	panic("崩溃")
	// fmt.Println("我是A", i)

}

func recoverDefer() {
	var wg sync.WaitGroup
	fmt.Println("我是main")
	wg.Add(1)
	go func(i int) {
		defer func() { //在panic后声明defer,不能捕获异常
			if err := recover(); err != nil {
				fmt.Println("恢复", err)
			} else {
				fmt.Println("没有异常")
			}
			wg.Done()
			// fmt.Println("defer")

		}()
		Fn(i)

	}(1)
	wg.Wait()

	fmt.Println("执行完了")
}

func main_pre() {
	// SyncWaitGroupWay()
	// SyncCondWay()
	recoverDefer()
}

// from https://zhuanlan.zhihu.com/p/374464199
