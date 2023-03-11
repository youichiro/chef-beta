<script lang="ts">
  let getTodos = fetch('https://jsonplaceholder.typicode.com/todos').then(response => response.json())
</script>

{#await getTodos}
  loading...
{:then todos}
  {#each todos as todo}
    <p>{todo.title}</p>
  {/each}
{:catch error}
  <p>error! {error}</p>
{/await}
