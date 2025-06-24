# Range Sum Query - Immutable

from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        #  Khởi tạo mảng prefix với độ dài bằng độ dài của mảng nums
        self.prefix = [0] * len(nums)
        # Nếu mảng nums không rỗng, tính toán mảng prefix
        if nums:
            # Phần tử đầu tiên của mảng prefix là phần tử đầu tiên của mảng nums
            self.prefix[0] = nums[0]
            # Tính toán các phần tử còn lại của mảng prefix từ 1 đến cuối mảng nums
            for i in range(1, len(nums)):
                self.prefix[i] = self.prefix[i - 1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        # Hàm để tính tổng từ chỉ số left đến right
        # Nếu left là 0, trả về giá trị tại chỉ số right trong mảng prefix
        if left == 0:
            return self.prefix[right]
        # Nếu không, trả về hiệu giữa giá trị tại chỉ số right và giá trị tại chỉ số left - 1 trong mảng prefix
        # [left - 1] là chỉ số của phần tử cuối cùng không được tính trong tổng
        return self.prefix[right] - self.prefix[left - 1]


# === TEST BÀI TOÁN ===
commands = ["NumArray", "sumRange", "sumRange", "sumRange"]
inputs = [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]

result = []
obj = None

for command, param in zip(commands, inputs):
    if command == "NumArray":
        obj = NumArray(*param)
        result.append(None)  # Constructor trả về null
    elif command == "sumRange":
        result.append(obj.sumRange(*param))

print("Output:", result)  # Output: [None, 1, -1, -3]


# [-2, 0, 3, -5, 2, -1]
# prefix =  [-2, -2, 1, -4, -2, -3]
# ===
# [0]
# [0] + [1]
# [0] + [1] + [2] = left
# [0] + [1] + [2] + [3] + [4] + [5] = right
# ==> sum left -> right => 2 -> 5 =>  [2] + [3] + [4] + [5] => remove  [0] + [1] = prefix[1]
# => prefix[right] - prefix[left - 1]
