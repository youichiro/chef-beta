<script lang="ts">
  import type { PageData } from "./$types";
  import PageTop from "$lib/components/PageTop.svelte";
  import { Spinner } from "flowbite-svelte";
  import { ProjectDetailSchema } from "$lib/types/project-types";
  import type { ProjectDetail } from "$lib/types/project-types";
  import { Tabs, TabItem } from 'flowbite-svelte';
  import DatasetTable from "$lib/components/datasets/DatasetTable.svelte";
  import Pagination from "$lib/components/common/Pagination.svelte";
  import { goto } from '$app/navigation';
  import type { Tab } from "$lib/types/dataset-types";

  export let data: PageData;
  let projectDetail: ProjectDetail;

  const getProjectDetail = async () => {
    const response = await self.fetch(`http://localhost:8000/api/projects/${data.id}`);
    if (response.ok) {
      return response.json();
    } else {
      throw new Error(`status: ${response.status}, ${response.statusText}`);
    }
  };

  let promise = getProjectDetail().then(response => {
    projectDetail = ProjectDetailSchema.parse(response);
  });

  const handleClickTab = async (tab: Tab) => {
    if (tab === null) {
      return
    }
    const queryParams = new URLSearchParams(location.search);
    queryParams.set('tab', tab);
    await goto(`?${queryParams.toString()}`);
  }
</script>

<PageTop title="Project Detail" pages={[{name: 'projects', url: '/projects'}]} />

<div>
  {#await promise}
    <div class="text-center mt-8">
      <Spinner />
    </div>
  {:then}
    <Tabs style="underline" defaultClass="flex flex-wrap space-x-2 bg-slate-50 pl-4" contentClass="">
      <TabItem open={data.tab === "datasets" || data.tab === null} title="Datasets" on:click={() => handleClickTab("datasets")}>
        <DatasetTable datasets={projectDetail.datasets} />
      </TabItem>
      <TabItem open={data.tab === "guideline"} title="Guideline" on:click={() => handleClickTab("guideline")}>
        <p>{projectDetail.guideline?.content}</p>
      </TabItem>
      <TabItem open={data.tab === "members"} title="Members" on:click={() => handleClickTab("members")}>
        <p>members</p>
      </TabItem>
    </Tabs>
  {:catch error}
    <p>error! {error}</p>
  {/await}
</div>

