import { z } from "zod";

export const DatasetSchema = z.object({
  id: z.number(),
  name: z.string(),
})

export type Dataset = z.infer<typeof DatasetSchema>;

export const TabSchema = z.union([z.literal('datasets'), z.literal('guideline'), z.literal('members'), z.null()])
export type Tab = z.infer<typeof TabSchema>
