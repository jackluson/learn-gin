/*
 * Desc:
 * File: /redirect.go
 * Project: routers
 * File Created: Thursday, 31st August 2023 4:42:57 pm
 * Author: luxuemin2108@gmail.com
 * -----
 * Copyright (c) 2023 Camel Lu
 */

package routers

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func SetRedirect(r *gin.Engine) {
	r.GET("/redirect", func(c *gin.Context) {
		c.Redirect(http.StatusMovedPermanently, "http://www.google.com/")
	})

	r.GET("/redirect-test", func(c *gin.Context) {
		c.Request.URL.Path = "/redirect-test2"
		r.HandleContext(c)
	})
	r.GET("/redirect-test2", func(c *gin.Context) {
		c.JSON(200, gin.H{"hello": "world"})
	})
}
