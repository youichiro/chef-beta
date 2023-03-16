<script lang="ts">
  import { Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell } from "flowbite-svelte";
  export let key: string
  export let rows: any[]
  const columns = Object.keys(rows[0])
</script>

<Table hoverable={true}>
  <TableHead>
    {#each columns as column}
      <TableHeadCell>{column}</TableHeadCell>
    {/each}
  </TableHead>
  <TableBody>
    {#each rows as row (row[key])}
      <TableBodyRow>
        {#each Object.values(row) as value}
          <TableBodyCell>{value}</TableBodyCell>
        {/each}
      </TableBodyRow>
    {/each}
  </TableBody>
</Table>

