class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numdict = {}
        for n in nums:
            if n not in numdict:
                numdict[n] = 1
            elif n in numdict:
                return True
        return False

        