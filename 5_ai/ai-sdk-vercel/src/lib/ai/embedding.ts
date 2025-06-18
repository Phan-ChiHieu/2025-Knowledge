import { embed, embedMany } from "ai";
import { openai } from "@ai-sdk/openai";
import { db } from "../db";
import { cosineDistance, desc, gt, sql } from "drizzle-orm";
import { embeddings } from "../db/schema/embeddings";

const generateChunks = (input: string): string[] => {
  return input
    .trim()
    .split(".")
    .filter((i) => i !== "");
};

/*
🔹 Mục đích:
Tách một chuỗi input thành mảng các câu, sử dụng dấu "." làm dấu phân cách.

🔍 Chi tiết các bước:

    1 .trim(): Loại bỏ khoảng trắng đầu và cuối chuỗi.
    2 .split("."): Tách chuỗi thành mảng các phần tử dựa trên dấu ".".
    3 .filter((i) => i !== ""): Loại bỏ các phần tử rỗng (do có thể có dấu "." liên tiếp hoặc "." cuối chuỗi).

🧪 Ví dụ:

  ```txs
    const input = "Xin chào. Tôi là Edric. Đây là đoạn test.";
    const result = generateChunks(input);
    console.log(result);
  ```

=> Kết quả:

```txs
    [
      "Xin chào",
      " Tôi là Edric",
      " Đây là đoạn test"
    ]
  ```  
*/

//---------------==------------------------------------==------------------

const embeddingModel = openai.embedding("text-embedding-ada-002");

export const generateEmbeddings = async (value: string): Promise<Array<{ embedding: number[]; content: string }>> => {
  const chunks = generateChunks(value); // Tách input thành các câu riêng biệt và loại bỏ khoảng trắng lưu dưới dạng mảng.

  // link: https://ai-sdk.dev/docs/reference/ai-sdk-core/embed-many#embedmany
  const { embeddings } = await embedMany({
    model: embeddingModel,
    values: chunks,
  });
  return embeddings.map((e, i) => ({ content: chunks[i], embedding: e }));
};

/*
Todo  🧪 Ví dụ Demo:

Giả sử input là:

```ts
const input = "ChatGPT rất hữu ích. Nó giúp tôi viết code. Embedding thật tuyệt.";
```

Sau khi chạy `generateChunks(input)`:

```ts
chunks = [
  "ChatGPT rất hữu ích",
  " Nó giúp tôi viết code",
  " Embedding thật tuyệt"
];
```

Giả sử `embedMany()` trả về (giả lập):

```ts
embeddings = [
  [0.1, 0.2, 0.3],
  [0.4, 0.5, 0.6],
  [0.7, 0.8, 0.9]
];
```

* Thì kết quả `return` sẽ là:

```ts
[
  {
    content: "ChatGPT rất hữu ích",
    embedding: [0.1, 0.2, 0.3]
  },
  {
    content: " Nó giúp tôi viết code",
    embedding: [0.4, 0.5, 0.6]
  },
  {
    content: " Embedding thật tuyệt",
    embedding: [0.7, 0.8, 0.9]
  }
]
```
*/

//---------------==------------------------------------==------------------

export const generateEmbedding = async (value: string): Promise<number[]> => {
  const input = value.replaceAll("\\n", " ");
  const { embedding } = await embed({
    model: embeddingModel,
    value: input,
  });
  return embedding;
};

//---------------==------------------------------------==------------------

export const findRelevantContent = async (userQuery: string) => {
  const userQueryEmbedded = await generateEmbedding(userQuery);
  const similarity = sql<number>`1 - (${cosineDistance(embeddings.embedding, userQueryEmbedded)})`;
  const similarGuides = await db
    .select({ name: embeddings.content, similarity })
    .from(embeddings)
    .where(gt(similarity, 0.5))
    .orderBy((t) => desc(t.similarity))
    .limit(4);
  return similarGuides;
};
