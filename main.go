package main

import (
	"learn-gin/middleware"
	"learn-gin/routers"
	"log"
	"net/http"

	"github.com/gin-gonic/gin"
)

type Person struct {
	ID   string `uri:"id" binding:"required,uuid"`
	Name string `uri:"name" binding:"required"`
}

func setupRouter() *gin.Engine {
	// Disable Console Color
	// gin.DisableConsoleColor()
	// gin.ForceConsoleColor()

	r := gin.Default()
	middleware.InitLog(r)
	gin.DebugPrintRouteFunc = func(httpMethod, absolutePath, handlerName string, nuHandlers int) {
		log.Printf("endpoint %v %v %v %v\n", httpMethod, absolutePath, handlerName, nuHandlers)
	}

	r.Use(gin.Recovery())
	// Ping test
	r.GET("/ping", func(c *gin.Context) {
		c.String(http.StatusOK, "pong")
	})
	routers.SetTemplate(r)
	routers.SetBindForm(r)
	routers.SetBindUri(r)
	routers.SetBasicAuth(r)
	routers.SetSyncAsyncRoute(r)
	routers.SetValidatorsRoute(r)
	routers.SetGroupRoute(r)
	routers.SetJsonp(r)
	routers.SetQueryFormMap(r)
	routers.SetBindAndValidation(r)
	r.GET("/someJSON", func(c *gin.Context) {
		data := map[string]interface{}{
			"lang": "GO语言",
			"tag":  "<br>",
		}

		// will output : {"lang":"GO\u8bed\u8a00","tag":"\u003cbr\u003e"}
		c.AsciiJSON(http.StatusOK, data)
	})

	return r
}

func main() {
	r := setupRouter()
	// Listen and Server in 0.0.0.0:8080
	r.Run(":8088")
}

// curl -v localhost:8088/thinkerou/987fbc97-4bed-5078-9f07-9141ba07c9f3
