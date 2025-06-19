import { openai } from "@ai-sdk/openai";
import { xai } from "@ai-sdk/xai";
import { streamText, type Message } from "ai";

export const maxDuration = 30;

export async function POST(req: Request) {
  const { messages }: { messages: Message[] } = await req.json();

  // check if user has sent a PDF
  const messagesHavePDF = messages.some((message) => message.experimental_attachments?.some((a) => a.contentType === "application/pdf"));

  const result = streamText({
    model: messagesHavePDF ? xai("grok-2-vision-1212") : openai("gpt-4o"),
    messages,
  });

  return result.toDataStreamResponse();
}
