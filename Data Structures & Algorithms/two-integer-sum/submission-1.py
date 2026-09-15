class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for n in range(len(nums)):
            difference = target - nums[n]
            if difference not in diff:
                diff[nums[n]] = difference
            elif difference in diff:
                return [nums.index(difference),n]

        