# 560. Subarray Sum Equals K

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = {0: 1}  # prefix_sum = 0 xuất hiện 1 lần (trước mảng)
        count = 0
        current_sum = 0

        for num in nums:
            current_sum += num

            # Tìm target = current_sum - k
            target = current_sum - k
            if target in prefix_map:
                count += prefix_map[target]

            # Cập nhật frequency của current_sum
            prefix_map[current_sum] = prefix_map.get(current_sum, 0) + 1

        return count
