<script lang="ts">
  import type { PageData } from "./$types";
  import PageTop from "$lib/components/PageTop.svelte";
  import { Spinner } from "flowbite-svelte";
  import { Tabs, TabItem } from 'flowbite-svelte';
  import DatasetTable from "$lib/components/datasets/DatasetTable.svelte";
  import { goto } from '$app/navigation';
  import { DatasetListSchema, type DatasetList, type Tab } from "$lib/types/dataset-types";
  import Pagination from "$lib/components/common/Pagination.svelte";
  import { ProjectSchema, type Project, Guideline, GuidelineSchema } from "$lib/types/project-types";

  export let data: PageData;
  let datasetList: DatasetList;
  let project: Project;
  let guideline: Guideline | null = null;

  const getProject = async (): Promise<Project> => {
    const response = await self.fetch(`http://localhost:8000/api/projects/${data.id}`);
    if (response.ok) {
      return response.json();
    } else {
      throw new Error(`status: ${response.status}, ${response.statusText}`);
    }
  };

  const getDatasetList = async (): Promise<DatasetList> => {
    const response = await self.fetch(`http://localhost:8000/api/projects/${data.id}/datasets?page=${data.page}&size=3`);
    if (response.ok) {
      return response.json();
    } else {
      throw new Error(`status: ${response.status}, ${response.statusText}`);
    }
  };

  const getGuideline = async (): Promise<Guideline | null> => {
    const response = await self.fetch(`http://localhost:8000/api/projects/${data.id}/guideline`)
    if (response.ok) {
      return response.json()
    } else {
      throw new Error(`status: ${response.status}, ${response.statusText}`);
    }
  }

  let promise = Promise.all([
    getProject().then(response => {
      project = ProjectSchema.parse(response);
    }),
    getDatasetList().then(response => {
      datasetList = DatasetListSchema.parse(response);
    }),
    getGuideline().then(response => {
      if (response !== null) {
        guideline = GuidelineSchema.parse(response);
      }
    })
  ]);

  const handleClickTab = async (tab: Tab) => {
    if (tab === null) {
      return
    }
    const queryParams = new URLSearchParams(location.search);
    queryParams.set('tab', tab);
    await goto(`?${queryParams.toString()}`);
  }
</script>

<style lang="postcss">
  .guideline {
    @apply m-8;
  }
</style>

<div>
  {#await promise}
    <div class="text-center mt-8">
      <Spinner />
    </div>
  {:then}
    <PageTop title={project.name} pages={[{name: 'projects', url: '/projects'}]} />
    <Tabs style="underline" defaultClass="flex flex-wrap space-x-2 bg-slate-50 pl-4" contentClass="">
      <TabItem open={data.tab === "datasets"} title="Datasets" on:click={() => handleClickTab("datasets")}>
        <DatasetTable datasets={datasetList.items} />
        <Pagination currentPage={data.page} lastPage={datasetList.pages} />
      </TabItem>
      <TabItem open={data.tab === "guideline"} title="Guideline" on:click={() => handleClickTab("guideline")}>
        <div class="guideline">
          {#if guideline !== null}
            <p>{guideline.content}</p>
          {:else}
            <p>😃</p>
          {/if}
        </div>
      </TabItem>
      <TabItem open={data.tab === "members"} title="Members" on:click={() => handleClickTab("members")}>
        <p>members</p>
      </TabItem>
    </Tabs>
  {:catch error}
    <p>error! {error}</p>
  {/await}
</div>

