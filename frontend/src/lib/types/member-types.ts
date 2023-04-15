import { z } from "zod";

export const Member = z.object({
  id: z.number(),
  name: z.string(),
})

export type Member = z.infer<typeof Member>;

export const MemberListResponse = z.object({
  items: Member.array(),
  total: z.number(),
  page: z.number(),
  size: z.number(),
  pages: z.number(),
});
