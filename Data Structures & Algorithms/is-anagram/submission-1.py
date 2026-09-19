class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hasht = {}
        hashs = {}

        if len(s) != len(t):
            return False
            
        for i in t:
            if i in hasht.keys():
                hasht[i] += 1
            else:
                hasht[i] = 1
        
        for i in s:
            if i in hashs.keys():
                hashs[i] += 1
            else:
                hashs[i] = 1
        
        return hashs == hasht