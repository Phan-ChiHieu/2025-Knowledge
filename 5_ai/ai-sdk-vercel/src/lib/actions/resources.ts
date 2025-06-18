"use server";

import { NewResourceParams, insertResourceSchema, resources } from "@/lib/db/schema/resources";
import { db } from "../db";
import { generateEmbeddings } from "../ai/embedding";
import { embeddings as embeddingsTable } from "../db/schema/embeddings";

// resources: tài nguyên có thể là tài liệu, bài viết, video, v.v.
export const createResource = async (input: NewResourceParams) => {
  try {
    const { content } = insertResourceSchema.parse(input); // Validate input từ client bằng insertResourceSchema.

    // chèn bản ghi mới vào bảng resources và trả về bản ghi vừa chèn.
    // CHỉ cần content, id và createdAt sẽ được tự động tạo.
    const [resource] = await db.insert(resources).values({ content }).returning();

    const embeddings = await generateEmbeddings(content);
    /* 
      Ví du về embeddings:
      const embeddings = [
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
      
    */

    // Chèn các embedding vào bảng embeddings, liên kết với resource mới tạo.
    // Mỗi embedding sẽ có resourceId là id của resource mới tạo.
    await db.insert(embeddingsTable).values(
      embeddings.map((embedding) => ({
        resourceId: resource.id,
        ...embedding,
      }))
    );

    return "Resource successfully created and embedded.";
  } catch (error) {
    // console.error("Error creating resource:", error);
    return error instanceof Error && error.message.length > 0 ? error.message : "Error, please try again.";
  }
};
