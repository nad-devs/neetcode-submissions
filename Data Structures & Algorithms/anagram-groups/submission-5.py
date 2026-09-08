class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #make a default dict
        group = defaultdict(list)
        #take element from strs 
        for word in strs:
           key = tuple(sorted(word))
           group[key].append(word)
        return list(group.values())


        
            

         