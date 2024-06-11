#------- valid Paranthesis-------
class Solution:
    def isValid(self, s: str) -> bool:
        empty = []
        mapping = {')': '(', '}': '{', ']': '['}
        for i in s:
            if i in mapping:
                if not empty or mapping[i] != empty.pop():
                    return False
            else:
                empty.append(i)
        return not empty
s='{}'
o=Solution()
print(o.isValid(s))

'''
20. Valid Parentheses
Solved
Easy
Topics
Companies
Hint
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''