<script lang="ts">
  import type { PageData } from "./$types";
  import PageTop from "$lib/components/PageTop.svelte";
  import { Spinner } from "flowbite-svelte";
  import { ProjectDeatil } from "$lib/types/project-types";

  export let data: PageData;

  const getProjectDetail = async () => {
    const response = await self.fetch(`http://localhost:8000/api/projects/${data.id}`);
    if (response.ok) {
      return response.json();
    } else {
      throw new Error(`status: ${response.status}, ${response.statusText}`);
    }
  };

  let promise = getProjectDetail();
</script>

<PageTop title="Project Detail" />

<div>
  {#await promise}
    <div class="text-center mt-8">
      <Spinner />
    </div>
  {:then response}
    {ProjectDeatil.parse(response)}
  {:catch error}
    <p>error! {error}</p>
  {/await}
</div>

