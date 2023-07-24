/*
 * Desc:
 * File: /personal/project/learn-gin/routers/validators.go
 * Project: edy
 * File Created: Friday, 21st July 2023 7:17:34 pm
 * Author: luxuemin2108@gmail.com
 * -----
 * Copyright (c) 2022 Camel Lu
 */
package routers

import (
	"net/http"
	"time"

	"github.com/gin-gonic/gin"
	"github.com/gin-gonic/gin/binding"
	"github.com/go-playground/validator/v10"
)

// Booking contains binded and validated data.
type Booking struct {
	CheckIn  time.Time `form:"check_in" binding:"required,bookabledate" time_format:"2006-01-02"`
	CheckOut time.Time `form:"check_out" binding:"required,gtfield=CheckIn,bookabledate" time_format:"2006-01-02"`
}

var bookableDate validator.Func = func(fl validator.FieldLevel) bool {
	date, ok := fl.Field().Interface().(time.Time)
	if ok {
		today := time.Now()
		if today.After(date) {
			return false
		}
	}
	return true
}

// curl "localhost:8088/bookable?check_in=2023-08-16&check_out=2023-08-27"
func getBookable(c *gin.Context) {
	var b Booking
	if err := c.ShouldBindWith(&b, binding.Query); err == nil {
		c.JSON(http.StatusOK, gin.H{"message": "Booking dates are valid!"})
	} else {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
	}
}

func SetValidatorsRoute(r *gin.Engine) {

	if v, ok := binding.Validator.Engine().(*validator.Validate); ok {
		v.RegisterValidation("bookabledate", bookableDate)
	}
	r.GET("/bookable", getBookable)
}
