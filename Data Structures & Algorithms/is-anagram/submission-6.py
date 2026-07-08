from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        freqs=Counter(s)
        freqt=Counter(t)

        if freqs==freqt:
            return True
        return False
        
        