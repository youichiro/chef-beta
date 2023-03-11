/** @type {import('./$types').PageLoad} */
export const load = async ({ fetch }) => {
  try {
    const response = await fetch("/projects/api");
    return await response.json();
  } catch (error) {
    console.log(`Error is load function for : ${error}`);
  }
};
