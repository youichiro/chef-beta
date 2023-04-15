import { z } from "zod";
import { DatasetSchema } from "$lib/types/dataset-types";

export const Project = z.object({
  id: z.number(),
  name: z.string(),
  project_type: z.object({
    id: z.number(),
    name: z.string(),
  }),
})

export type Project = z.infer<typeof Project>;

export const ProjectListSchema = z.object({
  items: Project.array(),
  total: z.number(),
  page: z.number(),
  size: z.number(),
  pages: z.number(),
});

export type ProjectList = z.infer<typeof ProjectListSchema>;

export const Guideline = z.object({
  id: z.number(),
  content: z.string(),
})

export const ProjectDetailSchema = z.object({
  id: z.number(),
  name: z.string(),
  project_type: z.object({
    name: z.string(),
  }),
  guideline: Guideline.optional(),
  datasets: DatasetSchema.array(),
})

export type ProjectDetail = z.infer<typeof ProjectDetailSchema>;
