package io.devdog.lotto

class LottoNumber private constructor(val number: Int) {

    companion object {
        fun from(number: Int): LottoNumber {
            return LottoNumber(number)
        }
    }

    override fun equals(other: Any?): Boolean {
        if (this === other) return true
        if (javaClass != other?.javaClass) return false

        other as LottoNumber

        if (number != other.number) return false

        return true
    }

    override fun hashCode(): Int {
        return number
    }

}