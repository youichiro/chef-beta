<script lang="ts">
  import { PaginationItem, ChevronLeft, ChevronRight } from "flowbite-svelte";
  import { ChevronDoubleLeft, ChevronDoubleRight } from "svelte-heros-v2";

  export let currentPage: number;
  export let lastPage: number;

  const firstPage = 1;
  const previousPage = currentPage - 1 >= 1 ? currentPage - 1 : null;
  const nextPage = currentPage + 1 <= lastPage ? currentPage + 1 : null;

  const handleClickFirst = () => {
    window.location.href = `/projects?page=${firstPage}`;
  };
  const handleClickPrevious = () => {
    if (previousPage !== null) {
      window.location.href = `/projects?page=${previousPage}`;
    }
  };
  const handleClickNext = () => {
    if (nextPage !== null) {
      window.location.href = `/projects?page=${nextPage}`;
    }
  };
  const handleClickLast = () => {
    window.location.href = `/projects?page=${lastPage}`;
  };

  const styles = {
    paginationButton: {
      base: "border-none text-gray-500 bg-white hover:bg-gray-100",
      prev: `border-none bg-white ${
        previousPage ? "text-gray-500 hover:bg-gray-100" : "text-gray-300 cursor-not-allowed"
      }`,
      next: `border-none bg-white ${nextPage ? "text-gray-500 hover:bg-gray-100" : "text-gray-300 cursor-not-allowed"}`,
    },
    paginationButtonIcon: "outline-none",
  };
</script>

<div class="flex items-center justify-end">
  <div class="text-sm text-gray-700 mr-4">
    <span>page {currentPage} of {lastPage}</span>
  </div>
  <div class="flex">
    <PaginationItem on:click={handleClickFirst} normalClass={styles.paginationButton.base}>
      <ChevronDoubleLeft class={styles.paginationButtonIcon} />
    </PaginationItem>
    <PaginationItem on:click={handleClickPrevious} normalClass={styles.paginationButton.prev}>
      <ChevronLeft class={styles.paginationButtonIcon} />
    </PaginationItem>
    <PaginationItem on:click={handleClickNext} normalClass={styles.paginationButton.next}>
      <ChevronRight class={styles.paginationButtonIcon} />
    </PaginationItem>
    <PaginationItem on:click={handleClickLast} normalClass={styles.paginationButton.base}>
      <ChevronDoubleRight class={styles.paginationButtonIcon} />
    </PaginationItem>
  </div>
</div>
