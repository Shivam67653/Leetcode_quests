# 643. Maximum Average Subarray I
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000
 

# Constraints:

# n == nums.length
# 1 <= k <= n <= 105
# -104 <= nums[i] <= 104

def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[:k])      #Sum elements before the Kth element
        m = s
        for i in range(k, len(nums)):        # We move with K till end
            s += nums[i] - nums[i - k]        #We add the removal of initial elements (This is the core logic. It may take time to understand)
            if s > m:
                m = s
        return m / float(k)  #We divide the maximum sum by the total elements required for average