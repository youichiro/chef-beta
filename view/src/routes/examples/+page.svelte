<script lang="ts">
  import PageTop from "$lib/components/PageTop.svelte";
  import { Spinner } from "flowbite-svelte";

  // https://jsonplaceholder.typicode.com
  let getTodos = fetch('https://jsonplaceholder.typicode.com/todos').then(response => response.json())
</script>

<PageTop title="Example" page_path="examples/" />

<div class="p-4">
  {#await getTodos}
    <div class="text-center">
      <Spinner />
    </div>
  {:then todos}
    {#each todos as todo}
      <p>{todo.title}</p>
    {/each}
  {:catch error}
    <p>error! {error}</p>
  {/await}
</div>
