from palindrome import palindrome_number


def test_answer():
    assert palindrome_number() == 585


def test_palindrome(benchmark):
    benchmark(palindrome_number)
