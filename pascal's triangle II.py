#----------119. Pascal's Triangle II------------
def check(nums):
    res=[[1]]
    for i in range(nums):
        temp=[0]+res[-1]+[0]
        temp_res=[]
        for i in range(len(temp)-1):
            temp_res.append(temp[i]+temp[i+1])
        res.append(temp_res)
    return res[nums]
nums=4
print(check(nums))
'''
119. Pascal's Triangle II
Solved
Easy
Topics
Companies
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 33'''