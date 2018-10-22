package palindrome

import "strconv"

var candidates = [55]int{
	11, 33, 55, 77, 99,
	101, 111, 121, 131, 141, 151, 161, 171, 181, 191,
	303, 313, 323, 333, 343, 353, 363, 373, 383, 393,
	505, 515, 525, 535, 545, 555, 565, 575, 585, 595,
	707, 717, 727, 737, 747, 757, 767, 777, 787, 797,
	909, 919, 929, 939, 949, 959, 969, 979, 989, 999,
}

// Util method to test if a string a palindrome
func isPalindrome(s string) bool {
	l := len(s)
	for i := 0; i <= l/2; i++ {
		if s[i] != s[l-1-i] {
			return false
		}
	}
	return true
}

// PalindromeNumber test number by trasforming to string
func PalindromeNumber() int {
	for _, num := range candidates {
		uintNum := int64(num)
		if isPalindrome(strconv.FormatInt(uintNum, 8)) &&
			isPalindrome(strconv.FormatInt(uintNum, 2)) {
			return num
		}
	}
	return -1
}
