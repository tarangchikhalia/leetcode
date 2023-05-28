#!/usr/bin/python3

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Solution 1
        # Time: O(nlogn)
        # Space: O(n)
        if len(s) == len(t):
            if sorted(s) == sorted(t):
                return True
        return False
    
        # Solution 2
        # Time: O(n)
        # Space: O(n)
        if len(s) == len(t):

            s_hash_map = {}
            for char in s:
                s_hash_map[char] = 1 + s_hash_map.get(char,0)
            
            t_hash_map = {}
            for char in t:
                t_hash_map[char] = 1 + t_hash_map.get(char,0)
            
            if len(s_hash_map) != len(t_hash_map):
                return False
            
            for c in s_hash_map:
                if s_hash_map.get(c) != t_hash_map.get(c):
                    return False
            return True
        return False