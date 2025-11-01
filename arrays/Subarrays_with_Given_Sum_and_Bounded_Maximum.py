"""
Given an integer array nums and integers k and M, count the number of contiguous subarrays whose sum equals k and whose maximum element is at most M.

Example:
Input:
nums = [2, -1, 2, 1, -2, 3]
k = 3 M = 2

Output:
2

Explanation:
We need subarrays with sum = 3 and all elements ≤ 2. 
Also, any subarray containing 3 is invalid because 3 > M. Check all starts:
- From index 0: [2, -1, 2] → sum = 3, max = 2 → valid (count = 1).
- From index 2: [2, 1] → sum = 3, max = 2 → valid 
"""
def countSubarraysWithSumAndMaxAtMost(nums, k, M):
    counter = 0
    n = len(nums)
    
    for i in range(n):
        cur_sum = 0
        j = i
        while (j < n and nums[j] <= M ):
            cur_sum += nums[j]
            if cur_sum == k:
                counter += 1
            j += 1
    
    return counter
