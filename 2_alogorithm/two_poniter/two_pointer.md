Thuật toán **Two Pointer** (hai con trỏ) là một kỹ thuật rất phổ biến trong lập trình, đặc biệt là trong các bài toán **mảng**, **chuỗi**, hoặc **tìm kiếm**. Mục tiêu của kỹ thuật này là dùng **hai con trỏ (thường là chỉ số trong mảng)** để **duyệt mảng một cách hiệu quả hơn** so với các giải pháp duyệt đơn giản.

---

## 💡 **Ý tưởng cốt lõi:**

Thay vì dùng hai vòng lặp lồng nhau (O(n²)), ta dùng **hai con trỏ di chuyển theo cách thông minh** để giảm thời gian xuống O(n) hoặc O(n log n).

---

## 🎯 **Khi nào dùng Two Pointer?**

- Mảng đã **sắp xếp**
- Bài toán yêu cầu **tìm cặp**, **tổng**, **subarray**, hoặc **so sánh hai dãy**
- Tối ưu **O(n²)** xuống **O(n)**

---

## 🧠 **Các kiểu phổ biến:**

| Tình huống                                              | Cách đặt con trỏ                                   |
| ------------------------------------------------------- | -------------------------------------------------- |
| Tìm cặp có tổng bằng `target` trong mảng **đã sắp xếp** | Một trỏ ở đầu, một trỏ ở cuối                      |
| Duyệt chuỗi hoặc subarray                               | Hai con trỏ cùng xuất phát từ đầu (sliding window) |
| So sánh hai danh sách/mảng                              | Hai con trỏ độc lập                                |

---

## 🧪 **Ví dụ đơn giản:**

### Bài toán:

> Cho mảng số nguyên đã sắp xếp tăng dần `arr`, tìm **một cặp** có tổng bằng `target`.

---

### ✍️ Code Python:

```python
def two_sum_sorted(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return (arr[left], arr[right])
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return None

# Test
arr = [1, 2, 4, 7, 11, 15]
target = 15
print(two_sum_sorted(arr, target))  # Output: (4, 11)
```

---

## 📊 **Phân tích:**

- Thời gian: `O(n)` (duyệt một lần từ hai đầu)
- Không dùng vòng lặp lồng nhau
- Điều kiện là **mảng đã sắp xếp**

---
