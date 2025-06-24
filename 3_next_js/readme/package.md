# Next.js 14 App Router - Dependencies & DevDependencies

## 📦 DEPENDENCIES (Production)

### Core Next.js (Bắt buộc)

```json
{
  "next": "^14.2.0",
  "react": "^18.3.1",
  "react-dom": "^18.3.1"
}
```

### UI Components & Styling

```json
{
  // Headless UI Components
  "@headlessui/react": "^1.7.19",
  "@radix-ui/react-dialog": "^1.0.5",
  "@radix-ui/react-dropdown-menu": "^2.0.6",
  "@radix-ui/react-tabs": "^1.0.4",
  "@radix-ui/react-toast": "^1.1.5",
  "@radix-ui/react-tooltip": "^1.0.7",

  // Icons
  "lucide-react": "^0.263.1",
  "@heroicons/react": "^2.0.18",
  "react-icons": "^4.12.0",

  // Utility
  "clsx": "^2.1.1",
  "class-variance-authority": "^0.7.0",
  "tailwind-merge": "^2.3.0",

  // Runtime CSS-in-JS (nếu dùng)
  "styled-components": "^6.1.11",
  "@emotion/react": "^11.11.4",
  "@emotion/styled": "^11.11.5"
}
```

### Forms & Validation

```json
{
  "react-hook-form": "^7.51.4",
  "@hookform/resolvers": "^3.6.0",
  "zod": "^3.23.8",
  "yup": "^1.4.0"
}
```

### Data Fetching & State Management

```json
{
  // Data Fetching
  "swr": "^2.2.5",
  "@tanstack/react-query": "^5.40.0",
  "axios": "^1.7.2",

  // State Management
  "zustand": "^4.5.2",
  "jotai": "^2.8.4",
  "redux": "^5.0.1",
  "@reduxjs/toolkit": "^2.2.5",
  "react-redux": "^9.1.2"
}
```

### Database & ORM

```json
{
  "@prisma/client": "^5.14.0",
  "drizzle-orm": "^0.31.2",
  "mongoose": "^8.4.1",
  "@supabase/supabase-js": "^2.43.4",
  "pg": "^8.11.6",
  "mysql2": "^3.10.1"
}
```

### Authentication

```json
{
  "next-auth": "^4.24.7",
  "auth0-react": "^2.2.4",
  "clerk": "^5.1.0",
  "@clerk/nextjs": "^5.1.0",
  "firebase": "^10.12.2"
}
```

### Utilities & Helpers

```json
{
  "date-fns": "^3.6.0",
  "dayjs": "^1.11.11",
  "lodash": "^4.17.21",
  "nanoid": "^5.0.7",
  "uuid": "^10.0.0",
  "bcryptjs": "^2.4.3",
  "jsonwebtoken": "^9.0.2",
  "crypto-js": "^4.2.0"
}
```

### File Upload & Media

```json
{
  "react-dropzone": "^14.2.3",
  "multer": "^1.4.5-lts.1",
  "sharp": "^0.33.4",
  "cloudinary": "^2.2.0",
  "uploadthing": "^6.12.0"
}
```

### Animation & Motion

```json
{
  "framer-motion": "^11.2.10",
  "react-spring": "^9.7.3",
  "lottie-react": "^2.4.0"
}
```

### Charts & Visualization

```json
{
  "recharts": "^2.12.7",
  "chart.js": "^4.4.3",
  "react-chartjs-2": "^5.2.0",
  "d3": "^7.9.0"
}
```

### Email & Notifications

```json
{
  "nodemailer": "^6.9.13",
  "@sendgrid/mail": "^8.1.3",
  "resend": "^3.2.0",
  "react-hot-toast": "^2.4.1",
  "sonner": "^1.4.41"
}
```

### Payment

```json
{
  "stripe": "^15.12.0",
  "@stripe/stripe-js": "^3.5.0",
  "@stripe/react-stripe-js": "^2.7.1"
}
```

---

## 🛠️ DEVDEPENDENCIES (Development)

### TypeScript

```json
{
  "typescript": "^5.4.5",
  "@types/node": "^20.14.2",
  "@types/react": "^18.3.3",
  "@types/react-dom": "^18.3.0",
  "@types/lodash": "^4.17.5",
  "@types/bcryptjs": "^2.4.6",
  "@types/jsonwebtoken": "^9.0.6",
  "@types/uuid": "^10.0.0",
  "@types/multer": "^1.4.11"
}
```

### Linting & Formatting

```json
{
  "eslint": "^8.57.0",
  "eslint-config-next": "14.2.3",
  "eslint-config-prettier": "^9.1.0",
  "eslint-plugin-react": "^7.34.2",
  "eslint-plugin-react-hooks": "^4.6.2",
  "@typescript-eslint/eslint-plugin": "^7.13.0",
  "@typescript-eslint/parser": "^7.13.0",
  "prettier": "^3.3.2",
  "prettier-plugin-tailwindcss": "^0.6.4"
}
```

### CSS & Styling Build Tools

```json
{
  "tailwindcss": "^3.4.4",
  "postcss": "^8.4.38",
  "autoprefixer": "^10.4.19",
  "sass": "^1.77.5",
  "@tailwindcss/forms": "^0.5.7",
  "@tailwindcss/typography": "^0.5.13"
}
```

### Database Tools

```json
{
  "prisma": "^5.14.0",
  "drizzle-kit": "^0.22.7",
  "@types/pg": "^8.11.6"
}
```

### Testing

```json
{
  "jest": "^29.7.0",
  "jest-environment-jsdom": "^29.7.0",
  "@testing-library/react": "^16.0.0",
  "@testing-library/jest-dom": "^6.4.5",
  "@testing-library/user-event": "^14.5.2",
  "cypress": "^13.12.0",
  "@playwright/test": "^1.44.1",
  "vitest": "^1.6.0",
  "@vitejs/plugin-react": "^4.3.1"
}
```

### Build & Bundle Analysis

```json
{
  "@next/bundle-analyzer": "^14.2.3",
  "webpack-bundle-analyzer": "^4.10.2",
  "cross-env": "^7.0.3"
}
```

### Development Utilities

```json
{
  "concurrently": "^8.2.2",
  "nodemon": "^3.1.4",
  "rimraf": "^5.0.7",
  "husky": "^9.0.11",
  "lint-staged": "^15.2.7",
  "commitizen": "^4.3.0",
  "cz-conventional-changelog": "^3.3.0"
}
```

### Storybook (nếu dùng)

```json
{
  "@storybook/nextjs": "^8.1.10",
  "@storybook/react": "^8.1.10",
  "@storybook/addon-essentials": "^8.1.10",
  "@storybook/addon-interactions": "^8.1.10",
  "storybook": "^8.1.10"
}
```

---

## 🎯 PACKAGE.JSON MẪU CHO NEXT.JS 14

```json
{
  "name": "my-nextjs-app",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint",
    "lint:fix": "next lint --fix",
    "type-check": "tsc --noEmit",
    "test": "jest",
    "test:watch": "jest --watch",
    "db:push": "prisma db push",
    "db:generate": "prisma generate"
  },
  "dependencies": {
    "next": "^14.2.3",
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "@radix-ui/react-dialog": "^1.0.5",
    "lucide-react": "^0.263.1",
    "clsx": "^2.1.1",
    "tailwind-merge": "^2.3.0",
    "react-hook-form": "^7.51.4",
    "zod": "^3.23.8",
    "@prisma/client": "^5.14.0",
    "next-auth": "^4.24.7"
  },
  "devDependencies": {
    "@types/node": "^20.14.2",
    "@types/react": "^18.3.3",
    "@types/react-dom": "^18.3.0",
    "typescript": "^5.4.5",
    "eslint": "^8.57.0",
    "eslint-config-next": "14.2.3",
    "prettier": "^3.3.2",
    "tailwindcss": "^3.4.4",
    "postcss": "^8.4.38",
    "autoprefixer": "^10.4.19",
    "prisma": "^5.14.0"
  }
}
```

## 📝 LƯU Ý QUAN TRỌNG

### ✅ Luôn để trong DEPENDENCIES:

- Packages cần thiết cho runtime
- UI components được render
- Database clients (@prisma/client)
- Authentication libraries
- State management libraries
- API clients (axios, swr)

### ⚠️ Luôn để trong DEVDEPENDENCIES:

- TypeScript và @types packages
- Linting tools (eslint, prettier)
- Build tools (tailwindcss, postcss)
- Testing frameworks
- Database CLI tools (prisma CLI)
- Bundle analyzers
- Development servers

### 🔍 Cách kiểm tra:

```bash
# Test production build
npm run build
rm -rf node_modules
npm ci --only=production
npm start
```

Nếu app chạy được với lệnh trên, bạn đã phân chia đúng!
