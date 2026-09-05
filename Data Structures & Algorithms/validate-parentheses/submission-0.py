class Solution:
    def isValid(self, s: str) -> bool:
        check = {'{': '}', '[': ']', '(': ')'}
        stack = []

        for char in s:  
            if char in check:
                stack.append(char)
            else:
                if not stack:
                    return False
                if char == check[stack[-1]]:
                    stack.pop()
                else:
                    return False
        
        return not stack