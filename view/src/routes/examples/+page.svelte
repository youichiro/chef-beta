<script lang="ts">
  import { z } from 'zod'
  import PageTop from "$lib/components/PageTop.svelte";
  import Table from "$lib/components/Table.svelte";
  import { Spinner } from "flowbite-svelte";
  import Pagination from '$lib/components/Pagination.svelte';

  // https://jsonplaceholder.typicode.com
  let getTodos = fetch('https://jsonplaceholder.typicode.com/todos')
    .then(response => response.json())

  const TodosSchema = z.object({
    id: z.number(),
    title: z.string(),
  }).array()
</script>

<PageTop title="Example" page_path="examples/" />

<div>
  {#await getTodos}
    <div class="text-center">
      <Spinner />
    </div>
  {:then todos}
    <Table rows={TodosSchema.parse(todos).slice(0, 10)} key="id" />
    <Pagination />
  {:catch error}
    <p>error! {error}</p>
  {/await}
</div>
