#-------9. Palindrome Number----------
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        l,r=0,len(x)-1
        while l<r:
            if x[l]==x[r]:
                l+=1
                r-=1
            else:
                return False
        return True
x=121
o=Solution()
print(o.isPalindrome(x))

'''
9. Palindrome Number
Solved
Easy
Topics
Companies
Hint
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1'''
