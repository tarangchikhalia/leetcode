#!/usr/bin/python3

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Time: O(n)
        # Space: O(n)
        seen = {}
        for index, value in enumerate(nums):
            remaining_value = target - value
            if remaining_value in seen:
                return [seen[remaining_value], index]
            seen[value] = index
        return []