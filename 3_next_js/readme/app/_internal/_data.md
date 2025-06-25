Tôi sẽ giải thích cách viết TypeScript này từng phần:

## Phân tích cú pháp:

```typescript
const demo = [] as const satisfies DemoCategory[];
```

### 1. `as const` - Const Assertion

```typescript
[] as const;
```

**Mục đích**: Biến array thành **immutable tuple** với type cụ thể

**Không có `as const`:**

```typescript
const demo = ["a", "b"]; // type: string[]
```

**Có `as const`:**

```typescript
const demo = ["a", "b"] as const; // type: readonly ["a", "b"]
```

### 2. `satisfies` - Type Satisfaction

```typescript
satisfies DemoCategory[]
```

**Mục đích**: Đảm bảo giá trị **satisfy** một type nhưng **không thay đổi inferred type**

### 3. Kết hợp `as const satisfies`

```typescript
const demo = [] as const satisfies DemoCategory[];
```

## So sánh các cách viết:

### Cách 1: Chỉ type annotation

```typescript
const demo: DemoCategory[] = [];
// Type: DemoCategory[]
// Có thể mutate: demo.push(newItem)
```

### Cách 2: Chỉ as const

```typescript
const demo = [] as const;
// Type: readonly []
// Không biết có satisfy DemoCategory[] không
```

### Cách 3: as const satisfies (Best!)

```typescript
const demo = [] as const satisfies DemoCategory[];
// Type: readonly []
// Đảm bảo satisfy DemoCategory[]
// Immutable + Type safe
```

## Ví dụ thực tế:

```typescript
interface DemoCategory {
  id: string;
  name: string;
}

// ❌ Có thể mutate
const demos: DemoCategory[] = [
  { id: "1", name: "React" },
  { id: "2", name: "Vue" },
];
demos.push({ id: "3", name: "Angular" }); // OK

// ✅ Immutable + Type safe
const demos = [
  { id: "1", name: "React" },
  { id: "2", name: "Vue" },
] as const satisfies DemoCategory[];

// demos.push(...) // ❌ Error: Cannot assign to 'demos' because it is a constant
// demos[0].id = "new" // ❌ Error: Cannot assign to read-only property
```

## Lợi ích:

### 1. **Immutability**

```typescript
const colors = ["red", "blue"] as const satisfies string[];
// colors.push("green") // ❌ Error
```

### 2. **Precise Types**

```typescript
const status = ["pending", "success", "error"] as const satisfies string[];
// Type: readonly ["pending", "success", "error"]
// Không chỉ là string[] mà là exact values
```

### 3. **Type Safety**

```typescript
interface Config {
  theme: "dark" | "light";
}

const configs = [
  { theme: "dark" },
  { theme: "light" },
  // { theme: "blue" } // ❌ Error: không satisfy Config
] as const satisfies Config[];
```

## Khi nào sử dụng:

- **Configuration arrays** cần immutable
- **Constant data** không thay đổi trong runtime
- **Type-safe enums** thay thế cho enum
- **Lookup tables** cần exact types

Pattern này rất phổ biến trong modern TypeScript để có **type safety** và **immutability** tối đa!

---

---

Tôi sẽ giải thích cách viết TypeScript này - đây là một pattern rất hay để **extract union types từ nested arrays**!

## Phân tích từng phần:

```typescript
export type DemoSlug = (typeof demos)[number]["items"][number]["slug"];
```

### 1. `typeof demos`

```typescript
typeof demos;
```

**Lấy type của variable `demos`** thay vì value

Ví dụ:

```typescript
const demos = [
  {
    category: "React",
    items: [
      { slug: "hooks", name: "Hooks Demo" },
      { slug: "context", name: "Context Demo" },
    ],
  },
  {
    category: "Vue",
    items: [{ slug: "composition", name: "Composition API" }],
  },
] as const;

// typeof demos = readonly [{ category: "React", items: [...] }, { category: "Vue", items: [...] }]
```

### 2. `[number]` - Array Index Access

```typescript
(typeof demos)[number];
```

**Lấy type của một element bất kỳ trong array**

```typescript
// Kết quả:
// { category: "React", items: [...] } | { category: "Vue", items: [...] }
```

### 3. `['items']` - Property Access

```typescript
(typeof demos)[number]["items"];
```

**Lấy type của property `items`**

```typescript
// Kết quả:
// readonly [{ slug: "hooks", name: "Hooks Demo" }, ...] |
// readonly [{ slug: "composition", name: "Composition API" }]
```

### 4. `[number]` lần nữa

```typescript
(typeof demos)[number]["items"][number];
```

**Lấy type của một item bất kỳ trong `items` array**

```typescript
// Kết quả:
// { slug: "hooks", name: "Hooks Demo" } |
// { slug: "context", name: "Context Demo" } |
// { slug: "composition", name: "Composition API" }
```

### 5. `['slug']` - Final Property Access

```typescript
(typeof demos)[number]["items"][number]["slug"];
```

**Lấy type của property `slug`**

```typescript
// Kết quả final:
// "hooks" | "context" | "composition"
```

## Ví dụ hoàn chỉnh:

```typescript
const demos = [
  {
    category: "React",
    items: [
      { slug: "hooks", name: "Hooks Demo" },
      { slug: "context", name: "Context Demo" },
      { slug: "suspense", name: "Suspense Demo" },
    ],
  },
  {
    category: "Vue",
    items: [
      { slug: "composition", name: "Composition API" },
      { slug: "reactivity", name: "Reactivity Demo" },
    ],
  },
] as const;

// DemoSlug = "hooks" | "context" | "suspense" | "composition" | "reactivity"
export type DemoSlug = (typeof demos)[number]["items"][number]["slug"];

// Sử dụng:
function getDemoBySlug(slug: DemoSlug) {
  // slug chỉ có thể là một trong các giá trị trên
}

getDemoBySlug("hooks"); // ✅ OK
getDemoBySlug("invalid"); // ❌ Error
```

## Tại sao pattern này hữu ích:

### 1. **Single Source of Truth**

```typescript
// Thay vì define type riêng:
type DemoSlug = "hooks" | "context" | "composition"; // Có thể out of sync

// Dùng pattern này - auto sync với data:
type DemoSlug = (typeof demos)[number]["items"][number]["slug"];
```

### 2. **Type Safety**

```typescript
// TypeScript sẽ autocomplete và validate
function navigateToDemo(slug: DemoSlug) {
  router.push(`/demo/${slug}`);
}
```

### 3. **Maintainability**

Khi thêm/xóa demo trong `demos` array, type `DemoSlug` tự động update!

## Pattern tương tự:

```typescript
// Lấy tất cả category names
type CategoryName = (typeof demos)[number]["category"];

// Lấy tất cả demo names
type DemoName = (typeof demos)[number]["items"][number]["name"];

// Lấy keys của object
type ConfigKeys = keyof typeof config;

// Lấy values của object
type ConfigValues = (typeof config)[keyof typeof config];
```

Đây là **advanced TypeScript pattern** rất mạnh để tạo type-safe APIs từ runtime data!
