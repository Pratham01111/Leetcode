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
