class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numList = {}
        for num in nums:
            if num not in numList:
                numList[num] = 1
            else:
                numList[num] += 1
        for val in numList:
            if numList[val] > len(nums) // 2:
                return val
