import { env } from "@/lib/env.mjs";
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  schema: "./src/lib/db/schema",
  out: "./src/lib/db/migrations",
  dialect: "postgresql",
  dbCredentials: {
    // biome-ignore lint: Forbidden non-null assertion.
    url: env.DATABASE_URL,
  },
});
