---

### 🌟 Prefix Sum là gì?

**Prefix Sum** giống như một cách để “tính trước” tổng các số từ đầu danh sách đến từng vị trí, để sau này nếu ai đó hỏi “Từ đây đến đây tổng là bao nhiêu?”, mình có thể trả lời thật nhanh!

---

### 📚 Ví dụ dễ hiểu

Giả sử bạn có một dãy số:

```
nums = [1, 2, 3, 4, 5, 6]
```

Bạn muốn biết:
**Tổng các số từ vị trí số 1 đến số 3 là bao nhiêu?** (Tức là: `2 + 3 + 4 = 9`)

---

### 🔍 Cách làm thông minh hơn với Prefix Sum

Thay vì cộng từng số mỗi lần (rất chậm nếu có nhiều câu hỏi), bạn **tính trước một dãy mới**, gọi là **prefix sum array** như sau:

```
prefix = [1, 3, 6, 10, 15, 21]
```

Cách tính:

- Vị trí 0: 1
- Vị trí 1: 1 + 2 = 3
- Vị trí 2: 1 + 2 + 3 = 6
- Vị trí 3: 1 + 2 + 3 + 4 = 10
- Vị trí 4: 1 + 2 + 3 + 4 + 5 = 15
- Vị trí 5: 1 + 2 + 3 + 4 + 5 + 6 = 21

---

### 💡 Giờ thì trả lời câu hỏi cực nhanh

Muốn biết tổng từ **vị trí 1 đến vị trí 3** (2 + 3 + 4), dùng công thức:

```
prefix[3] - prefix[0] = 10 - 1 = 9
```

\==> **Kết quả: 9**

---

### ✅ Khi nào nên dùng cách này?

Khi bạn cần:

- Tính tổng giữa nhiều đoạn trong dãy số (rất nhiều lần),
- Và bạn muốn làm điều đó **nhanh** và **hiệu quả**.

---

---

---

# Range Sum Query - Immutable

```base
Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
```

## ✅ **Yêu cầu bài toán**

Thiết kế một lớp `NumArray` với:

- **Constructor** nhận một mảng số nguyên.
- Một phương thức **`sumRange(i, j)`** trả về tổng từ chỉ số `i` đến `j` trong mảng.

---

## 🧠 **Ý tưởng giải bằng Prefix Sum**

- Tính trước một mảng `prefix` sao cho:

  ```python
  prefix[i] = tổng từ nums[0] đến nums[i]
  ```

- Sau đó:

  ```python
  sumRange(i, j) = prefix[j] - prefix[i - 1]  (nếu i > 0)
                 = prefix[j]                 (nếu i == 0)
  ```

---

## 🐍 **Code Python hoàn chỉnh**

```python
class NumArray:
    def __init__(self, nums):
        self.prefix = [0] * len(nums)
        if nums:
            self.prefix[0] = nums[0]
            for i in range(1, len(nums)):
                self.prefix[i] = self.prefix[i - 1] + nums[i]

    def sumRange(self, i, j):
        if i == 0:
            return self.prefix[j]
        return self.prefix[j] - self.prefix[i - 1]


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

print("Output:", result)
```

---

## ✅ **Kết quả**

Chạy chương trình sẽ in:

```
Output: [None, 1, -1, -3]
```

\==> Đúng như yêu cầu bài toán!

---

---

---

---

## 🔁 **Câu lệnh `for i in range(...)` là gì?**

- Dùng để **lặp lại** một đoạn mã nhiều lần với giá trị `i` thay đổi trong khoảng nhất định.
- `range(start, stop, step)` tạo ra một dãy số từ `start` đến nhỏ hơn `stop`, cách nhau `step`.

---

## 🔍 **Cách dùng phổ biến**

### 1. `for i in range(n)`: lặp từ 0 đến n-1

```python
for i in range(5):
    print(i)
```

➡️ Kết quả:

```
0
1
2
3
4
```

---

### 2. `for i in range(start, stop)`: lặp từ start đến stop - 1

```python
for i in range(2, 6):
    print(i)
```

➡️ Kết quả:

```
2
3
4
5
```

---

### 3. `for i in range(start, stop, step)`: lặp theo bước nhảy `step`

```python
for i in range(1, 10, 2):
    print(i)
```

➡️ Kết quả:

```
1
3
5
7
9
```

---

## 🧠 Trong bài `prefix sum`, chúng ta dùng:

```python
for i in range(1, len(nums)):
    prefix[i] = prefix[i - 1] + nums[i]
```

### 👉 Điều này nghĩa là:

- Bắt đầu từ `i = 1` (vì `prefix[0]` đã được gán trước).
- Ở mỗi bước, `prefix[i]` = tổng dồn từ đầu đến `i`.

---

## ✅ Khi nào dùng `for in range`?

| Mục đích               | Cách dùng                    |
| ---------------------- | ---------------------------- |
| Lặp qua chỉ số (index) | `for i in range(len(array))` |
| Lặp n lần              | `for i in range(n)`          |
| Lặp có bước nhảy       | `for i in range(0, 10, 2)`   |
| Đếm ngược              | `for i in range(10, 0, -1)`  |

---

---

---

# 525. Contiguous Array

## 🧠 HashMap là gì?

Trong Python, hashmap chính là **dictionary (`dict`)**.
Nó lưu **cặp `key: value`**, cho phép **tra cứu nhanh (O(1))**.

### 📦 Ví dụ cơ bản:

```python
my_map = {}
my_map['apple'] = 5
my_map['banana'] = 2

print(my_map['apple'])  # Output: 5
```

---

## 📌 Áp dụng vào bài toán:

Ta cần một hashmap như sau:

```python
sum_to_index = {}
```

- **Key**: `prefix_sum` tại thời điểm nào đó
- **Value**: Chỉ số `index` đầu tiên mà `prefix_sum` đó xuất hiện

---

### ✅ Ví dụ đơn giản:

Giả sử:

```python
nums = [0, 1, 0]
# Đổi 0 -> -1 → [-1, 1, -1]
# Prefix_sum: [-1, 0, -1]
```

Bước duyệt qua từng phần tử, ta làm:

```python
sum_to_index = {0: -1}  # mặc định: tổng 0 xảy ra trước khi bắt đầu

total = 0

for i in range(len(nums)):
    total += 1 if nums[i] == 1 else -1
    if total in sum_to_index:
        print(f"Tìm thấy prefix_sum = {total} lần 2 tại index {i}, trước đó tại index {sum_to_index[total]}")
    else:
        sum_to_index[total] = i
        print(f"Thêm mới: prefix_sum = {total} tại index {i}")
```

---

## 🧪 Kết quả console:

```
Thêm mới: prefix_sum = -1 tại index 0
Tìm thấy prefix_sum = 0 lần 2 tại index 1, trước đó tại index -1
Tìm thấy prefix_sum = -1 lần 2 tại index 2, trước đó tại index 0
```

---

## ✅ Kết luận:

Hashmap giúp ta:

- **Ghi nhớ lần đầu** một tổng xuất hiện
- Khi gặp lại tổng đó → **xác định đoạn cân bằng nhanh**

---

---

## ✅ `enumerate(nums)` là gì?

`enumerate(iterable)` là một hàm **trả về cặp (index, value)** khi duyệt qua một danh sách (hoặc iterable nói chung).

### Ví dụ:

```python
nums = [10, 20, 30]
for i, val in enumerate(nums):
    print(i, val)
```

✅ Output:

```
0 10
1 20
2 30
```

---

## 🆚 So sánh với `range(len(nums))`

### Ví dụ dùng `range`:

```python
nums = [10, 20, 30]
for i in range(len(nums)):
    val = nums[i]
    print(i, val)
```

✅ Output: giống hệt

---

## 🔍 So sánh nhanh:

| Đặc điểm                      | `enumerate(nums)`                 | `range(len(nums))`                   |
| ----------------------------- | --------------------------------- | ------------------------------------ |
| Cú pháp ngắn gọn              | ✅ Có                             | ❌ Phải truy cập lại `nums[i]`       |
| Truy cập index + value        | ✅ Trực tiếp qua `i, val`         | ✅ Nhưng cần `val = nums[i]`         |
| Dễ đọc                        | ✅ Rõ ràng hơn                    | ❌ Lằng nhằng hơn với `nums[i]`      |
| Dùng được với bất kỳ iterable | ✅ (string, tuple, generator,...) | ❌ Chỉ dùng với list hoặc có `len()` |

---

## ✅ Kết luận:

> Dùng `enumerate(nums)` khi bạn cần **cả index lẫn giá trị** — rõ ràng, ngắn gọn, Pythonic hơn ✅

---

---

## 🎯 **Mục tiêu bài toán**:

Tìm **độ dài lớn nhất của đoạn con liên tiếp** trong mảng nhị phân `nums` sao cho **số lượng `0` và `1` bằng nhau**.

---

## 🔄 Ý tưởng chính:

Chuyển bài toán đếm `0` và `1` thành bài toán về **prefix sum**:

- Gán:

  - `0 → -1` (coi như trừ 1)
  - `1 → +1`

→ Khi nào tổng từ đầu đến vị trí `i` quay lại bằng tổng đã gặp trước đó (cùng một `count`), tức là từ đoạn `j+1` đến `i` có tổng = 0 → số lượng `0 == 1`

---

## 🧠 Biến chính:

- `count`: tổng tích lũy (prefix sum) sau khi thay `0 → -1`
- `max_len`: kết quả trả về – độ dài đoạn con dài nhất thỏa yêu cầu
- `sum_to_index`: dict lưu **vị trí đầu tiên** gặp một `count` nào đó
  → `{count: first_index}`
  → Nếu gặp lại `count` đó, đoạn từ `first_index + 1` đến `i` là đoạn cân bằng.

---

## 🔍 Phân tích từng dòng code:

```python
count = 0
max_len = 0
sum_to_index = {0: -1}
```

- Khởi tạo:

  - `count = 0`: tổng tích lũy ban đầu
  - `max_len = 0`: kết quả khởi đầu
  - `{0: -1}`: giúp handle đúng đoạn bắt đầu từ index 0

---

```python
for i, num in enumerate(nums):
    count += 1 if num == 1 else -1
```

- Duyệt từng phần tử `nums`, tăng/giảm `count`:

  - Nếu gặp `1`: tăng count
  - Nếu gặp `0`: giảm count

---

```python
    if count in sum_to_index:
        max_len = max(max_len, i - sum_to_index[count])
```

- Nếu `count` **đã xuất hiện trước đó**, tức là tổng từ `first_index + 1` đến `i` bằng 0 → đoạn cân bằng
- Tính độ dài đoạn này: `i - first_index`
- Cập nhật `max_len` nếu lớn hơn

---

```python
    else:
        sum_to_index[count] = i
```

- Nếu đây là **lần đầu gặp count này**, lưu lại index hiện tại vào `sum_to_index`

---

```python
return max_len
```

- Trả về độ dài lớn nhất của đoạn con thỏa điều kiện

---

## 🔁 Ví dụ nhỏ minh họa:

```python
nums = [0, 1, 0, 1]
→ Sau chuyển đổi: [-1, +1, -1, +1]
→ Prefix sum: [-1, 0, -1, 0]
```

| i   | num | count | sum_to_index   | max_len |
| --- | --- | ----- | -------------- | ------- |
| 0   | 0   | -1    | {0: -1, -1: 0} | 0       |
| 1   | 1   | 0     | `0 đã có ở -1` | 2       |
| 2   | 0   | -1    | `-1 đã có ở 0` | 2       |
| 3   | 1   | 0     | `0 đã có ở -1` | 4 ✅    |

---

## 🧠 Tổng kết:

- ✅ **Thời gian (Time Complexity):** `O(n)`
- ✅ **Không cần 2 vòng for, rất tối ưu**
- ✅ **Không dùng nhiều bộ nhớ: Space O(n)**

---

```python
nums = [0,1,1,1,1,1,0,0,0]
# same = [-1,1,1,1,1,1,-1,-1,-1]
→ prefix = [-1,0,1,2,3,4,3,2,1]
```

| index | num | sum | sum_to_index                       | max_len |
| ----- | --- | --- | ---------------------------------- | ------- |
| 0     | 0   | -1  | {0: -1, -1: 0}                     | 0       |
| 1     | 1   | 0   | `0 đã có ở -1`                     | 2       |
| 2     | 1   | 1   | {0: -1, -1: 0, 1:2}                |         |
| 3     | 1   | 2   | {0: -1, -1: 0, 1:2, 2:3}           |         |
| 4     | 1   | 3   | {0: -1, -1: 0, 1:2, 2:3, 3:4}      |         |
| 5     | 1   | 4   | {0: -1, -1: 0, 1:2, 2:3, 3:4, 4:5} |         |
| 6     | 0   | 3   | `3 đã có ở 4`                      | 2       |
| 7     | 0   | 2   | `2 đã có ở 3`                      | 4       |
| 8     | 0   | 1   | `1 đã có ở 2`                      | 6       |
