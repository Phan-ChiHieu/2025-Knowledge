Hiểu đơn giản:

- **Agile** là _tư duy/phương pháp luận_ để phát triển phần mềm một cách linh hoạt, thích ứng nhanh với thay đổi.
- **Scrum** là một **framework (khuôn mẫu)** cụ thể để thực hiện Agile.

---

## 1. **Agile là gì?**

Agile là một **triết lý phát triển phần mềm linh hoạt**, được giới thiệu trong **Agile Manifesto** (2001), với 4 giá trị cốt lõi:

| Trọng Agile                 | Ít quan trọng hơn                |
| --------------------------- | -------------------------------- |
| Cá nhân & tương tác         | Hơn là quy trình & công cụ       |
| Phần mềm chạy được          | Hơn là tài liệu đầy đủ           |
| Cộng tác với khách hàng     | Hơn là đàm phán hợp đồng         |
| Phản hồi nhanh với thay đổi | Hơn là làm theo kế hoạch cố định |

### Agile hướng đến:

- Chia nhỏ công việc, làm theo từng đợt ngắn (iteration)
- Release nhanh, lấy phản hồi sớm từ khách hàng
- Liên tục cải tiến (continuous improvement)

---

## 2. **Scrum là gì?**

Scrum là một **framework Agile** giúp team tổ chức công việc trong các vòng lặp ngắn gọi là **Sprint** (thường 1–2 tuần).

### Cấu trúc của Scrum:

#### 🧑‍🤝‍🧑 **Vai trò**

- **Product Owner (PO)**: Người đại diện khách hàng, quyết định thứ tự ưu tiên
- **Scrum Master**: Đảm bảo Scrum diễn ra đúng, gỡ rối cho team
- **Development Team**: Dev, QA, Designer – người trực tiếp làm sản phẩm

#### 🔁 **Sự kiện**

1. **Sprint Planning**: Lên kế hoạch cho sprint
2. **Daily Scrum**: Họp nhanh 15 phút mỗi sáng
3. **Sprint Review**: Demo sản phẩm cho PO, lấy phản hồi
4. **Sprint Retrospective**: Nhìn lại quá trình, cải tiến

#### 📋 **Artifacts (Tài liệu)**

- **Product Backlog**: Danh sách việc cần làm (PO quản lý)
- **Sprint Backlog**: Việc sẽ làm trong sprint
- **Increment**: Bản build chạy được sau mỗi sprint

---

## Tóm tắt:

| Agile                                                | Scrum                            |
| ---------------------------------------------------- | -------------------------------- |
| Tư duy / phương pháp                                 | Framework cụ thể của Agile       |
| Không có quy trình cố định                           | Có quy trình rõ ràng theo Sprint |
| Có nhiều framework theo Agile (Scrum, Kanban, XP...) | Scrum là một trong số đó         |

---

---

Hiểu rồi. Bạn đang hỏi về **các quy trình làm việc (workflow/process) theo mô hình quản lý dự án trong công ty công nghệ**, như **Scrum, Kanban, Waterfall**, v.v. Dưới đây là **tổng quan các mô hình phổ biến nhất**, cùng ưu nhược điểm của từng cái:

---

### 1. **Scrum** – Agile-based (phổ biến nhất hiện nay)

**Đặc điểm:**

- Làm việc theo **Sprint** (thường 1–2 tuần)
- Team tự quản, daily stand-up, planning, retro
- Mỗi sprint có backlog rõ ràng → commit xong là không đổi giữa chừng

**Vai trò:**

- Product Owner: định hướng tính năng, ưu tiên backlog
- Scrum Master: người bảo vệ team, loại bỏ cản trở
- Dev team: tự tổ chức làm việc

**Ưu điểm:**

- Phù hợp với sản phẩm thay đổi liên tục
- Có thể release nhanh, validate thị trường

**Nhược điểm:**

- Cần team kỷ luật và hiểu phương pháp
- Dễ fake Scrum (gọi là ScrumBut)

---

### 2. **Kanban**

**Đặc điểm:**

- Không sprint, **luồng công việc liên tục**
- Sử dụng **Kanban board**: To Do → In Progress → Review → Done
- Giới hạn số task đang làm (WIP limit)

**Ưu điểm:**

- Linh hoạt, đơn giản để triển khai
- Phù hợp cho team support, vận hành, devops

**Nhược điểm:**

- Dễ bị backlog quá tải nếu không kiểm soát
- Không có deadline rõ ràng nếu không quản tốt

---

### 3. **Waterfall (Thác đổ)** – truyền thống

**Đặc điểm:**

- Làm tuần tự: Requirement → Design → Dev → Test → Deploy
- Không có sự quay lại hoặc lặp lại giai đoạn

**Ưu điểm:**

- Dễ kiểm soát, rõ ràng từ đầu
- Phù hợp với dự án có yêu cầu ổn định, cố định

**Nhược điểm:**

- Không linh hoạt nếu yêu cầu thay đổi
- Deliver lâu (phải xong hết mới release được)

---

### 4. **XP (Extreme Programming)**

**Đặc điểm:**

- Rất kỹ tính về **code quality, testing, pairing**
- Test-driven development (TDD), CI, code review nghiêm ngặt

**Ưu điểm:**

- Code chất lượng cao, giảm bug
- Phù hợp với team kỹ thuật mạnh

**Nhược điểm:**

- Yêu cầu rất cao về kỷ luật kỹ thuật
- Khó áp dụng cho team junior

---

### 5. **Scrumban** – kết hợp Scrum và Kanban

**Đặc điểm:**

- Có Sprint planning (Scrum) + Kanban board
- Phù hợp với team cần linh hoạt nhưng vẫn có nhịp release

**Ưu điểm:**

- Giữ được tính tổ chức (Scrum) + sự linh hoạt (Kanban)

---

### Nên chọn mô hình nào?

| Mô hình       | Phù hợp với loại dự án nào?                          |
| ------------- | ---------------------------------------------------- |
| **Scrum**     | Dự án phát triển sản phẩm dài hạn, thay đổi liên tục |
| **Kanban**    | Team support, devops, vận hành                       |
| **Waterfall** | Dự án outsource, fixed scope & budget                |
| **XP**        | Sản phẩm yêu cầu cực cao về code quality             |
| **Scrumban**  | Team chuyển từ Scrum sang Kanban hoặc ngược lại      |

---

---
