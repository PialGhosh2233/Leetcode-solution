class Solution:
    def isPalindrome(self, s: str) -> bool:
        y=""
        for i in s.lower():
            if i.isalnum():
                y+=i
        return y==y[::-1]