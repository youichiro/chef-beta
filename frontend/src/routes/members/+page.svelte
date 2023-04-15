<script lang="ts">
  import PageTop from "$lib/components/PageTop.svelte";
  import { Spinner } from "flowbite-svelte";
  import type { PageData } from "./$types";
  import MemberTable from "$lib/components/members/MemberTable.svelte";
  import { MemberListResponse } from "$lib/types/member-types";
  import Pagination from "$lib/components/common/Pagination.svelte";

  export let data: PageData;

  const getMembers = async () => {
    const response = await self.fetch(`http://localhost:8000/api/members?page=${data.page}&size=3`);
    if (response.ok) {
      return response.json();
    } else {
      throw new Error(`status: ${response.status}, ${response.statusText}`);
    }
  };

  let promise = getMembers();
</script>

<PageTop title="Members" />

<div>
  {#await promise}
    <div class="text-center mt-8">
      <Spinner />
    </div>
  {:then response}
    {#if response.items.length === 0}
      <p>items empty.</p>
    {:else}
      <MemberTable members={MemberListResponse.parse(response).items} />
      <Pagination baseUrl="/members" currentPage={data.page} lastPage={MemberListResponse.parse(response).pages} />
    {/if}
  {:catch error}
    <p>error! {error}</p>
  {/await}
</div>
