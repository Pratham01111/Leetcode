from typing import List


# --- Contains Duplicate ---
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = set()
        for n in nums:
            if n in hashmap:
                return True
            hashmap.add(n)
        return False
    
# --- Valid Anagram ---
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return Counter(s)==Counter(t)
    
    #2nd soln better time complexity
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_freq = {}     #making a dict to store the frequency of characters in s
        
        for c in s:
            char_freq[c] = char_freq.get(c, 0) + 1
            
        for c in t:
            if c not in char_freq:
                return False
            char_freq[c] -= 1
            if dict[c] < 0:
                return False
            
        return True

# --- Two Sum (brute force) ---
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  # no solution found
    
# --- Two Sum (hashmap) ---
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prevMap = {} #for value : index

        for i, n in enumerate(nums):
            diff=target-n
            if diff in prevMap:
                return[prevMap[diff], i]
            prevMap[n]=i
