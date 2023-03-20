<script lang="ts">
  import { Button } from "flowbite-svelte";

  type Category = {
      value: string;
      name: string;
      color: string;
  }
  export let categories: Category[];
  export let text: string;

  type Annotation = {
    start: number;
    end: number;
    text: string;
    category: string;
    color: string;
    rect: DOMRect | null;
  };

  let selectedText = '';
  let selectedStart = 0;
  let selectedEnd = 0;
  let selectedRect: DOMRect | null = null;
  let annotations: Annotation[] = [];
  let showCategory = false;
  $: modalStyle = selectedRect ? `top: ${selectedRect.bottom}px; left: ${selectedRect.left}px;` : "";

  const handleMouseUp = () => {
    const selection = document.getSelection();
    if (selection && selection.toString().length > 0) {
      selectedText = selection.toString();
      const range = selection.getRangeAt(0);
      selectedStart = range.startOffset;
      selectedEnd = range.endOffset;
      selectedRect = range.getBoundingClientRect();
      showCategory = true;
    } else {
      selectedText = '';
      selectedStart = selectedEnd = 0;
      selectedRect = null;
      showCategory = false;
    }
  }

  const handleClickCategory = (category: Category) => {
    const newAnnotation: Annotation = {
      start: selectedStart,
      end: selectedEnd,
      text: selectedText,
      category: category.name,
      color: category.color,
      rect: selectedRect,
    };
    annotations = [...annotations, newAnnotation];
    showCategory = false;
  }

  const annotationBorderStyle = (annotation: Annotation) => {
    return `top: ${annotation.rect?.bottom}px; left: ${annotation.rect?.left}px; width: ${annotation.rect?.width}px; border-color: ${annotation.color};`
  }

  const styles = {
    selectBtn: "border-none py-2 px-4 w-full hover:bg-slate-100 text-left"
  }
</script>

<div class="m-4">
  <div class="bg-white p-4 border rounded w-full min-h-[200px] min-w-[600px]" on:mouseup={handleMouseUp}>
    <p>{text}</p>
    {#if annotations.length > 0}
      {#each annotations as annotation, i (i)}
        <div class="fixed border-b-2" style={annotationBorderStyle(annotation)}>
          <span class="fixed">{annotation.category}</span>
        </div>
      {/each}
    {/if}
  </div>
  {#if showCategory}
    <div class="fixed bg-white my-2 z-20 border rounded shadow flex flex-col" style={modalStyle}>
      {#each categories as category}
        <Button color="alternative" size="sm" btnClass={styles.selectBtn} on:click={() => handleClickCategory(category)}>{category.name}</Button>
      {/each}
    </div>
  {/if}
</div>
