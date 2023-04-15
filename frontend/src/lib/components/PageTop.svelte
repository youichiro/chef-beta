<script lang="ts">
  import { Breadcrumb, BreadcrumbItem } from "flowbite-svelte";

  type Page = {
    name: string,
    url: string,
  }

  export let pages: Page[] = [];
  export let title: string;
</script>

<div class="w-full bg-slate-50 px-4 py-4">
  {#if pages.length > 0}
    <Breadcrumb>
      <BreadcrumbItem home href="/" />
      {#each pages as page}
        <BreadcrumbItem href={page.url}>{page.name}</BreadcrumbItem>
      {/each}
    </Breadcrumb>
  {/if}
  <h2 class="text-xl font-bold my-2">{title}</h2>
</div>
