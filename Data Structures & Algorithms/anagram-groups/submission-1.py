class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        li = []
        for s in strs:
            if "".join(sorted(s)) not in map:
                map["".join(sorted(s))] = [s]
            else:
                map["".join(sorted(s))].append(s)

        for i in map.values():
            li.append(i)
        
        return li