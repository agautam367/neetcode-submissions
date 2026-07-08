from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq=defaultdict(list)
        for i in range(len(strs)):
            temp=''.join(sorted(strs[i]))
            freq[temp].append(strs[i])
        return list(freq.values())



        