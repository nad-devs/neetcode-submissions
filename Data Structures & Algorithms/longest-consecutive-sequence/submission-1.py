class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash = set(nums)
        max_length = 0

        for i in nums:
            if (i-1) not in hash:
                start_sequence = i
                current_num = start_sequence
                length = 1
                while (current_num + 1) in hash:
                    current_num += 1
                    length += 1
                if max_length < length:
                    max_length = length
        return max_length
            