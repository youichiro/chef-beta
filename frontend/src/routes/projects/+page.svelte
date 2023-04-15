<script lang="ts">
  import PageTop from "$lib/components/PageTop.svelte";
  import ProjectTable from "$lib/components/projects/ProjectTable.svelte";
  import { Spinner } from "flowbite-svelte";
  import ProjectTablePagination from "$lib/components/common/Pagination.svelte";
  import type { PageData } from "./$types";
  import { ProjectListSchema } from "$lib/types/project-types";
  import type { ProjectList } from "$lib/types/project-types";

  export let data: PageData;
  let projectList: ProjectList;

  const getProjects = async () => {
    const response = await self.fetch(`http://localhost:8000/api/projects?page=${data.page}&size=3`);
    if (response.ok) {
      return response.json();
    } else {
      throw new Error(`status: ${response.status}, ${response.statusText}`);
    }
  };

  let promise = getProjects().then(response => {
    projectList = ProjectListSchema.parse(response);
  });
</script>

<PageTop title="Projects" />

<div>
  {#await promise}
    <div class="text-center mt-8">
      <Spinner />
    </div>
  {:then}
    {#if projectList.items.length === 0}
      <p>items empty.</p>
    {:else}
      <ProjectTable projects={projectList.items} />
      <ProjectTablePagination baseUrl="/projects" currentPage={data.page} lastPage={projectList.pages} />
    {/if}
  {:catch error}
    <p>error! {error}</p>
  {/await}
</div>
