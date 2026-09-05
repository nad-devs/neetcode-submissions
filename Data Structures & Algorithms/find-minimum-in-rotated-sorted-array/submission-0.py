class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while right - left > 1:
            middle = (left + right) // 2
    
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle

        return min(nums[left], nums[right])