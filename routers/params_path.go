/*
 * Desc:
 * File: /params_path.go
 * Project: routers
 * File Created: Wednesday, 30th August 2023 7:04:44 pm
 * Author: luxuemin2108@gmail.com
 * -----
 * Copyright (c) 2023 Camel Lu
 */
package routers

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func SetParamsPath(r *gin.Engine) {
	r.GET("/tag/:tagId", func(c *gin.Context) {
		name := c.Param("tagId")
		c.String(http.StatusOK, "Hello %s", name)
	})
}
