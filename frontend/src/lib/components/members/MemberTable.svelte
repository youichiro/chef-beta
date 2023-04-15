<script lang="ts">
  import { Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell } from "flowbite-svelte";
  import type { Member } from "$lib/types/member-types"

  export let members: Member[];
</script>

<div class="m-4 border rounded">
  <Table hoverable={true}>
    <TableHead>
      <TableHeadCell>id</TableHeadCell>
      <TableHeadCell>name</TableHeadCell>
    </TableHead>
    <TableBody>
      {#each members as member (member.id)}
        <TableBodyRow>
          <TableBodyCell>{member.id}</TableBodyCell>
          <TableBodyCell>{member.name}</TableBodyCell>
        </TableBodyRow>
      {/each}
    </TableBody>
  </Table>
</div>
