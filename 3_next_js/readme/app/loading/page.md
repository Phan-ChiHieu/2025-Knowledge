Phần `await connection();` trong đoạn code của bạn là **để buộc Next.js xử lý request như một request động (dynamic request)**, thay vì prerender tại build time.

---

### 🔍 Giải thích chi tiết:

Trong Next.js, khi một route **không sử dụng dữ liệu dynamic** (không gọi API, không fetch data từ request), thì **mặc định sẽ được prerender sẵn (SSG)** trong quá trình `next build`.

> ✅ Điều này có lợi vì tốc độ rất nhanh (HTML sẵn sàng), nhưng điểm yếu là **không có loading state** (vì trang hiển thị ngay lập tức).

---

### `await connection();` làm gì?

```ts
import { connection } from "next/server";
```

- Hàm `connection()` đến từ Next.js App Router (`next/server`).
- Nó **yêu cầu truy cập vào `Request` object** → Điều này khiến Next hiểu rằng: _"Trang này phụ thuộc vào request, không thể prerender trước"_.
  \=> Kết quả là trang sẽ được render như **SSR hoặc ISR**, không còn là SSG nữa.

---

### ⚠️ Lưu ý

Ngoài ra, bạn còn có đoạn này:

```ts
await new Promise((resolve) => setTimeout(resolve, 1000));
```

→ Thêm delay để **demo loading state** khi dữ liệu đang được tải (ví dụ như từ DB hoặc API).

---

### 🧠 Tổng kết

| Mục đích               | Giải pháp                                       |
| ---------------------- | ----------------------------------------------- |
| Bỏ chế độ SSG          | Dùng `await connection()`                       |
| Giả lập độ trễ loading | `await new Promise(...setTimeout...)`           |
| Kết quả                | Cho phép Next.js xử lý SSR + hiện loading state |

---
