import type { PageLoad } from './$types'

export const load = (({ url }) => {
  const page = Number(url.searchParams.get('page') ?? '1')
  return { page }
}) satisfies PageLoad;
