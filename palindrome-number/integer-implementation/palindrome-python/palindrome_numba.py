import numpy
from numba import jit, int32

CANDIDATES = numpy.array([
    11, 33, 55, 77, 99,
    101, 111, 121, 131, 141, 151, 161, 171, 181, 191,
    303, 313, 323, 333, 343, 353, 363, 373, 383, 393,
    505, 515, 525, 535, 545, 555, 565, 575, 585, 595,
    707, 717, 727, 737, 747, 757, 767, 777, 787, 797,
    909, 919, 929, 939, 949, 959, 969, 979, 989, 999,
])


REVERSE_TABLE = numpy.array([0, 4, 2, 6, 1, 5, 3, 7])
MOV_TABLE = numpy.array([0, 1, 2, 2, 3, 3, 3, 3])
REM_TABLE = numpy.array([0, 1, 1, 3, 1, 5, 3, 7])


@jit(int32(int32))
def reverse2(num: int) -> int:
    result = REVERSE_TABLE[num & 7]
    remain = num >> 3
    while remain > 7:
        result = (result << 3) + REVERSE_TABLE[remain & 7]
        remain >>= 3

    if remain == 0:
        return result

    return (result << MOV_TABLE[remain]) + REM_TABLE[remain]


@jit(int32(int32))
def reverse8(num: int) -> int:
    result = num & 7
    remain = num >> 3
    while remain > 0:
        result = (result << 3) + (remain & 7)
        remain >>= 3

    return result


@jit(int32())
def palindrome_numba() -> int:
    for num in CANDIDATES:
        if num == reverse8(num) and num == reverse2(num):
            return num

    return -1
