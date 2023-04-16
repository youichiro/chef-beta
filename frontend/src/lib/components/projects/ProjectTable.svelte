<script lang="ts">
  import { A, Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell } from "flowbite-svelte";
  import type { Project } from "$lib/types/project-types";

  export let projects: Project[];
</script>

<div class="m-4 border rounded">
  <Table hoverable={true}>
    <TableHead>
      <TableHeadCell>id</TableHeadCell>
      <TableHeadCell>name</TableHeadCell>
      <TableHeadCell>project type</TableHeadCell>
    </TableHead>
    <TableBody>
      {#each projects as project (project.id)}
        <TableBodyRow>
          <TableBodyCell>{project.id}</TableBodyCell>
          <TableBodyCell><A href={`/projects/${project.id}?tab=datasets`}>{project.name}</A></TableBodyCell>
          <TableBodyCell>{project.project_type.name}</TableBodyCell>
        </TableBodyRow>
      {/each}
    </TableBody>
  </Table>
</div>
