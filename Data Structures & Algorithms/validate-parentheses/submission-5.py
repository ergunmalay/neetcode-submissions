class Solution:
    def isValid(self, s: str) -> bool:
        
        # always look at the middle of the string and if it is true remove the middle
        split = list(s)

        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in split:
            if char in "([{":
                stack.append(char)
            elif not stack or stack.pop() != pairs[char]:
                return False

        return not stack


