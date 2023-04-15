import { z } from "zod";

export const Project = z.object({
  id: z.number(),
  name: z.string(),
  project_type: z.object({
    name: z.string(),
  }),
})

export type Project = z.infer<typeof Project>;

export const ProjectListResponse = z.object({
  items: Project.array(),
  total: z.number(),
  page: z.number(),
  size: z.number(),
  pages: z.number(),
});
