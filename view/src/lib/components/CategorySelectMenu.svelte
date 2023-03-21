<script lang="ts">
  import { createEventDispatcher } from "svelte";
  import { Button } from "flowbite-svelte";
  import type { Category } from "$lib/types";

  export let categories: Category[] = []
  export let rect: DOMRect | null = null;
  $: modalStyle = rect ? `top: ${rect.bottom}px; left: ${rect.left}px;` : "";

  const dispatch = createEventDispatcher();
  const selectCategory = (category: Category) => {
    dispatch('click', { category });
  }

  const styles = {
    selectBtn: "border-none py-2 px-4 w-full hover:bg-slate-100 text-left"
  }
</script>


<div class="fixed bg-white my-2 z-20 border rounded shadow flex flex-col" style={modalStyle}>
  {#each categories as category}
    <Button color="alternative" size="sm" btnClass={styles.selectBtn} on:click={() => selectCategory(category)}>{category.name}</Button>
  {/each}
</div>
