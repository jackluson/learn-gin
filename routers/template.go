/*
 * Desc:
 * File: /template.go
 * Project: routers
 * File Created: Tuesday, 22nd August 2023 6:53:17 pm
 * Author: luxuemin2108@gmail.com
 * -----
 * Copyright (c) 2023 Camel Lu
 */

package routers

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func SetTemplate(r *gin.Engine) {
	r.LoadHTMLGlob("templates/*")
	//r.LoadHTMLFiles("templates/template1.html", "templates/template2.html")
	r.GET("/index", func(c *gin.Context) {
		c.HTML(http.StatusOK, "index.tmpl", gin.H{
			"title": "Main website",
		})
	})
}
