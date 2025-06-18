import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";
import { customAlphabet } from "nanoid";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

// Tạo một ID ngẫu nhiên với độ dài 21 ký tự, bao gồm chữ cái thường và số
export const nanoid = customAlphabet("abcdefghijklmnopqrstuvwxyz0123456789");
