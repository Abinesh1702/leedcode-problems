#-----125. Valid Palindrome---------
class Solution:
    def isPalindrome(self, s: str) -> bool:
        empty = []

        str = s.casefold()
        if str == '':
            return True
        for i in str:
            if i.isalnum():
                empty.append(i)
        l = 0
        r = len(empty) - 1
        while l < r:
            if empty[l] == empty[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
s='race a car'
o=Solution()
print(o.isPalindrome(s))


'''

125. Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.'''