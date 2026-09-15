class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        current = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current += 1
            elif nums[i] == 0:
                if current != 0 and max < current:
                    max = current
                current = 0
        if max > current:
            return max
        else:
            return current    


        