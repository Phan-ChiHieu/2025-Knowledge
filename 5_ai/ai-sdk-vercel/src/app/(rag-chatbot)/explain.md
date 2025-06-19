# RAG

## What is RAG ?

- RAG stands for retrieval augmented generation. In simple terms, RAG is the process of providing a Large Language Model (LLM) with specific information relevant to the prompt.
  > RAG là viết tắt của thế hệ tăng cường. Nói một cách đơn giản, RAG là quá trình cung cấp một mô hình ngôn ngữ lớn (LLM) các thông tin cụ thể liên quan đến dấu nhắc.

## Why is RAG important?

- While LLMs are powerful, the information they can reason on is restricted to the data they were trained on. This problem becomes apparent when asking an LLM for information outside of their training data, like proprietary data or common knowledge that has occurred after the model’s training cutoff. RAG solves this problem by fetching information relevant to the prompt and then passing that to the model as context.

  > Mặc dù LLM rất mạnh mẽ, thông tin họ có thể lý do được giới hạn trong dữ liệu họ được đào tạo. Vấn đề này trở nên rõ ràng khi hỏi một LLM về thông tin ngoài dữ liệu đào tạo của họ, như dữ liệu độc quyền hoặc kiến ​​thức phổ biến đã xảy ra sau khi mô hình cắt đào tạo. Rag giải quyết vấn đề này bằng cách tìm nạp thông tin liên quan đến lời nhắc và sau đó chuyển điều đó cho mô hình dưới dạng bối cảnh.

- To illustrate with a basic example, imagine asking the model for your favorite food:

  ```base
  **input**
  What is my favorite food?

  **generation**
  I don't have access to personal information about individuals, including their
  favorite foods.
  ```

- Not surprisingly, the model doesn’t know. But imagine, alongside your prompt, the model received some extra context:

  > Không có gì đáng ngạc nhiên, người mẫu không biết. Nhưng hãy tưởng tượng, bên cạnh lời nhắc của bạn, mô hình đã nhận được một số bối cảnh bổ sung:

  ```base
  **input**
  Respond to the user's prompt using only the provided context.
  user prompt: 'What is my favorite food?'
  context: user loves chicken nuggets

  **generation**
  Your favorite food is chicken nuggets!
  ```

- Just like that, you have augmented the model’s generation by providing relevant information to the query. Assuming the model has the appropriate information, it is now highly likely to return an accurate response to the users query. But how does it retrieve the relevant information? The answer relies on a concept called embedding.
  > Chỉ như vậy, bạn đã tăng cường thế hệ mô hình bằng cách cung cấp thông tin liên quan cho truy vấn. Giả sử mô hình có thông tin phù hợp, giờ đây nó rất có thể trả lại một phản hồi chính xác cho truy vấn người dùng. Nhưng làm thế nào để nó lấy lại thông tin liên quan? Câu trả lời phụ thuộc vào một khái niệm gọi là nhúng.

## Embedding

-[Embeddings](https://ai-sdk.dev/docs/ai-sdk-core/embeddings) are a way to represent words, phrases, or images as vectors in a high-dimensional space. In this space, similar words are close to each other, and the distance between words can be used to measure their similarity.

> Nhúng là một cách để thể hiện các từ, cụm từ hoặc hình ảnh như các vectơ trong một không gian chiều cao. Trong không gian này, các từ tương tự gần nhau và khoảng cách giữa các từ có thể được sử dụng để đo lường sự giống nhau của chúng.

- In practice, this means that if you embedded the words cat and dog, you would expect them to be plotted close to each other in vector space. The process of calculating the similarity between two vectors is called ‘cosine similarity’ where a value of 1 would indicate high similarity and a value of -1 would indicate high opposition. [Guild](https://jalammar.github.io/illustrated-word2vec/)

  > Trong thực tế, điều này có nghĩa là nếu bạn nhúng các từ mèo và chó, bạn sẽ mong đợi chúng được vẽ gần nhau trong không gian vector. Quá trình tính toán sự tương đồng giữa hai vectơ được gọi là ‘cosine tương tự trong đó giá trị 1 sẽ cho thấy độ tương tự cao và giá trị -1 sẽ cho thấy sự phản đối cao.

- As mentioned above, embeddings are a way to represent the semantic meaning of words and phrases. The implication here is that the larger the input to your embedding, the lower quality the embedding will be. So how would you approach embedding content longer than a simple phrase?
  > Như đã đề cập ở trên, việc nhúng là một cách để thể hiện ý nghĩa ngữ nghĩa của các từ và cụm từ. Hàm ý ở đây là đầu vào của bạn càng lớn, chất lượng nhỏ hơn của việc nhúng sẽ là. Vậy làm thế nào bạn sẽ tiếp cận việc nhúng nội dung lâu hơn một cụm từ đơn giản?

## Chunking

- Chunking refers to the process of breaking down a particular source material into smaller pieces. There are many different approaches to chunking and it’s worth experimenting as the most effective approach can differ by use case. A simple and common approach to chunking (and what you will be using in this guide) is separating written content by sentences.

  > Chunking đề cập đến quá trình phá vỡ một vật liệu nguồn cụ thể thành các mảnh nhỏ hơn. Có nhiều cách tiếp cận khác nhau để phân chia và nó đáng để thử nghiệm vì cách tiếp cận hiệu quả nhất có thể khác nhau theo trường hợp sử dụng. Một cách tiếp cận đơn giản và phổ biến để chunking (và những gì bạn sẽ sử dụng trong hướng dẫn này) là phân tách nội dung bằng văn bản theo các câu.

- Once your source material is appropriately chunked, you can embed each one and then store the embedding and the chunk together in a database. Embeddings can be stored in any database that supports vectors. For this tutorial, you will be using [Postgres](https://www.postgresql.org/) alongside the [pgvector](https://github.com/pgvector/pgvector) plugin.
  > Khi tài liệu nguồn của bạn được chunk thích hợp, bạn có thể nhúng từng cái và sau đó lưu trữ nhúng và chunk với nhau trong cơ sở dữ liệu. Nhúng có thể được lưu trữ trong bất kỳ cơ sở dữ liệu nào hỗ trợ các vectơ. Đối với hướng dẫn này, bạn sẽ sử dụng Postgres cùng với plugin PGVector.

![Images Demo](../../../public/images/rag/chunk_1.webp)

---

## All Together Now

- Combining all of this together, RAG is the process of enabling the model to respond with information outside of it’s training data by embedding a users query, retrieving the relevant source material (chunks) with the highest semantic similarity, and then passing them alongside the initial query as context. Going back to the example where you ask the model for your favorite food, the prompt preparation process would look like this.
  > Kết hợp tất cả những điều này với nhau, RAG là quá trình cho phép mô hình trả lời với thông tin bên ngoài dữ liệu đào tạo của nó bằng cách nhúng truy vấn người dùng, truy xuất tài liệu nguồn liên quan (khối) với sự tương đồng ngữ nghĩa cao nhất, sau đó chuyển chúng cùng với câu hỏi ban đầu làm bối cảnh. Quay trở lại ví dụ mà bạn hỏi mô hình cho thực phẩm yêu thích của bạn, quá trình chuẩn bị nhanh chóng sẽ trông như thế này.

![Images Demo](../../../public/images/rag/chunk_2.webp)

- By passing the appropriate context and refining the model’s objective, you are able to fully leverage its strengths as a reasoning machine.
  > Bằng cách vượt qua bối cảnh thích hợp và tinh chỉnh mục tiêu mô hình, bạn có thể tận dụng đầy đủ các điểm mạnh của nó như một cỗ máy lý luận.

---

# Setup Project

## Tải pgvector/pgvector:pg17 với Docker:

### create file: docker-compose.yml

```yaml
version: "3.8"

services:
  pgvector:
    image: pgvector/pgvector:pg17
    container_name: pgvector-db
    restart: unless-stopped
    ports:
      - "5432:5432"
    environment:
      POSTGRES_USER: postgres-user
      POSTGRES_PASSWORD: 123456
      POSTGRES_DB: pgvector-db
    volumes:
      - pgvector_data:/var/lib/postgresql/data

volumes:
  pgvector_data:
```

Đây là file **Docker Compose** để thiết lập database PostgreSQL với extension pgvector

## Cấu trúc tổng quan

```yaml
version: "3.8"
```

- Chỉ định phiên bản Docker Compose format
- Version 3.8 hỗ trợ đầy đủ các tính năng hiện đại

## Service pgvector

### Image và Container

```yaml
image: pgvector/pgvector:pg17
container_name: pgvector-db
```

- **Image**: `pgvector/pgvector:pg17` - PostgreSQL 17 với pgvector extension được cài sẵn
- **pgvector** là extension cho phép lưu trữ và tìm kiếm vector embeddings (dùng cho AI/ML)
- **Container name**: Đặt tên cố định là `pgvector-db`

### Network và Restart Policy

```yaml
restart: unless-stopped
ports:
  - "5432:5432"
```

- **Restart policy**: Container sẽ tự động khởi động lại khi Docker daemon restart, trừ khi bị stop thủ công
- **Port mapping**: Expose port 5432 (PostgreSQL standard port) từ container ra host

### Environment Variables

```yaml
environment:
  POSTGRES_USER: postgres-user
  POSTGRES_PASSWORD: 123456
  POSTGRES_DB: pgvector-db
```

- **POSTGRES_USER**: Tên user database (postgres-user)
- **POSTGRES_PASSWORD**: Mật khẩu (123456 - không an toàn cho production)
- **POSTGRES_DB**: Tên database sẽ được tạo tự động

### Volume Mapping

```yaml
volumes:
  - pgvector_data:/var/lib/postgresql/data
```

- Mount named volume `pgvector_data` vào `/var/lib/postgresql/data`
- Đảm bảo data persistent khi container bị xóa/tạo lại

## Named Volume

```yaml
volumes:
  pgvector_data:
```

- Định nghĩa named volume để lưu trữ data PostgreSQL
- Docker sẽ quản lý volume này tự động

## Cách sử dụng

### Khởi chạy

```bash
docker-compose up -d
```

### Kết nối database

```bash
# Connection string
postgresql://postgres-user:123456@localhost:5432/pgvector-db

```

---

## create file: drizzle.config.ts

```tsx
import { config } from "dotenv";
import { defineConfig } from "drizzle-kit";

config({
  path: ".env.local",
});

export default defineConfig({
  schema: "./src/lib/db/schema",
  out: "./src/lib/db/migrations",
  dialect: "postgresql",
  dbCredentials: {
    // biome-ignore lint: Forbidden non-null assertion.
    url: process.env.DATABASE_URL!,
  },
});
```

- Vì toàn bộ code nằm trong src nên ta sẽ bắt đầu từ ./src/\*\* đi vô

---

## Update package.json

```shell
{
  "name": "ai-sdk-vercel",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev --turbopack",
    "build": "next build",
    "start": "next start",
    "lint": "next lint",
    "db:generate": "drizzle-kit generate",
    "db:migrate": "tsx src/lib/db/migrate.ts",
    "db:drop": "drizzle-kit drop",
    "db:pull": "drizzle-kit introspect",
    "db:push": "drizzle-kit push",
    "db:studio": "drizzle-kit studio",
    "db:check": "drizzle-kit check"
  },
  "dependencies": {
    "@ai-sdk/openai": "^1.3.22",
    "@ai-sdk/react": "^1.2.12",
    "@radix-ui/react-slot": "^1.2.3",
    "ai": "^4.3.16",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "dotenv": "^16.5.0",
    "drizzle-orm": "^0.44.2",
    "drizzle-zod": "^0.5.1",
    "lucide-react": "^0.515.0",
    "next": "15.3.3",
    "pg": "^8.16.0",
    "postgres": "^3.4.7",
    "react": "^19.0.0",
    "react-dom": "^19.0.0",
    "tailwind-merge": "^3.3.1",
    "zod": "^3.25.64"
  },
  "devDependencies": {
    "@tailwindcss/postcss": "^4",
    "@types/node": "^20",
    "@types/pg": "^8.15.4",
    "@types/react": "^19",
    "@types/react-dom": "^19",
    "drizzle-kit": "^0.31.1",
    "tailwindcss": "^4",
    "tsx": "^4.20.3",
    "tw-animate-css": "^1.3.4",
    "typescript": "^5"
  }
}

```

---

## create all: /src/lib/db

---

---

---

# BUILD

## 1.Create a table in your database to store embeddings

- Currently, your application has one table (`resources`) which has a column (`content`) for storing content. Remember, each `resource` (source material) will have to be chunked, embedded, and then stored. Let’s create a table called `embeddings` to store these chunks.

- Create a new file (`lib/db/schema/embeddings.ts`) and add the following code:

```tsx
import { nanoid } from "@/lib/utils";
import { index, pgTable, text, varchar, vector } from "drizzle-orm/pg-core";
import { resources } from "./resources";

export const embeddings = pgTable(
  "embeddings",
  {
    id: varchar("id", { length: 191 })
      .primaryKey()
      .$defaultFn(() => nanoid()),
    resourceId: varchar("resource_id", { length: 191 }).references(() => resources.id, { onDelete: "cascade" }),
    content: text("content").notNull(),
    embedding: vector("embedding", { dimensions: 1536 }).notNull(),
  },
  (table) => ({
    embeddingIndex: index("embeddingIndex").using("hnsw", table.embedding.op("vector_cosine_ops")),
  })
);
```

This table has four columns:

- `id` - unique identifier
- `resourceId` - a foreign key relation to the full source material
- `content` - the plain text chunk
- `embedding` - the vector representation of the plain text chunk -> biểu diễn vector của đoạn văn bản đơn giản

To push this change to the database, run the following command:

```shell
npm run db:push
```

## 2.Add Embedding Logic

- file: `src/lib/ai/embedding.ts`

```tsx
const generateChunks = (input: string): string[] => {
  return input
    .trim()
    .split(".")
    .filter((i) => i !== "");
};
```

- This function will take an input string and split it by periods, filtering out any empty items. This will return an array of strings. It is worth experimenting with different chunking techniques in your projects as the best technique will vary.

  > Hàm này sẽ lấy một chuỗi đầu vào và chia nó theo các khoảng thời gian, lọc ra bất kỳ mục trống nào. Điều này sẽ trả lại một mảng chuỗi. Điều đáng để thử nghiệm với các kỹ thuật chunking khác nhau trong các dự án của bạn vì kỹ thuật tốt nhất sẽ khác nhau.

- Code hoàn chỉnh của file: `src/lib/ai/embedding.ts`

```tsx
import { embedMany } from "ai";
import { openai } from "@ai-sdk/openai";

const embeddingModel = openai.embedding("text-embedding-ada-002");

const generateChunks = (input: string): string[] => {
  return input
    .trim()
    .split(".")
    .filter((i) => i !== "");
};

export const generateEmbeddings = async (value: string): Promise<Array<{ embedding: number[]; content: string }>> => {
  const chunks = generateChunks(value);
  const { embeddings } = await embedMany({
    model: embeddingModel,
    values: chunks,
  });
  return embeddings.map((e, i) => ({ content: chunks[i], embedding: e }));
};
```

- In this code, you first define the model you want to use for the embeddings. In this example, you are using OpenAI’s `text-embedding-ada-002` embedding model.

  > Trong mã này, trước tiên bạn xác định mô hình bạn muốn sử dụng cho các nhúng. Trong ví dụ này, bạn đang sử dụng mô hình nhúng văn bản Openai `text-embedding-ada-002`.

- Next, you create an asynchronous function called `generateEmbeddings`. This function will take in the source material (`value`) as an input and return a promise of an array of of objects, each containing an embedding and content. Within the function, you first generate chunks for the input. Then, you pass those chunks to the [embedMany](https://ai-sdk.dev/docs/reference/ai-sdk-core/embed-many) function imported from the AI SDK which will return embeddings of the chunks you passed in. Finally, you map over and return the embeddings in a format that is ready to save in the database.
  > Tiếp theo, bạn tạo một chức năng không đồng bộ gọi là `generateEmbeddings`. Hàm này sẽ lấy tài liệu nguồn (giá trị) làm đầu vào và trả lại lời hứa về một mảng của các đối tượng, mỗi đối tượng chứa một sự nhúng và nội dung. Trong chức năng, trước tiên bạn tạo các khối cho đầu vào. Sau đó, bạn chuyển các khối đó cho chức năng nhúng được nhập từ AI SDK sẽ trả về các phần nhúng của các khối bạn truyền vào. Cuối cùng, bạn ánh xạ và trả lại các nhúng theo định dạng đã sẵn sàng để lưu trong cơ sở dữ liệu.

-> Tóm lại là chuyển văn bản thành vector để chuẩn bị lưu vào DB

## 3. Update Server Action file: src/lib/actions/resources.ts

```tsx
"use server";

import { NewResourceParams, insertResourceSchema, resources } from "@/lib/db/schema/resources";
import { db } from "../db";

export const createResource = async (input: NewResourceParams) => {
  try {
    const { content } = insertResourceSchema.parse(input);

    const [resource] = await db.insert(resources).values({ content }).returning();

    return "Resource successfully created.";
  } catch (e) {
    if (e instanceof Error) return e.message.length > 0 ? e.message : "Error, please try again.";
  }
};
```

- This function is a Server Action, as denoted by the “use server”; directive at the top of the file. This means that it can be called anywhere in your Next.js application. This function will take an input, run it through a Zod schema to ensure it adheres to the correct schema, and then creates a new resource in the database. This is the ideal location to generate and store embeddings of the newly created resources.

  > Chức năng này là một hành động của máy chủ, như được biểu thị bằng máy chủ sử dụng máy chủ; Chỉ thị ở đầu tập tin. Điều này có nghĩa là nó có thể được gọi ở bất cứ đâu trong ứng dụng tiếp theo của bạn. Hàm này sẽ lấy một đầu vào, chạy nó thông qua một lược đồ ZOD để đảm bảo nó tuân thủ đúng lược đồ, sau đó tạo một tài nguyên mới trong cơ sở dữ liệu. Đây là vị trí lý tưởng để tạo và lưu trữ các tài nguyên mới được tạo.

- Hoàn thiện code:

```tsx
"use server";

import { NewResourceParams, insertResourceSchema, resources } from "@/lib/db/schema/resources";
import { db } from "../db";
// Update thêm
import { generateEmbeddings } from "../ai/embedding";
import { embeddings as embeddingsTable } from "../db/schema/embeddings";

export const createResource = async (input: NewResourceParams) => {
  try {
    const { content } = insertResourceSchema.parse(input);

    const [resource] = await db.insert(resources).values({ content }).returning();

    // Update thêm
    const embeddings = await generateEmbeddings(content);
    await db.insert(embeddingsTable).values(
      embeddings.map((embedding) => ({
        resourceId: resource.id,
        ...embedding,
      }))
    );

    return "Resource successfully created and embedded.";
  } catch (error) {
    return error instanceof Error && error.message.length > 0 ? error.message : "Error, please try again.";
  }
};
```

---

more: https://ai-sdk.dev/docs/guides/rag-chatbot#refining-your-prompt
