# 845. Longest Mountain in Array
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# You may recall that an array arr is a mountain array if and only if:

# arr.length >= 3
# There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.

 

# Example 1:

# Input: arr = [2,1,4,7,3,2,5]
# Output: 5
# Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
# Example 2:

# Input: arr = [2,2,2]
# Output: 0
# Explanation: There is no mountain.
 

# Constraints:

# 1 <= arr.length <= 104
# 0 <= arr[i] <= 104

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        max_len = 0
        i = 1

        while i < n - 1:
            # Check if current index is a peak
            if arr[i - 1] < arr[i] > arr[i + 1]:
                left = i - 1
                right = i + 1

                # Move left while increasing
                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1

                # Move right while decreasing
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1

                # Update max length
                max_len = max(max_len, right - left + 1)

                # Skip past the current mountain
                i = right
            else:
                i += 1

        return max_len