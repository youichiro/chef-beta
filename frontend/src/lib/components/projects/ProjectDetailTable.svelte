<script lang="ts">
  import type { Project } from "$lib/types/project-types";
  import { Table, TableBody, TableBodyCell, TableBodyRow } from "flowbite-svelte";

  export let project: Project;
</script>

<div class="m-4 border rounded">
  <Table>
    <TableBody>
      <TableBodyRow>
        <TableBodyCell>id</TableBodyCell>
        <TableBodyCell>{project.id}</TableBodyCell>
      </TableBodyRow>
      <TableBodyRow>
        <TableBodyCell>name</TableBodyCell>
        <TableBodyCell>{project.name}</TableBodyCell>
      </TableBodyRow>
      <TableBodyRow>
        <TableBodyCell>project type</TableBodyCell>
        <TableBodyCell>{project.project_type.name}</TableBodyCell>
      </TableBodyRow>
    </TableBody>
  </Table>
</div>
