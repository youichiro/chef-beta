<script lang="ts">
  import { z } from 'zod'
  import PageTop from "$lib/components/PageTop.svelte";
  import Table from "$lib/components/Table.svelte";
  import { Spinner } from "flowbite-svelte";
  import Pagination from '$lib/components/Pagination.svelte';

  let getProjects = fetch('http://localhost:8000/api/projects')
    .then(response => response.json())

  const ResponseSchema = z.object({
    items: z.object({
      id: z.number(),
      name: z.string(),
    }).array(),
    total: z.number(),
    page: z.number(),
    size: z.number(),
    pages: z.number(),
  })
</script>

<PageTop title="Example" page_path="examples/" />

<div>
  {#await getProjects}
    <div class="text-center">
      <Spinner />
    </div>
  {:then response}
    <Table rows={ResponseSchema.parse(response).items} key="id" />
    <Pagination />
  {:catch error}
    <p>error! {error}</p>
  {/await}
</div>
