#-------53. Maximum Subarray-----------
def check(nums):
    cur_val = 0
    max_val = min(nums)
    if len(nums) == 1:
        return nums[0]
    for i in nums:
        cur_val += i
        max_val = max(cur_val, max_val)
        if cur_val < 0:
            cur_val = 0

    return max_val
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(check(nums))
'''
53. Maximum Subarray
Solved
Medium
Topics
Companies
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''