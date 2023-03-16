<script lang="ts">
  import { PaginationItem, ChevronLeft, ChevronRight } from "flowbite-svelte";
  import { ChevronDoubleLeft, ChevronDoubleRight } from "svelte-heros-v2";

  export let currentPage: number
  export let lastPage: number

  const firstPage = 1
  const previousPage = currentPage - 1 >= 1 ? currentPage - 1 : null
  const nextPage = currentPage + 1 <= lastPage ? currentPage + 1 : null

  let helper = {start: 1, end: 10, total: 100}
  const handleClickFirst = () => {
    window.location.href = `/examples?page=${firstPage}`
  };
  const handleClickPrevious = () => {
    if (previousPage !== null) {
      window.location.href = `/examples?page=${previousPage}`
    }
  };
  const handleClickNext = () => {
    if (nextPage !== null) {
      window.location.href = `/examples?page=${nextPage}`
    }
  };
  const handleClickLast = () => {
    window.location.href = `/examples?page=${lastPage}`
  };

  const styles = {
    paginationButton: {
      base: 'border-none text-gray-500 bg-white hover:bg-gray-100 hover:text-gray-700',
      prev: `border-none text-gray-500 bg-white ${previousPage ? 'hover:bg-gray-100 hover:text-gray-700' : 'cursor-not-allowed'}`,
      next: `border-none text-gray-500 bg-white ${nextPage ? 'hover:bg-gray-100 hover:text-gray-700' : 'cursor-not-allowed'}`,
    }
  }
</script>

<div class="flex items-center justify-end">
  <div class="text-sm text-gray-700 mr-4">
    <span>{helper.start} - {helper.end} of {helper.total}</span>
  </div>
  <div class="flex">
    <PaginationItem on:click={handleClickFirst} normalClass={styles.paginationButton.base}>
      <ChevronDoubleLeft />
    </PaginationItem>
    <PaginationItem on:click={handleClickPrevious} normalClass={styles.paginationButton.prev}>
      <ChevronLeft />
    </PaginationItem>
    <PaginationItem on:click={handleClickNext} normalClass={styles.paginationButton.next}>
      <ChevronRight />
    </PaginationItem>
    <PaginationItem on:click={handleClickLast} normalClass={styles.paginationButton.base}>
      <ChevronDoubleRight />
    </PaginationItem>
  </div>
</div>
