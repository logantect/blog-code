package io.playground.kotlin.basics

val PI = 3.14
var x = 0

fun incrementX() {
    x += 1
}

fun main() {
    val a: Int = 1 // 즉시 할당
    val b = 2   // `Int` 타입 추측
    val c: Int  // 초기화가 제공되지 않을 때
    c = 3   // 지연된 할당
    println("a = $a, b = $b, c = $c")

    // var 키워드는 재할당이 가능하다
    var x = 5 // `Int` type is inferred
    x += 1
    println("x = $x")

    // 상위 레벨에 변수를 선언할 수 있다.
    println("x = $x; PI = $PI")
    incrementX()
    println("incrementX()")
    println("x = $x; PI = $PI")
}
