package main


import (
	"fmt"
	"time"
)

func goroutineA(a <-chan int) {
	val := <- a
	fmt.Println("G1 received data: ", val)
	return
}

func goroutineB(b <-chan int) {
	val := <- b
	fmt.Println("G2 received data: ", val)
	return
}

func main() {
	// ch := make(chan int)
	// go goroutineA(ch)
	// go goroutineB(ch)
	// ch <- 3
	// time.Sleep(time.Second)
	test_without_buffer()
	test_buffer_chan()
}

func test_without_buffer() {
     var ch = make(chan string)

     for i := 0; i < 10; i++ {
             go sum(i, i+10, ch)
     }
		 for i := 0; i < 10; i++ {
					fmt.Print(<-ch)
		}

}

func test_buffer_chan() {
	message_chan := make(chan int, 2)

	go func() {
		time.Sleep(time.Second * 3)
		println("start recv...")
		println(<-message_chan)
		println(<-message_chan)
		println(<-message_chan)
		println("finish recv...")
	}()

	println("start send 10...")
	message_chan <- 10

	println("start send 20...")
	message_chan <- 20

	println("start send 30...")
	message_chan <- 30
	println("end send 30...")

	println("finish send...")

	time.Sleep(time.Second * 3)
	close(message_chan)
}

func sum(start, end int, ch chan string) {
     var sum int = 0
     for i := start; i < end; i++ {
             sum += i
     }
     ch <- fmt.Sprintf("Sum from %d to %d is %d\n", start, end, sum)
}
