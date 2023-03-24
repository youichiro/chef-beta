<script lang="ts">
  import type  { Category, Annotation } from "$lib/types";
  import CategorySelectMenu from "./CategorySelectMenu.svelte";

  export let categories: Category[];
  export let text: string;

  let selectedText = '';
  let selectedStart = 0;
  let selectedEnd = 0;
  let selectedRect: DOMRect | null = null;
  let annotations: Annotation[] = [];
  let showCategory = false;

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

  const onSelectCategory = (event: CustomEvent) => {
    const category = event.detail.category;
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
  <CategorySelectMenu show={showCategory} categories={categories} rect={selectedRect} on:select={onSelectCategory} />
</div>
