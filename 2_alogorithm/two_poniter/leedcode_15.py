from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(f"Sorted nums: {nums}")
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                print(f"Skip duplicate at i={i} with value={nums[i]}")
                continue  # bỏ qua số đã xét trước đó

            left = i + 1
            right = len(nums) - 1
            print(f"\nFixing nums[{i}] = {nums[i]}")

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                print(
                    f"  Checking triplet ({nums[i]}, {nums[left]}, {nums[right]}) = {total}"
                )

                if total < 0:
                    print(f"    Sum < 0 → Move left from {left} to {left + 1}")
                    left += 1
                elif total > 0:
                    print(f"    Sum > 0 → Move right from {right} to {right - 1}")
                    right -= 1
                else:
                    print(
                        f"    Found triplet: [{nums[i]}, {nums[left]}, {nums[right]}]"
                    )
                    res.append([nums[i], nums[left], nums[right]])

                    # Bỏ qua phần tử trùng ở left
                    while left < right and nums[left] == nums[left + 1]:
                        print(f"    Skip duplicate left at {left+1} = {nums[left+1]}")
                        left += 1

                    # Bỏ qua phần tử trùng ở right
                    while left < right and nums[right] == nums[right - 1]:
                        print(
                            f"    Skip duplicate right at {right-1} = {nums[right-1]}"
                        )
                        right -= 1

                    left += 1
                    right -= 1

        return res


solution = Solution()
# Example usage:
print(solution.threeSum([-1, 0, 1, 2, -1, -4]))  # Output: [[-1, -1, 2], [-1, 0, 1]]
