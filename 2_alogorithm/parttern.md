# Điều kiện nhận biết Prefix Sum:

Tuyệt! **Prefix Sum** là một kỹ thuật rất quan trọng và hay xuất hiện trong phỏng vấn.

## **Điều kiện nhận biết Prefix Sum:**

### **1. Từ khóa chính:**

- **"Sum of subarray"** - tổng của mảng con
- **"Range sum query"** - truy vấn tổng trong khoảng
- **"Continuous subarray"** - mảng con liên tiếp
- **"Subarray with sum equals K"** - mảng con có tổng bằng K

### **2. Mô tả bài toán điển hình:**

- Tính tổng các phần tử từ index `i` đến `j`
- Đếm số mảng con có tổng = target
- Tìm mảng con dài nhất có tổng = K
- Multiple queries về tổng trong khoảng

### **3. Tín hiệu mạnh:**

- **Nhiều truy vấn** (queries) về cùng một mảng
- Cần tính tổng **nhiều lần** trên các đoạn khác nhau
- **O(1)** cho mỗi query về range sum
- Bài toán về **cumulative sum**

### **4. Ví dụ bài toán thường gặp:**

```
"Given an array, answer Q queries. Each query asks for
sum of elements from index L to R"
```

```
"Find number of subarrays with sum equals to K"
```

```
"Given array of 0s and 1s, find longest subarray
with equal number of 0s and 1s"
```

### **5. Biến thể nâng cao:**

- **Prefix Sum + HashMap**: đếm subarray sum = K
- **2D Prefix Sum**: ma trận 2D
- **Prefix XOR**: thay sum bằng XOR
- **Difference Array**: cập nhật range

### **6. Độ phức tạp đặc trưng:**

- **Preprocessing**: O(n)
- **Query**: O(1)
- **Total**: O(n + q) với q là số queries

---
