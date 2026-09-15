class Solution:
    def maxArea(self, heights: List[int]) -> int:
        first = 0
        last = len(heights) - 1
        best = 0
        while first <= last:
            current = (last - first) * min(heights[first], heights[last])
            if current > best:
                best = current
            if heights[first] < heights[last]:
                first += 1
            elif heights[first] > heights[last]:
                last -= 1
            else:
                first += 1
                last -= 1
        return best
        
        