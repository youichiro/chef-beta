<script lang="ts">
  import { Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell } from "flowbite-svelte";
  import type { Dataset } from "$lib/types/dataset-types"

  export let datasets: Dataset[];
</script>

<div class="m-4 border rounded">
  <Table hoverable={true}>
    <TableHead>
      <TableHeadCell>id</TableHeadCell>
      <TableHeadCell>name</TableHeadCell>
    </TableHead>
    <TableBody>
      {#each datasets as dataset (dataset.id)}
        <TableBodyRow>
          <TableBodyCell>{dataset.id}</TableBodyCell>
          <TableBodyCell>{dataset.name}</TableBodyCell>
        </TableBodyRow>
      {/each}
    </TableBody>
  </Table>
</div>
