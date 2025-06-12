from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Khởi tạo hashmap để lưu lần đầu xuất hiện của prefix_sum
        # sum_to_index[total] = vị trí đầu tiên xuất hiện (index)
        sum_to_index = {0: -1}  # prefix_sum = 0 xảy ra tại vị trí -1 (trước mảng)
        max_len = 0  # Biến lưu kết quả độ dài lớn nhất
        total = 0  # Tổng tích lũy (prefix sum)

        for i in range(len(nums)):
            # Bước 1: Chuyển 0 thành -1, giữ 1 là 1
            if nums[i] == 0:
                total += -1
            else:
                total += 1
            # Bước 2: Kiểm tra xem tổng này đã xuất hiện trước chưa
            if total in sum_to_index:
                # Nếu có rồi, đoạn giữa 2 lần đó có tổng bằng 0 → cân bằng
                # ===> ví dụ 1 + 0 = 1 ===> 1 - 1 = 0 (đoạn giữa = 0) => -1 và 1 là cân bằng => mà 0 là -1 => 0 và 1 là cân bằng
                prev_index = sum_to_index[total]
                length = i - prev_index
                max_len = max(max_len, length)  # Cập nhật độ dài lớn nhất nếu cần
            else:
                # Nếu chưa có, lưu lại vị trí đầu tiên có tổng này
                sum_to_index[total] = i

        return max_len


class SolutionOptimized:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        max_len = 0
        sum_to_index = {0: -1}

        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1

            if count in sum_to_index:
                max_len = max(max_len, i - sum_to_index[count])
            else:
                sum_to_index[count] = i

        return max_len


# --- TEST ---
nums = [0, 1, 1, 1, 1, 1, 0, 0, 0]
sol = Solution()
print("Max balanced subarray length:", sol.findMaxLength(nums))
