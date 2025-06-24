Trong script `package.json`, câu lệnh:

```json
{
  "scripts": {
    "prettier": "prettier --write --ignore-unknown ."
  }
}
```

## Giải thích từng phần:

### `prettier`

- Command chính để chạy Prettier formatter

### `--write`

- **Tác dụng**: Ghi đè trực tiếp vào file gốc thay vì chỉ hiển thị kết quả
- **Không có flag này**: Prettier chỉ show preview, không thay đổi file
- **Có flag này**: Prettier sẽ format và lưu luôn vào file

### `--ignore-unknown`

- **Tác dụng**: Bỏ qua các file có extension mà Prettier không hỗ trợ
- **Không có flag này**: Prettier sẽ báo lỗi khi gặp file không support (như .pdf, .jpg)
- **Có flag này**: Prettier im lặng skip qua những file đó

### `.` (dấu chấm)

- **Tác dụng**: Target toàn bộ thư mục hiện tại và tất cả subfolder
- **Tương đương**: Format tất cả file được support trong project

## Cách sử dụng:

```bash
# Chạy script
npm run prettier

# Hoặc trực tiếp
npx prettier --write --ignore-unknown .
```

## Các biến thể phổ biến khác:

```json
{
  "scripts": {
    // Format tất cả
    "format": "prettier --write --ignore-unknown .",

    // Chỉ check, không ghi file
    "format:check": "prettier --check --ignore-unknown .",

    // Format specific folders
    "format:src": "prettier --write src/**/*.{js,jsx,ts,tsx,json,css,md}",

    // Format và show các file đã thay đổi
    "format:list": "prettier --write --ignore-unknown . --list-different"
  }
}
```

---

---

Đây là config Prettier rất tốt cho Next.js! Hãy giải thích từng option:

## Phân tích prettier.config.js của bạn:

### `arrowParens: "always"`

```javascript
// Output: luôn có dấu ngoặc
const func = (x) => x * 2;

// Thay vì:
const func = (x) => x * 2;
```

### `semi: true`

```javascript
// Output: luôn có dấu chấm phẩy
const name = "John";
console.log(name);
```

### `trailingComma: "all"`

```javascript
// Output: comma ở cuối mọi nơi có thể
const obj = {
  name: "John",
  age: 30, // ← comma này
};

const arr = [
  "item1",
  "item2", // ← comma này
];
```

### `singleQuote: true`

```javascript
// Output: dùng single quote
const message = "Hello world";

// Thay vì:
const message = "Hello world";
```

### `objectWrap: "collapse"`

⚠️ **Lưu ý**: Option này không tồn tại trong Prettier! Có thể bạn muốn dùng:

- `bracketSpacing: true/false`
- `bracketSameLine: true/false`

### `plugins: ["prettier-plugin-tailwindcss"]`

- **Rất quan trọng**: Sắp xếp class Tailwind theo thứ tự chuẩn
- **Cần cài**: `npm install -D prettier-plugin-tailwindcss`

## Config được sửa lại:

```javascript
// prettier.config.js
module.exports = {
  arrowParens: "always",
  semi: true,
  trailingComma: "all",
  singleQuote: true,

  // Thay objectWrap bằng:
  bracketSpacing: true, // { foo: bar } thay vì {foo: bar}
  bracketSameLine: false, // > xuống dòng trong JSX

  // Thêm các option hữu ích cho Next.js:
  tabWidth: 2,
  printWidth: 80,
  useTabs: false,

  // Plugin Tailwind
  plugins: ["prettier-plugin-tailwindcss"],
};
```

## Ví dụ output với config này:

### Before:

```javascript
const component = (
  <div className="flex bg-red-500 text-white p-4 justify-center items-center">
    <span>Hello</span>
  </div>
);

const data = { name: "John", age: 30, hobbies: ["reading", "coding"] };
```

### After:

```javascript
const component = (
  <div className="flex items-center justify-center bg-red-500 p-4 text-white">
    <span>Hello</span>
  </div>
);

const data = {
  name: "John",
  age: 30,
  hobbies: ["reading", "coding"],
};
```

## Script package.json tương ứng:

```json
{
  "scripts": {
    "format": "prettier --write --ignore-unknown .",
    "format:check": "prettier --check --ignore-unknown .",
    "lint": "next lint",
    "lint:fix": "next lint --fix && prettier --write --ignore-unknown ."
  },
  "devDependencies": {
    "prettier": "^3.3.2",
    "prettier-plugin-tailwindcss": "^0.6.4"
  }
}
```

## Thêm .prettierignore:

```gitignore
# .prettierignore
node_modules
.next
.vercel
dist
build
*.lock
package-lock.json
pnpm-lock.yaml
```

Config của bạn rất solid cho Next.js project! Chỉ cần sửa `objectWrap` là hoàn hảo rồi 👌
