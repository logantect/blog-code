package io.playground.kotlin.basics

// 기본적인 함수 선언.
// 두 개의 `Int` 매개변수와 `Int` 반환타입이 있는 함수.
fun sum(a: Int, b: Int): Int {
    return a + b
}

// 표현식 스타일.
// 함수 본문은 표현식이 될 수 있다.
// 반환 타입이 유추 됨.
fun inferredSum(a: Int, b: Int) = a + b

// 의미 있는 값을 반환하지 않는 함수.
fun printSum(a: Int, b: Int): Unit {
    println("sum of $a and $b is ${a + b}")
}

// `Unit` 반환타입은 생략 가능하다.
fun omittedPrintSum(a: Int, b: Int) {
    println("sum of $a and $b is ${a + b}")
}

fun main() {
    println("Hello World!")
    println(sum(5, 3))
    println(inferredSum(10, 3))
    printSum(100, 500)
    omittedPrintSum(500, 500)
}