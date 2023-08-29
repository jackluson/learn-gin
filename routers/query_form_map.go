/*
 * Desc:
 * File: /query_form_map.go
 * Project: routers
 * File Created: Wednesday, 23rd August 2023 6:59:53 pm
 * Author: luxuemin2108@gmail.com
 * -----
 * Copyright (c) 2023 Camel Lu
 */

package routers

import (
	"fmt"

	"github.com/gin-gonic/gin"
)

func SetQueryFormMap(r *gin.Engine) {

	r.POST("/post", func(c *gin.Context) {
		// fmt.Println("c.Request.RequestURI", c.Request.RequestURI)
		ids := c.QueryMap("ids")
		names := c.PostFormMap("names")
		fmt.Println(names)
		val, ok := names["chicago"]
		fmt.Println("ok", ok)

		if ok {
			fmt.Println(val, ok)
		}

		fmt.Printf("ids: %v; names: %v", ids, names)
	})
}
