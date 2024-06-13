#--------283.Move zeros----------
def check(nums):
    res=0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[i],nums[res]=nums[res],nums[i]
            res+=1
    return nums
nums = [0, 1, 0, 3, 12]
print(check(nums))
'''
283. Move Zeroes
Solved
Easy
Topics
Companies
Hint
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
'''