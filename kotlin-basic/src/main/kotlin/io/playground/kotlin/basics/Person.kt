package io.playground.kotlin.basics

val javajigi = Person(name = "박재성", age = 49)
val jason = javajigi.copy(age = 30)

data class Person(val name: String, val age: Int)