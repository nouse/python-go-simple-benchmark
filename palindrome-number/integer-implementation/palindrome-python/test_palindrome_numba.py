from palindrome_numba import palindrome_numba


def test_numba_answer():
    assert palindrome_numba() == 585


def test_palindrome_numba(benchmark):
    benchmark(palindrome_numba)

