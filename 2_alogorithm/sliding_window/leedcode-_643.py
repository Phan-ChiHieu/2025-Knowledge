from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        w_s = sum(nums[:k])
        max_s = w_s

        for i in range(k, len(nums)):
            w_s = w_s - nums[i - k] + nums[i]
            max_s = max(max_s, w_s)

        return max_s / k


nums = [1,12,-5,-6,50,3], k = 4
solution = Solution()
print(solution.findMaxAverage(nums, 4))  # Output: 12.75