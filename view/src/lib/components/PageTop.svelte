<script lang="ts">
  export let page_path: string | undefined = undefined;
  export let title: string;
</script>

<div class="w-full bg-slate-100 px-4 py-4">
  {#if page_path}
    <p class="text-slate-500">{page_path}</p>
  {/if}
  <h2 class="text-xl font-bold my-2">{title}</h2>
</div>
