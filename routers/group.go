/*
 * Desc:
 * File: /group.go
 * Project: routers
 * File Created: Thursday, 3rd August 2023 6:45:48 pm
 * Author: luxuemin2108@gmail.com
 * -----
 * Copyright (c) 2023 Camel Lu
 */

package routers

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func SetGroupRoute(r *gin.Engine) {
	v1 := r.Group("/v2")
	{
		v1.GET("/ping", func(c *gin.Context) {

			c.String(http.StatusOK, "pong v1")
		})
		v1.GET("/hello", func(c *gin.Context) {

			c.String(http.StatusOK, "hello v1")

		})
	}
}
