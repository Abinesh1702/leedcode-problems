#----Pascal's Triangle----------
def check(numRows):
    res=[[1]]
    for i in range(numRows-1):
        temp=[0]+res[-1]+[0]
        temp_res=[]
        for i in range(len(temp)-1):
            temp_res.append(temp[i]+temp[i+1])
        res.append(temp_res)
    return res
numRows=5
print(check(numRows))
'''
118. Pascal's Triangle
Solved
Easy
Topics
Companies
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30'''