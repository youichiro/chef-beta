<script lang="ts">
  import { z } from 'zod'
  import PageTop from "$lib/components/PageTop.svelte";
  import Table from "$lib/components/Table.svelte";
  import { Spinner } from "flowbite-svelte";
  import Pagination from '$lib/components/Pagination.svelte';
  import type { PageData } from './$types';

  export let data: PageData;

  const getProjects = async () => {
    const response = await self.fetch(`http://localhost:8000/api/projects?page=${data.page}&size=3`);
    if (response.ok) {
      return response.json();
    } else {
      throw new Error(`status: ${response.status}, ${response.statusText}`);
    }
  }

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

  let promise = getProjects();
</script>

<PageTop title="Example" page_path="examples/" />

<div>
  {#await promise}
    <div class="text-center">
      <Spinner />
    </div>
  {:then response}
    {#if response.items.length === 0}
      <p>items empty.</p>
    {:else}
      <Table rows={ResponseSchema.parse(response).items} key="id" />
      <Pagination currentPage={data.page} lastPage={ResponseSchema.parse(response).pages} />
    {/if}
  {:catch error}
    <p>error! {error}</p>
  {/await}
</div>
