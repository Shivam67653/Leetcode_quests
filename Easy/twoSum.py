# 1. Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

def twoSum(nums, target):
    num_map = {}  # This is your data container!
    
    for i, num in enumerate(nums):  # You look at every number and its position
        complement = target - num   # What number do I need to reach the target?
        
        if complement in num_map:   # Have I seen that needed number before?
            return [num_map[complement], i]  # If yes — Yay! Found the two spots!
        
        num_map[num] = i  # Didn't find it? No problem! Write this number