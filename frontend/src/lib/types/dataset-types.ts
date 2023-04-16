import { z } from "zod";

export const TabSchema = z.union([z.literal('datasets'), z.literal('guideline'), z.literal('members'), z.literal("detail")])
export type Tab = z.infer<typeof TabSchema>

export const DatasetSchema = z.object({
  id: z.number(),
  name: z.string(),
})

export type Dataset = z.infer<typeof DatasetSchema>;

export const DatasetListSchema = z.object({
  items: DatasetSchema.array(),
  total: z.number(),
  page: z.number(),
  size: z.number(),
  pages: z.number(),
});

export type DatasetList = z.infer<typeof DatasetListSchema>;
