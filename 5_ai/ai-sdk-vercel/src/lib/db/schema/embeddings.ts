import { nanoid } from "@/lib/utils";
import { index, pgTable, text, varchar, vector } from "drizzle-orm/pg-core";
import { resources } from "./resources";

export const embeddings = pgTable(
  "embeddings",
  {
    id: varchar("id", { length: 191 })
      .primaryKey()
      .$defaultFn(() => nanoid()),

    // resourceId: Foreign key liên kết đến resources.id.
    // Dùng để biết embedding này thuộc tài nguyên nào.
    // onDelete: "cascade" → nếu xoá resource, embedding liên quan cũng sẽ bị xoá (giữ dữ liệu sạch sẽ).
    resourceId: varchar("resource_id", { length: 191 }).references(() => resources.id, { onDelete: "cascade" }),
    content: text("content").notNull(),

    // embedding: Trường vector (pgvector), có 1536 chiều (đúng với text-embedding-ada-002 của OpenAI).
    embedding: vector("embedding", { dimensions: 1536 }).notNull(),
  },

  (table) => ({
    // Tạo index cho vector để tăng tốc độ tìm kiếm semantic.
    // Dùng thuật toán HNSW (Hierarchical Navigable Small World) – là một thuật toán rất nhanh và phổ biến cho vector search.
    // .op("vector_cosine_ops"): Dùng cosine similarity làm phép đo khoảng cách (phù hợp nhất với OpenAI embedding).
    // Tự đặt tên là "embeddingIndex" để dùng rõ ràng.
    embeddingIndex: index("embeddingIndex").using("hnsw", table.embedding.op("vector_cosine_ops")),
  })
);

/*

Todo 📌 Ý nghĩa của (table) => ({}):
Đây là hàm cấu hình nâng cao, cho phép bạn định nghĩa:

Index (chỉ mục)

Unique constraint

Check constraint

Foreign key (nếu cần định nghĩa thủ công)

Any other table-level constraint (tùy engine)

🟡 Khi viết () => ({}), tức là:
Bạn không định nghĩa gì thêm (return một object rỗng).

Tuy nhiên, bạn vẫn giữ lại callback này – có thể để bổ sung sau, hoặc đơn giản là do code theo một pattern chuẩn.
*/
