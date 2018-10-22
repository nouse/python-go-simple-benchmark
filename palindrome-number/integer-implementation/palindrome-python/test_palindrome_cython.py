import palindrome_cython as p


def test_cython_answer():
    assert p.palindrome_cython() == 585


def test_palindrome_cython(benchmark):
    benchmark(p.palindrome_cython)

