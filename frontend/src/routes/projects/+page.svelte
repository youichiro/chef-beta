<script lang="ts">
  import PageTop from "$lib/components/PageTop.svelte";
  import ProjectTable from "$lib/components/projects/ProjectTable.svelte";
  import { Spinner } from "flowbite-svelte";
  import ProjectTablePagination from "$lib/components/projects/ProjectTablePagination.svelte";
  import type { PageData } from "./$types";
  import { ProjectListResponse } from "$lib/types/project-types";

  export let data: PageData;

  const getProjects = async () => {
    const response = await self.fetch(`http://localhost:8000/api/projects?page=${data.page}&size=3`);
    if (response.ok) {
      return response.json();
    } else {
      throw new Error(`status: ${response.status}, ${response.statusText}`);
    }
  };

  let promise = getProjects();
</script>

<PageTop title="Projects" />

<div>
  {#await promise}
    <div class="text-center mt-8">
      <Spinner />
    </div>
  {:then response}
    {#if response.items.length === 0}
      <p>items empty.</p>
    {:else}
      <ProjectTable projects={ProjectListResponse.parse(response).items} />
      <ProjectTablePagination currentPage={data.page} lastPage={ProjectListResponse.parse(response).pages} />
    {/if}
  {:catch error}
    <p>error! {error}</p>
  {/await}
</div>
