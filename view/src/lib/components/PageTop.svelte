<script lang="ts">
  export let pagePath: string | undefined = undefined;
  export let title: string;
</script>

<div class="w-full bg-slate-100 px-4 py-4">
  {#if pagePath}
    <p class="text-slate-500">{pagePath}</p>
  {/if}
  <h2 class="text-xl font-bold my-2">{title}</h2>
</div>
