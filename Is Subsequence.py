#------392.Is Subsequence---------
def check(s,t):
    p1=0
    p2=0
    while p1<len(t) and p2<len(s):
        if t[p1]==s[p2]:
            p1+=1
            p2+=1
        else:
            p1+=1
    if p2==len(s):
        return True
    else:
        return False

s = "abc"
t = "acbgd"
print(check(s,t))

'''
392. Is Subsequence
Solved
Easy
Topics
Companies
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.'''
