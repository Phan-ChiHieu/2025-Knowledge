# Bước 1: Tạo mảng ban đầu
nums = [1, 2, 3, 4, 5, 6]

# Bước 2: Tính mảng prefix sum
# tạo một mảng prefix với độ dài bằng độ dài của mảng nums
prefix = [0] * len(nums)

# Phần tử đầu tiên của mảng prefix là phần tử đầu tiên của mảng nums
prefix[0] = nums[0]

for i in range(1, len(nums)):
    prefix[i] = prefix[i - 1] + nums[i]


# prefix = [1, 3, 6, 10, 15, 21]


# Hàm để tính tổng từ chỉ số i đến j
def range_sum(i, j):
    if i == 0:
        return prefix[j]
    return prefix[j] - prefix[i - 1]


# Ví dụ: tính tổng từ vị trí 1 đến 3
i, j = 1, 3
print(f"Tổng từ vị trí {i} đến {j} là: {range_sum(i, j)}")
