class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(char for char in s.lower() if char.isalnum())
        print(clean)
        print(clean[::-1])
        if clean == clean[::-1]:
            return True
        else:
            return False
