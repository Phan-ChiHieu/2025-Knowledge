Ah tôi hiểu rồi! Bạn hỏi về sự khác biệt giữa **function declaration** và **arrow function** trong JavaScript/TypeScript. Đây là những điểm khác biệt chính:

## 1. **Hoisting**

```javascript
// Function declaration - được hoisted
console.log(myFunc()); // ✅ Hoạt động - "Hello"

function myFunc() {
  return "Hello";
}

// Arrow function - không được hoisted
console.log(myArrow()); // ❌ ReferenceError

const myArrow = () => {
  return "Hello";
};
```

## 2. **Context của `this`**

```javascript
const obj = {
  name: "John",

  // Function declaration - có context `this` riêng
  regularFunc: function () {
    console.log(this.name); // "John"

    setTimeout(function () {
      console.log(this.name); // undefined (hoặc global object)
    }, 1000);
  },

  // Arrow function - kế thừa `this` từ scope bên ngoài
  arrowFunc: () => {
    console.log(this.name); // undefined (this = global/window)
  },

  mixedExample: function () {
    console.log(this.name); // "John"

    setTimeout(() => {
      console.log(this.name); // "John" - kế thừa từ mixedExample
    }, 1000);
  },
};
```

## 3. **Arguments object**

```javascript
// Function declaration - có arguments object
function regularFunc() {
  console.log(arguments); // [1, 2, 3]
  console.log(arguments.length); // 3
}
regularFunc(1, 2, 3);

// Arrow function - không có arguments
const arrowFunc = () => {
  console.log(arguments); // ❌ ReferenceError
};

// Arrow function - dùng rest parameters thay thế
const arrowFuncWithRest = (...args) => {
  console.log(args); // [1, 2, 3]
};
```

## 4. **Constructor usage**

```javascript
// Function declaration - có thể dùng làm constructor
function Person(name) {
  this.name = name;
}
const person1 = new Person("John"); // ✅ Hoạt động

// Arrow function - không thể dùng làm constructor
const PersonArrow = (name) => {
  this.name = name;
};
const person2 = new PersonArrow("Jane"); // ❌ TypeError
```

## 5. **Prototype**

```javascript
// Function declaration - có prototype
function regularFunc() {}
console.log(regularFunc.prototype); // {}

// Arrow function - không có prototype
const arrowFunc = () => {};
console.log(arrowFunc.prototype); // undefined
```

## 6. **Method definitions**

```javascript
class MyClass {
  // Method - có context `this` bình thường
  regularMethod() {
    console.log(this); // MyClass instance
  }

  // Arrow function property - `this` từ class scope
  arrowMethod = () => {
    console.log(this); // MyClass instance (bound permanently)
  };
}

const obj = new MyClass();
const extracted = obj.regularMethod;
extracted(); // undefined hoặc global object

const extractedArrow = obj.arrowMethod;
extractedArrow(); // vẫn là MyClass instance
```

## 7. **TypeScript-specific differences**

```typescript
// Function declaration - dễ dàng overload
function process(x: string): string;
function process(x: number): number;
function process(x: any): any {
  return x;
}

// Arrow function - khó overload hơn
type ProcessFn = {
  (x: string): string;
  (x: number): number;
};

const processArrow: ProcessFn = (x: any) => x;
```

## 8. **Performance**

```javascript
// Arrow functions thường nhanh hơn một chút khi được tạo
// vì không cần tạo context `this` mới

// Nhưng function declarations có thể được optimize tốt hơn
// bởi JavaScript engine do hoisting
```

## **Khi nào dùng cái gì?**

**Function Declaration:**

- Khi cần hoisting
- Khi cần `this` context riêng
- Khi làm constructor
- Khi cần `arguments` object

**Arrow Function:**

- Khi muốn kế thừa `this` từ scope bên ngoài
- Callbacks, event handlers
- Functional programming
- Khi muốn syntax ngắn gọn
- Method trong class (để bind `this` permanent)
