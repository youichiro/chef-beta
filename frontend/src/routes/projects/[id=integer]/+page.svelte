<script lang="ts">
  import type { PageData } from "./$types";
  import PageTop from "$lib/components/PageTop.svelte";
  import { Spinner } from "flowbite-svelte";
  import { ProjectDetailSchema } from "$lib/types/project-types";
  import type { ProjectDetail } from "$lib/types/project-types";
  import { Tabs, TabItem } from 'flowbite-svelte';
  import DatasetTable from "$lib/components/datasets/DatasetTable.svelte";

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
</script>

<PageTop title="Project Detail" pages={[{name: 'projects', url: '/projects'}]} />

<div>
  {#await promise}
    <div class="text-center mt-8">
      <Spinner />
    </div>
  {:then}
    <Tabs style="underline">
      <TabItem open title="Datasets">
        <DatasetTable datasets={projectDetail.datasets} />
      </TabItem>
      <TabItem title="Guideline">
        <p>{projectDetail.guideline?.content}</p>
      </TabItem>
      <TabItem title="Members">
        <p>members</p>
      </TabItem>
    </Tabs>
  {:catch error}
    <p>error! {error}</p>
  {/await}
</div>

