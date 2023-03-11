<script lang="ts">
  import { z } from 'zod'
  import PageTop from "$lib/components/PageTop.svelte";
  import Table from "$lib/components/Table.svelte";
  import { Spinner } from "flowbite-svelte";
  import Pagination from '$lib/components/Pagination.svelte';

  let getTodos = fetch('http://localhost:4010/todos', {headers: {'Prefer': 'example=at_first'}})
    .then(response => response.json())

  const ResponseSchema = z.object({
    data: z.object({
      id: z.number(),
      title: z.string(),
    }).array(),
    total: z.number(),
    isFirst: z.boolean(),
    isLast: z.boolean(),
    prevOffset: z.nullable(z.number()),
    nextOffset: z.nullable(z.number()),
  })
</script>

<PageTop title="Example" page_path="examples/" />

<div>
  {#await getTodos}
    <div class="text-center">
      <Spinner />
    </div>
  {:then response}
    <Table rows={ResponseSchema.parse(response).data} key="id" />
    <Pagination />
  {:catch error}
    <p>error! {error}</p>
  {/await}
</div>
