/*
 * Desc:
 * File: /jsonp.go
 * Project: routers
 * File Created: Wednesday, 23rd August 2023 5:41:30 pm
 * Author: luxuemin2108@gmail.com
 * -----
 * Copyright (c) 2023 Camel Lu
 */

package routers

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func SetJsonp(r *gin.Engine) {
	r.GET("/JSONP", func(c *gin.Context) {
		data := map[string]interface{}{
			"foo": "bar",
		}

		//callback is x
		// Will output  :   x({\"foo\":\"bar\"})
		c.JSONP(http.StatusOK, data)
	})
}
