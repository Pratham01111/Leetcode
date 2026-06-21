# --- Valid Palindrome(using alphanum and extra memory) ---
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr=""

        for c in s:
            if c.isalnum():
                newstr+=c.lower()
        return newstr == newstr[::-1]
    
    #alphanumeric check: isalnum() method returns True if all characters in the string are alphanumeric (either alphabets or numbers) and there is at least one character, otherwise it returns False.
        
# --- Valid Palindrome(two pointers the better way) ---
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True