/*
 * Desc:
 * File: /query_post_form.go
 * Project: routers
 * File Created: Thursday, 31st August 2023 3:51:17 pm
 * Author: luxuemin2108@gmail.com
 * -----
 * Copyright (c) 2023 Camel Lu
 */
package routers

import (
	"fmt"

	"github.com/gin-gonic/gin"
)

func SetQueryPostForm(r *gin.Engine) {
	r.POST("/query_post_form", func(c *gin.Context) {
		// obj := make(map[string]interface{})
		// c.BindJSON(&obj)
		// fmt.Println(obj)
		// fmt.Println(obj["user"])
		id := c.Query("id")
		page := c.DefaultQuery("page", "0")
		name := c.PostForm("name")
		message := c.PostForm("message")

		fmt.Printf("id: %s; page: %s; name: %s; message: %s", id, page, name, message)
	})
}
