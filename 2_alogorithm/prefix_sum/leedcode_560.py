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


# === TESTING ALL SOLUTIONS ===
# # BƯỚC 1: Brute Force - Kiểm tra tất cả subarray
# def subarraySum_bruteforce(nums, k):
#     """
#     Tư duy: Kiểm tra từng subarray có tổng = k
#     Time: O(n^2), Space: O(1)
#     """
#     n = len(nums)
#     count = 0

#     for i in range(n):
#         current_sum = 0
#         for j in range(i, n):
#             current_sum += nums[j]
#             if current_sum == k:
#                 count += 1

#     return count


# # BƯỚC 2: Optimal - Prefix Sum + HashMap
# def subarraySum_optimal(nums, k):
#     """
#     Tư duy: prefix_sum[j] - prefix_sum[i] = k
#            → prefix_sum[i] = prefix_sum[j] - k

#     Time: O(n), Space: O(n)
#     """
#     # HashMap: prefix_sum → frequency
#     prefix_map = {0: 1}  # prefix_sum = 0 xuất hiện 1 lần (trước mảng)

#     count = 0
#     current_sum = 0

#     for num in nums:
#         current_sum += num

#         # Tìm target = current_sum - k
#         target = current_sum - k
#         if target in prefix_map:
#             count += prefix_map[target]

#         # Cập nhật frequency của current_sum
#         prefix_map[current_sum] = prefix_map.get(current_sum, 0) + 1

#     return count


# # BƯỚC 3: Trace chi tiết để hiểu thuật toán
# def subarraySum_with_trace(nums, k):
#     """
#     Version có trace để debug và hiểu thuật toán
#     """
#     print(f"Input: nums = {nums}, k = {k}")
#     print(f"Tìm số subarray có tổng = {k}\n")

#     prefix_map = {0: 1}
#     count = 0
#     current_sum = 0

#     print("Step | num | current_sum | target | found | count | prefix_map")
#     print("-" * 65)

#     for i, num in enumerate(nums):
#         current_sum += num
#         target = current_sum - k

#         found_count = prefix_map.get(target, 0)
#         count += found_count

#         print(
#             f"{i:4} | {num:3} | {current_sum:11} | {target:6} | {found_count:5} | {count:5} | ",
#             end="",
#         )

#         # Cập nhật prefix_map
#         prefix_map[current_sum] = prefix_map.get(current_sum, 0) + 1
#         print(f"{prefix_map}")

#     print(f"\nKết quả: {count}")
#     return count


# # Test với các ví dụ
# def test_solutions():
#     test_cases = [
#         ([1, 1, 1], 2),  # Expected: 2
#         ([1, 2, 3], 3),  # Expected: 2
#         ([1], 0),  # Expected: 0
#         ([1], 1),  # Expected: 1
#         ([1, -1, 0], 0),  # Expected: 3
#         ([3, 4, 7, 2, -3, 1, 4, 2], 7),  # Expected: 4
#     ]

#     print("=== TESTING ALL SOLUTIONS ===")
#     for i, (nums, k) in enumerate(test_cases):
#         print(f"\nTest case {i+1}: nums = {nums}, k = {k}")

#         result1 = subarraySum_bruteforce(nums, k)
#         result2 = subarraySum_optimal(nums, k)

#         print(f"Brute force: {result1}")
#         print(f"Optimal:     {result2}")
#         print(f"Match: {'✓' if result1 == result2 else '✗'}")


# # Chi tiết trace cho ví dụ cụ thể
# def detailed_example():
#     print("\n" + "=" * 50)
#     print("DETAILED TRACE EXAMPLE")
#     print("=" * 50)

#     # Ví dụ 1
#     print("\n--- Example 1 ---")
#     subarraySum_with_trace([1, 1, 1], 2)

#     # Ví dụ 2
#     print("\n--- Example 2 ---")
#     subarraySum_with_trace([1, 2, 3], 3)

#     # Ví dụ phức tạp hơn
#     print("\n--- Complex Example ---")
#     subarraySum_with_trace([1, -1, 0], 0)


# # Giải thích manual cho ví dụ đầu tiên
# def manual_explanation():
#     print("\n" + "=" * 50)
#     print("MANUAL EXPLANATION")
#     print("=" * 50)

#     nums = [1, 1, 1]
#     k = 2
#     print(f"nums = {nums}, k = {k}")
#     print("Tìm tất cả subarray có tổng = 2:")

#     print("\nTất cả subarray có thể:")
#     for i in range(len(nums)):
#         for j in range(i, len(nums)):
#             subarray = nums[i : j + 1]
#             sum_val = sum(subarray)
#             match = "✓" if sum_val == k else " "
#             print(f"  [{i}:{j}] = {subarray} → sum = {sum_val} {match}")

#     print(f"\nCó 2 subarray có tổng = {k}:")
#     print("  - [0:1] = [1,1] → sum = 2")
#     print("  - [1:2] = [1,1] → sum = 2")


# if __name__ == "__main__":
#     # Chạy test
#     test_solutions()

#     # Trace chi tiết
#     detailed_example()

#     # Giải thích manual
#     manual_explanation()
