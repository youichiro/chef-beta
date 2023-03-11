<script lang="ts">
  import PageTop from "$lib/components/PageTop.svelte";
  import Table from "$lib/components/Table.svelte";
  import { Spinner } from "flowbite-svelte";

  // https://jsonplaceholder.typicode.com
  let getTodos = fetch('https://jsonplaceholder.typicode.com/todos').then(response => response.json())
</script>

<PageTop title="Example" page_path="examples/" />

<div class="p-2">
  {#await getTodos}
    <div class="text-center">
      <Spinner />
    </div>
  {:then todos}
    <Table rows={todos} key="id" />
  {:catch error}
    <p>error! {error}</p>
  {/await}
</div>
