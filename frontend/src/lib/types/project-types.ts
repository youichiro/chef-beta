import { z } from "zod";

export const Project = z.object({
  id: z.number(),
  name: z.string(),
  project_type: z.object({
    id: z.number(),
    name: z.string(),
  }),
})

export type Project = z.infer<typeof Project>;

export const ProjectList = z.object({
  items: Project.array(),
  total: z.number(),
  page: z.number(),
  size: z.number(),
  pages: z.number(),
});

export const Guideline = z.object({
  id: z.number(),
  content: z.string(),
})

export const Dataset = z.object({
  id: z.number(),
  name: z.string(),
})

export const ProjectDeatil = z.object({
  id: z.number(),
  name: z.string(),
  project_type: z.object({
    name: z.string(),
  }),
  guideline: Guideline.optional(),
  datasets: Dataset.array(),
})
