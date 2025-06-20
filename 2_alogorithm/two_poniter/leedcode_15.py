from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, val in enumerate(nums):
            if i > 0 and val == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                threeSum = val + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    result.append([val, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return result


solution = Solution()
# Example usage:
print(solution.threeSum([-1, 0, 1, 2, -1, -4]))  # Output: [[-1, -1, 2], [-1, 0, 1]]


# Example usage: https://www.youtube.com/watch?v=jzZsG8n2R9A
