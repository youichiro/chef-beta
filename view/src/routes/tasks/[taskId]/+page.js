import { error } from "@sveltejs/kit";

/** @type {import('./$types').PageLoad} */
export const load = async ({ params, fetch }) => {
  if (params.taskId !== "1") {
    throw error(404, "Not Found");
  }

  try {
    const response = await fetch(`/tasks/${params.taskId}/api`);
    return await response.json();
  } catch (error) {
    console.log(`Error is load function for : ${error}`);
  }
};
