/*
 * Desc:
 * File: /personal/project/learn-gin/modules/sync_async.go
 * Project: edy
 * File Created: Friday, 21st July 2023 5:45:18 pm
 * Author: luxuemin2108@gmail.com
 * -----
 * Copyright (c) 2022 Camel Lu
 */
package routers

import (
	"log"
	"time"

	"github.com/gin-gonic/gin"
)

func SetSyncAsyncRoute(r *gin.Engine) {
	r.GET("/long_async", func(c *gin.Context) {
		// create copy to be used inside the goroutine
		cCp := c.Copy()
		go func() {
			// simulate a long task with time.Sleep(). 5 seconds
			time.Sleep(5 * time.Second)

			// note that you are using the copied context "cCp", IMPORTANT
			log.Println("Done! in path " + cCp.Request.URL.Path)
		}()
	})

	r.GET("/long_sync", func(c *gin.Context) {
		// simulate a long task with time.Sleep(). 5 seconds
		time.Sleep(5 * time.Second)

		// since we are NOT using a goroutine, we do not have to copy the context
		log.Println("Done! in path " + c.Request.URL.Path)
	})

}
