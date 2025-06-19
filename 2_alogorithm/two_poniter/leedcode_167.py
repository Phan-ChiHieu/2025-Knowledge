# 167. Two Sum II - Input Array Is Sorted

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []  # This line is not expected to be reached as per problem constraints


# Example usage:
# solution = Solution()
# print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [1, 2]
# print(solution.twoSum([2, 3, 4], 6))  # Output: [1, 3]
# print(solution.twoSum([-1, 0], -1))  # Output: [1, 2]
# print(solution.twoSum([5, 25, 75], 100))  # Output: [2, 3]
# print(solution.twoSum([1, 2, 3, 4, 4, 5], 8))  # Output: [4, 5]
# print(solution.twoSum([1, 2, 3],  6))  # Output: [2, 3]
