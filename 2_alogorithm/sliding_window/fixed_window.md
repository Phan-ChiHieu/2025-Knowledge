```python
def fixed_window(arr, k):
    window_sum = sum(arr[:k])  # Khởi tạo window đầu tiên
    max_sum = window_sum

    for i in range(k, len(arr)):
        # Slide: bỏ phần tử đầu, thêm phần tử mới
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum
```

### Trace từng bước cụ thể:

```base
Array: [2, 1, 5, 1, 3, 2]
Index:  0  1  2  3  4  5
k = 3
```

### Window ban đầu chúng ta có (i = 0,1,2):

```base
[2, 1, 5, 1, 3, 2]
 ▓▓▓▓▓▓▓▓▓  ←── Window có size 3
 0  1  2
```

### Window tiếp theo chúng ta muốn (i = 1,2,3):

```base
[2, 1, 5, 1, 3, 2]
    ▓▓▓▓▓▓▓▓▓  ←── Window trượt sang phải 1 vị trí
    1  2  3
```

### Khởi tạo:

```base

Array = [2, 1, 5, 1, 3, 2]
window_sum = sum(arr[:3]) = sum([0], [1], [2]) = sum([2, 1, 5]) = 8
max_sum = window_sum = 8

=> Window hiện tại: [2, 1, 5] (index 0-2)
=> Sum = 8
```

### Vòng lặp

```python
for i in range(k, len(arr)):
```

- Vì k=3 nên và độ dài của arr = 6
- for i bắt đầu bằng 3 và kết thúc i < 6

### i = 3:

```python
Muốn window mới: [?, ?, ?] tại index (1,2,3)
                  [1, 5, 1]

Window cũ: [2, 1, 5] tại index (0,1,2)
Window mới: [1, 5, 1] tại index (1,2,3)

# Array: [2, 1, 5, 1, 3, 2]
Cần bỏ: arr[0] = 2  # => arr[i-k] = arr[3-3] = arr[0] = 2 ✓
Cần thêm: arr[3] = 1 # arr[i] = arr[3] = 1

Visualization:
[2, 1, 5, 1, 3, 2]
 ↑  ←--→  ↑
bỏ      thêm

```

### i = 4:

```python
Window cũ: [1, 5, 1] tại index (1,2,3)
Window mới: [5, 1, 3] tại index (2,3,4)


# Array: [2, 1, 5, 1, 3, 2]
Cần bỏ: arr[1] = 1 # => arr[i-k] = arr[4-3] = arr[1] = 1 ✓
Cần thêm: arr[4] = 3 # # arr[i] = arr[4] = 3

Visualization:
[2, 1, 5, 1, 3, 2]
    ↑  ←--→  ↑
    bỏ      thêm
```

### i = 5:

```python
Window cũ: [5, 1, 3] tại index (2,3,4)
Window mới: [1, 3, 2] tại index (3,4,5)


# Array: [2, 1, 5, 1, 3, 2]
Cần bỏ: arr[2] = 5 # => arr[i-k] = arr[5-3] = arr[2] = 5 ✓
Cần thêm: arr[5] = 2 # arr[i] = arr[5] = 2


Visualization:
[2, 1, 5, 1, 3, 2]
       ↑  ←--→  ↑
       bỏ      thêm
```

### Chúng ta có thể hình dung sliding window như này:

```python
i=3: Chúng ta thêm arr[3], bỏ arr[3-3]=arr[0]
[2, 1, 5, 1, 3, 2]
 ↑removed ↑added

i=4: Chúng ta thêm arr[4], bỏ arr[4-3]=arr[1]
[2, 1, 5, 1, 3, 2]
    ↑removed ↑added

i=5: Chúng ta thêm arr[5], bỏ arr[5-3]=arr[2]
[2, 1, 5, 1, 3, 2]
       ↑removed ↑added
```

### Cách chúng ta nhớ đơn giản:

- **"Khi chúng ta thêm phần tử thứ i, chúng ta bỏ phần tử cách đó k vị trí"**

  - Chúng ta thêm arr[i]
  - Chúng ta bỏ arr[i-k] (cách k vị trí về phía trước)

- **Tại sao lại k vị trí?**
  - Vì window có kích thước **k**, nên khi chúng ta thêm 1 phần tử mới, chúng ta phải bỏ 1 phần tử cũ ở đầu **để giữ nguyên kích thước.**
