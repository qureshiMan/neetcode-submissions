class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for i in nums:
            if not (i in s):
                s.add(i)
            else:
                return True
        return False
