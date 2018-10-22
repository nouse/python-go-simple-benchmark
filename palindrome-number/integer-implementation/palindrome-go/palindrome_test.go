package palindrome

import "testing"

func BenchmarkPalindrome(b *testing.B) {
	for i := 0; i < b.N; i++ {
		PalindromeNumber()
	}
}

func TestPalindromeNumber(t *testing.T) {
	num := PalindromeNumber()
	if num != 585 {
		t.Errorf("Expected PalindromeNumber2 to return 585, actual %d", num)
	}
}
