CANDIDATES = [
    11, 33, 55, 77, 99,
    101, 111, 121, 131, 141, 151, 161, 171, 181, 191,
    303, 313, 323, 333, 343, 353, 363, 373, 383, 393,
    505, 515, 525, 535, 545, 555, 565, 575, 585, 595,
    707, 717, 727, 737, 747, 757, 767, 777, 787, 797,
    909, 919, 929, 939, 949, 959, 969, 979, 989, 999,
]


def is_palindrome(s: str) -> bool:
    ls = len(s)
    max = ls // 2
    for i in range(max):
        if s[i] != s[ls - 1 - i]:
            return False
    return True

def palindrome_number() -> int:
    for num in CANDIDATES:
        o = f'{num:o}'
        if not is_palindrome(o):
            continue

        o = f'{num:b}'
        if is_palindrome(o):
            return num

    return -1
