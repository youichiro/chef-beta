import { TabSchema } from "$lib/types/dataset-types";
import type { PageLoad } from "./$types";

export const load = (({ params, url }) => {
  const tab = url.searchParams.get("tab");
  const page = Number(url.searchParams.get("page") ?? "1");

  return {
    id: params.id,
    tab: TabSchema.parse(tab),
    page,
  }
}) satisfies PageLoad;
