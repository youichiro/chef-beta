<script lang="ts">
  import { createEventDispatcher } from "svelte";
  import { Button } from "flowbite-svelte";
  import type { Label } from "$lib/types";

  export let show: boolean = false;
  export let labels: Label[] = []
  export let top: number | null = null;
  export let left: number | null = null;
  $: modalStyle = (top && left) ? `top: ${top}px; left: ${left}px;` : "";

  const dispatch = createEventDispatcher();
  const selectLabel = (label: Label) => {
    dispatch('select', { label });
  }
</script>

{#if show}
  <div class="fixed bg-white my-2 z-20 border rounded shadow flex flex-col" style={modalStyle}>
    {#each labels as label}
      <Button
        color="alternative"
        size="sm"
        btnClass="border-none py-2 px-4 w-full hover:bg-slate-100 text-left"
        on:click={() => selectLabel(label)}>{label.name}
      </Button>
    {/each}
  </div>
{/if}
