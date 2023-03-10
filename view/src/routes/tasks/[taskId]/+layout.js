import { error } from "@sveltejs/kit";

/** @type {import('./$types').PageLoad} */
export const load = async ({ params }) => {
  if (params.taskId === "1") {
    return { taskId: params.taskId };
  }

  throw error(404, "Not Found");
};
