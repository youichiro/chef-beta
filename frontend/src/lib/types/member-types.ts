import { z } from "zod";

export const MemberSchema = z.object({
  id: z.number(),
  name: z.string(),
})

export type Member = z.infer<typeof MemberSchema>;

export const MemberListResponse = z.object({
  items: MemberSchema.array(),
  total: z.number(),
  page: z.number(),
  size: z.number(),
  pages: z.number(),
});

export const ProjectMemberSchema = z.object({
  id: z.number(),
  member: MemberSchema,
})

export type ProjectMember = z.infer<typeof ProjectMemberSchema>;

export const ProjectMemberListSchema = z.object({
  items: ProjectMemberSchema.array(),
  total: z.number(),
  page: z.number(),
  size: z.number(),
  pages: z.number(),
});

export type ProjectMemberList = z.infer<typeof ProjectMemberListSchema>;
