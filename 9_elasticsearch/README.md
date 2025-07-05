# Setup môi trường chạy code

Để tạo môi trường `.venv` và cài đặt các thư viện từ `requirements.txt`, làm theo các bước sau:

---

### **1. Tạo môi trường ảo**

```bash
python -m venv .venv
```

> ⚠️ Đảm bảo bạn đang dùng đúng version Python (Python 3.x)

---

### **2. Kích hoạt môi trường ảo**

- **Trên macOS / Linux:**

```bash
source .venv/bin/activate
```

- **Trên Windows (cmd):**

```cmd
.venv\Scripts\activate.bat
```

- **Trên Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

---

### **3. Cài đặt thư viện từ `requirements.txt`**

```bash
pip install -r requirements.txt
```

---

### **4. Kiểm tra thư viện đã cài (tuỳ chọn)**

```bash
pip list
```

---

### **5. (Tuỳ chọn) Đóng băng thư viện lại**

Sau khi cài thêm lib mới:

```bash
pip freeze > requirements.txt
```

`pip install -r requirements.txt` cài hàng loạt package vào môi trường Python hiện tại. Để **gỡ toàn bộ các package đã cài**, có vài cách tùy theo mức độ **"clean"** bạn muốn:

---

## ✅ **1. Gỡ từng package trong `requirements.txt`**

```bash
pip uninstall -r requirements.txt -y
```

- Tham số `-y`: auto confirm, không cần gõ `y` từng package.
- Áp dụng khi bạn chỉ muốn **gỡ đúng những gì file `requirements.txt` đã cài**.

---

## 🔁 **2. Reset sạch môi trường (khuyến nghị)**

### 👉 Xoá toàn bộ `.venv`:

```bash
rm -rf .venv
```

Sau đó:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

> Cách này **chắc chắn sạch sẽ nhất**, tránh bị lỗi do dependency cũ còn sót lại.

---

## 🧪 **3. Gỡ tất cả package hiện tại trong môi trường (nguy hiểm hơn)**

Không khuyến khích nếu bạn có những package cài thủ công không nằm trong `requirements.txt`.

```bash
pip freeze | xargs pip uninstall -y
```

---

## Kết luận

- Gỡ đúng những gì `requirements.txt` cài:
  → `pip uninstall -r requirements.txt -y`
- Làm sạch toàn bộ môi trường nhanh, gọn, sạch:
  → `rm -rf .venv && python3 -m venv .venv`

---

---

Dưới đây là **hướng dẫn chi tiết cách add `.venv` vào VSCode để dùng làm Python Interpreter** (cho cả macOS):

---

## ✅ **Bước 1: Chọn Python Interpreter**

Trong VSCode:

1. Mở Command Palette: `Cmd (⌘) + Shift + P`
2. Gõ: `Python: Select Interpreter` → Enter
3. Nếu thấy `.venv/bin/python` trong danh sách → chọn nó

---

## ✅ **Bước 2: Nếu không thấy `.venv/bin/python` trong danh sách?**

### Cách thủ công:

1. Trong Command Palette: `Python: Select Interpreter`
2. Chọn **"Enter interpreter path..."** → rồi chọn **"Find..."**
3. Dẫn đến file:

   ```bash
   /Users/yourname/your-project/.venv/bin/python
   ```

4. Chọn file đó → Done

---
