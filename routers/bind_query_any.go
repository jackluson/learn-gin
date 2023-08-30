/*
 * Desc:
 * File: /bind_query_any.go
 * Project: routers
 * File Created: Wednesday, 30th August 2023 6:25:56 pm
 * Author: luxuemin2108@gmail.com
 * -----
 * Copyright (c) 2023 Camel Lu
 */

package routers

import (
	"log"

	"github.com/gin-gonic/gin"
)

type person struct {
	Name    string `form:"name"`
	Address string `form:"address"`
}

func handleBindQueryAny(c *gin.Context) {
	var person person
	if c.ShouldBindQuery(&person) == nil {
		log.Println("====== Only Bind By Query String ======")
		log.Println(person.Name)
		log.Println(person.Address)
	}
	c.String(200, "Success")
}

func SetBindQueryAny(r *gin.Engine) {
	r.Any("/setbindqueryany", handleBindQueryAny)
}
