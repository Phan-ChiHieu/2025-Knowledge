import { sql } from "drizzle-orm";
import { text, varchar, timestamp, pgTable } from "drizzle-orm/pg-core";
import { createSelectSchema } from "drizzle-zod";
import { z } from "zod";

import { nanoid } from "@/lib/utils";

export const resources = pgTable("resources", {
  id: varchar("id", { length: 191 }) // Kiểu varchar với độ dài tối đa 191 ký tự
    .primaryKey() // khóa chính
    .$defaultFn(() => nanoid()), // Mặc định tạo bằng hàm nanoid() – dùng để sinh một ID ngẫu nhiên (thường dùng trong các hệ thống không muốn lộ ID tăng dần).

  content: text("content").notNull(), // Nội dung của tài nguyên, có thể là văn bản, HTML, v.v.

  createdAt: timestamp("created_at")
    .notNull()
    .default(sql`now()`), // Giá trị mặc định là thời gian hiện tại (sql\now()``).
  updatedAt: timestamp("updated_at")
    .notNull()
    .default(sql`now()`),
});

//---------------==------------------------------------==------------------

// Schema for resources - used to validate API requests
export const insertResourceSchema = createSelectSchema(resources).extend({}).omit({
  id: true,
  createdAt: true,
  updatedAt: true,
});

/*
  Explain:

    - createSelectSchema(resources): Tự động sinh zod schema từ bảng resources, giúp đồng bộ kiểu dữ liệu từ database sang validation.

    - .extend({}): Có thể dùng để thêm các field custom, nhưng hiện để trống.

    - .omit({ id, createdAt, updatedAt }): Bỏ qua 3 field vì khi insert, chúng được tạo tự động (id từ nanoid, createdAt/updatedAt từ now()), không cần client truyền vào.

    ==>  Kết quả: Schema chỉ còn lại content – là field bắt buộc client phải truyền vào khi tạo mới tài nguyên.
*/

//---------------==------------------------------------==------------------

// Type for resources - used to type API request params and within Components
export type NewResourceParams = z.infer<typeof insertResourceSchema>;

// Explain: Suy ra kiểu dữ liệu TypeScript tương ứng từ insertResourceSchema, giúp type-safe trong các đoạn code khác như controller, form, hoặc gọi API.
