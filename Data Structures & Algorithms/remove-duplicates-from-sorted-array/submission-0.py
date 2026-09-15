class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nonDupes = []
        for num in nums[:]:
            if num not in nonDupes:
                nonDupes.append(num)
            else:
                nums.remove(num)
        return len(nums)
        