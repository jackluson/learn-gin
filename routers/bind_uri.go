/*
 * Desc:
 * File: /bind_uri.go
 * Project: routers
 * File Created: Tuesday, 22nd August 2023 6:17:52 pm
 * Author: luxuemin2108@gmail.com
 * -----
 * Copyright (c) 2023 Camel Lu
 */
package routers

import "github.com/gin-gonic/gin"

type PersonInfo struct {
	ID   string `uri:"id" binding:"required,uuid"`
	Name string `uri:"name" binding:"required"`
}

func SetBindUri(r *gin.Engine) {
	r.GET("/:name/:id", func(c *gin.Context) {
		var person PersonInfo
		if err := c.ShouldBindUri(&person); err != nil {
			c.JSON(400, gin.H{"msg": err})
			return
		}
		c.JSON(200, gin.H{"name": person.Name, "uuid": person.ID})
	})
}
