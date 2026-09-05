class Solution:
   def isPalindrome(self, s: str) -> bool:
       # Clean the string
       new_string = ""
       for char in s:
           if char.isalnum():
               new_string += char.lower()
       
       # Two pointer approach
       left = 0
       right = len(new_string) - 1
       
       while left < right:
           if new_string[left] == new_string[right]:
               left += 1
               right -= 1
           else:
               return False
       
       return True
        