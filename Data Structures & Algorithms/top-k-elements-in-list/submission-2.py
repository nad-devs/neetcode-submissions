class Solution:
   def topKFrequent(self, nums, k):
       compare = {}
       for i in range(len(nums)):
           if nums[i] in compare:
               compare[nums[i]] += 1
           else:
               compare[nums[i]] = 1
       
       sorted_pairs = sorted(compare.items(), key=lambda x: x[1], reverse=True)
       return [pair[0] for pair in sorted_pairs[:k]]
