Đoạn code này là một **Next.js App Router dynamic route page** được định nghĩa ở file `app/[section]/page.tsx`. Mục tiêu của trang là **hiển thị danh sách sản phẩm thuộc một `section` cụ thể**, ví dụ như `/electronics`, `/clothing`, v.v.

---

## 🎯 Mục tiêu tổng quan

- Route: `app/[section]/page.tsx`
- Dữ liệu:

  - `section`: một danh mục cụ thể (theo `slug`)
  - `product`: các sản phẩm thuộc danh mục đó

- Xử lý:

  - Validate `section` từ URL
  - Nếu không tồn tại → `notFound()`
  - Nếu có → render danh sách sản phẩm thuộc section

---

## 🔍 Phân tích từng phần

---

### 1. `'use cache';` (Top of file directive)

- Cho phép **React Cache** hoạt động (Next.js hỗ trợ mặc định).
- Các hàm async như `generateStaticParams` có thể **dùng cache** để tối ưu SSG/ISR.
- Dùng tốt khi data không thay đổi quá thường xuyên.

---

### 2. `generateStaticParams()`

```ts
export async function generateStaticParams() {
  const sections = db.section.findMany();
  return sections.map(({ slug }) => ({ section: slug }));
}
```

- Next.js sẽ gọi hàm này tại **build time** để **generate các route tĩnh** theo từng `section`.
- Trả về mảng `{ section: slug }`, ví dụ:

  ```ts
  [{ section: "electronics" }, { section: "toys" }, { section: "furniture" }];
  ```

- Tạo sẵn static page cho `/electronics`, `/toys`, ...

➡️ Đây là phần quan trọng trong **Static Site Generation (SSG)**.

---

### 3. `Page` Component

```ts
export default async function Page({ params }: { params: Promise<{ section: string }> }) {
  const { section: sectionSlug } = await params;
```

- Nhận `params` là một `Promise` chứa `{ section: string }`

  - Đây là behavior của App Router với `generateStaticParams` + async route.

- Gọi `await` để lấy `sectionSlug` thực tế.

---

### 4. Tìm section theo slug

```ts
const section = db.section.find({ where: { slug: sectionSlug } });
if (!section) {
  notFound();
}
```

- Kiểm tra xem `sectionSlug` có tồn tại trong DB không.
- Nếu không → gọi `notFound()` của Next.js → chuyển sang `404` page.

---

### 5. Lấy danh sách sản phẩm

```ts
const products = db.product.findMany({ where: { section: section.id } });
```

- Truy vấn các sản phẩm thuộc `section.id`.

---

### 6. Render UI

```tsx
<Boundary label="[section]/page.tsx">
  <div className="flex flex-col gap-4">
    <h1 className="text-xl font-semibold text-gray-300">
      All <span className="font-mono tracking-tighter text-gray-600">({products.length})</span>
    </h1>

    <div className="grid grid-cols-1 gap-6 lg:grid-cols-3">
      {products.map((product) => (
        <ProductCard key={product.id} product={product} />
      ))}
    </div>
  </div>
</Boundary>
```

- `Boundary`: một UI wrapper (có thể dùng để hiển thị lỗi, label vùng)
- Tiêu đề hiển thị tổng số sản phẩm.
- Render danh sách `ProductCard` theo dạng grid.

---

## ✅ Tổng quan luồng hoạt động

```text
User truy cập /[section] →
↓
Next gọi generateStaticParams() để tạo route tĩnh →
↓
Page component nhận section slug từ URL →
↓
Kiểm tra section có tồn tại không →
→ Nếu không → notFound()
→ Nếu có → lấy danh sách sản phẩm →
↓
Render danh sách sản phẩm trong UI
```

---

## 🔧 Ghi chú kỹ thuật

| Chi tiết                   | Ghi chú                                            |
| -------------------------- | -------------------------------------------------- |
| `generateStaticParams()`   | Kích hoạt SSG theo dynamic segment                 |
| `notFound()`               | Redirect sang trang 404                            |
| `params` là `Promise<...>` | Vì App Router dùng async/streaming                 |
| `'use cache'`              | Cho phép dữ liệu được cache lại ở level React/Next |
| `Boundary`                 | Có thể là UI wrapper cho Suspense/Error            |

---

---

ISR (**Incremental Static Regeneration**) là một cơ chế trong **Next.js** cho phép bạn:

> ⚡ **Kết hợp ưu điểm của SSG (hiệu năng cao)** và **cập nhật dữ liệu mới mà không cần rebuild toàn bộ site.**

---

## 🧠 Nói ngắn gọn:

- **SSG**: Tạo file HTML tĩnh **một lần khi build**, không đổi.
- **ISR**: Vẫn tạo file HTML tĩnh, **nhưng có thể regenerate sau X giây**, để cập nhật dữ liệu mới.
- **CSR/SSR**: Render động mỗi lần request, chậm hơn, nhưng luôn mới.

---

## 🔁 Ví dụ dễ hiểu:

Giả sử bạn có trang `/blog/hello-world` dùng `getStaticProps`:

```tsx
export async function getStaticProps() {
  const post = await getBlogPost("hello-world");
  return {
    props: { post },
    revalidate: 60, // ISR: regenerate sau mỗi 60 giây
  };
}
```

### Lúc đầu:

- Trang `/blog/hello-world` được tạo sẵn lúc build → siêu nhanh ⚡

### Sau đó 60s:

- Request tiếp theo → **Next.js sẽ ngầm regenerate HTML mới**
- Trong khi đó, người dùng vẫn thấy phiên bản cũ (không bị chặn)

➡️ Sau khi build lại xong, các request tiếp theo sẽ thấy **bản mới**.

---

## ⚙️ ISR hoạt động thế nào?

| Giai đoạn                | Mô tả                                                                        |
| ------------------------ | ---------------------------------------------------------------------------- |
| Build time               | Trang được tạo tĩnh lần đầu (giống SSG)                                      |
| Người dùng truy cập      | HTML cũ vẫn phục vụ ngay lập tức (cache)                                     |
| Đến thời điểm revalidate | Request đầu tiên sau thời gian `revalidate` sẽ kích hoạt quá trình **regen** |
| Sau khi regen xong       | HTML mới thay thế bản cũ, người dùng sau đó sẽ thấy nội dung cập nhật        |

---

## 🧪 Khi nào dùng ISR?

| Tình huống                                                    | Dùng ISR?         |
| ------------------------------------------------------------- | ----------------- |
| Trang có nội dung ít thay đổi, nhưng vẫn cần cập nhật định kỳ | ✅                |
| Trang phải luôn luôn mới nhất (real-time)                     | ❌ (dùng SSR/CSR) |
| Trang có dữ liệu gần như không đổi (docs, landing...)         | ❌ (dùng SSG)     |

---

## ✅ Ưu điểm ISR

- Tốc độ gần như SSG (HTML tĩnh)
- Không cần rebuild toàn bộ site
- Có thể cập nhật theo chu kỳ (ví dụ 60s)

---

## 🧨 Cần lưu ý gì?

1. **Chỉ hoạt động nếu đang deploy trên hosting hỗ trợ ISR**
   (Vercel, Netlify, hoặc Next.js Server Mode đầy đủ)

2. **Cẩn thận cache**: Nếu có CDN hoặc proxy, phải cấu hình đúng để không cache sai phiên bản.

3. **Không dùng ISR cho nội dung cực kỳ dynamic**
   Vì vẫn có độ trễ giữa lúc nội dung thay đổi và lúc regenerate xong.

---

✅ Tóm tắt khi dùng ISR

| Trang              | Dùng ISR? | Thời gian revalidate |
| ------------------ | --------- | -------------------- |
| Trang sản phẩm     | ✅ Có     | 5–30 phút            |
| Trang blog         | ✅ Có     | 1–12 giờ             |
| Trang danh mục     | ✅ Có     | 10–60 phút           |
| Trang tin tức      | ✅ Có     | 1–5 phút             |
| Trang user/profile | ❌ Không  | –                    |
| Trang admin/panel  | ❌ Không  | –                    |

---

# Đọc thêm ở document: [incremental-static-regeneration](https://nextjs.org/docs/app/guides/incremental-static-regeneration)
