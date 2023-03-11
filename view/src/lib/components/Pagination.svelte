<script lang="ts">
  import { PaginationItem, ChevronLeft, ChevronRight } from "flowbite-svelte";
  import { ChevronDoubleLeft, ChevronDoubleRight } from "svelte-heros-v2";

  let helper = {start: 1, end: 10, total: 100}
  const first = () => {
    alert('first()');
  };
  const previous = () => {
    alert('previous()');
  };
  const next = () => {
    alert('next()');
  };
  const last = () => {
    alert('last()');
  };
</script>

<div class="flex items-center justify-end">
  <div class="text-sm text-gray-700 mr-4">
    <span>{helper.start} - {helper.end} of {helper.total}</span>
  </div>
  <div class="flex">
    <PaginationItem on:clint={first}>
      <ChevronDoubleLeft />
    </PaginationItem>
    <PaginationItem on:clint={previous}>
      <ChevronLeft />
    </PaginationItem>
    <PaginationItem on:click={next}>
      <ChevronRight />
    </PaginationItem>
    <PaginationItem on:click={last}>
      <ChevronDoubleRight />
    </PaginationItem>
  </div>
</div>
