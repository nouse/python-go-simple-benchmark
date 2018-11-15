# python-go-simple-benchmark
A python benchmark comparing to Go, using various performance enhancements.

# Benchmark Results

Environment: Linux Kernel 4.18.0.2, CPU i5-7300U

## String Implementation

- Go: 842.45K
- Python3: 52.30K
- PyPy3: 217.84K
- Cython: 719.92K
- TruffleRuby(Native): 56.74K
- TruffleRuby(JVM): 170.23K

## Integer Implementation

- Go: 5586.59K
- Python3: 64.92K
- PyPy3: 556.40K
- Numba: 7004.1K
- Cython: 10503.2K
- TruffleRuby(Native): 4468K
- TruffleRuby(JVM): 6558K
