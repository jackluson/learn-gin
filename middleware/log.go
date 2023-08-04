/*
 * Desc:
 * File: /log.go
 * Project: routers
 * File Created: Friday, 4th August 2023 6:24:44 pm
 * Author: luxuemin2108@gmail.com
 * -----
 * Copyright (c) 2023 Camel Lu
 */
package middleware

import (
	"io"
	"os"

	"github.com/gin-gonic/gin"
)

func InitLog() {
	gin.DisableConsoleColor()

	// Logging to a file.
	f, _ := os.Create("gin.log")
	gin.DefaultWriter = io.MultiWriter(f)
}
