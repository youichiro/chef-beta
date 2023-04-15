import { TabSchema } from "$lib/types/dataset-types";
import type { PageLoad } from "./$types";

export const load = (({ params, url }) => {
  const tab = url.searchParams.get("tab")
  return {
    id: params.id,
    tab: TabSchema.parse(tab),
  }
}) satisfies PageLoad;
