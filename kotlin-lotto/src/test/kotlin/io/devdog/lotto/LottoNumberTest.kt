package io.devdog.lotto

import org.assertj.core.api.Assertions.assertThat
import org.junit.jupiter.api.Test

internal class LottoNumberTest {

    @Test
    internal fun `로또번호 생성`() {
        assertThat(LottoNumber.from(45)).isEqualTo(LottoNumber.from(45))
    }
}