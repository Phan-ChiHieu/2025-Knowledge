```tsx
{[...(typeof label === 'string' ? [label] : label)].map((label) => (
// JSX cho mỗi label
))}
```

### Giải thích từng phần:

1. typeof label === 'string': Kiểm tra nếu label là chuỗi.
2. ? [label] : label: Nếu là chuỗi, biến nó thành mảng chứa một phần tử ([label]). Nếu không, giữ nguyên (giả sử đã là mảng).
3. [...(...)]: Dùng toán tử spread để tạo một bản sao mảng mới (giúp tránh thay đổi dữ liệu gốc).
4. .map((label) => ( ... )): Lặp qua từng phần tử trong mảng label để render JSX cho mỗi phần tử.

#### Tóm lại:

Đoạn code này giúp bạn có thể truyền vào label là chuỗi hoặc mảng chuỗi, và luôn xử lý nó như một mảng khi render.
