<script lang="ts">
  import type  { Category, Annotation } from "$lib/types";
  import CategorySelectMenu from "./CategorySelectMenu.svelte";

  export let categories: Category[];
  export let text: string;

  let selectedText = '';
  let selectedRange: Range | null = null;
  let selectedRect: DOMRect | null = null;
  let annotations: Annotation[] = [];
  let showCategory = false;

  const handleMouseUp = () => {
    const selection = document.getSelection();
    if (selection && selection.toString().length > 0) {
      const range = selection.getRangeAt(0);
      const rect = range.getBoundingClientRect();
      selectedText = selection.toString();
      selectedRange = range;
      selectedRect = rect;
      showCategory = true;
    } else {
      selectedText = '';
      selectedRange = null;
      selectedRect = null;
      showCategory = false;
    }
  }

  const onSelectCategory = (event: CustomEvent) => {
    const category = event.detail.category;
    if (selectedRange === null || selectedRect === null) {
      showCategory = false;
      return;
    }
    const newAnnotation: Annotation = {
      text: selectedText,
      range: selectedRange,
      rect: selectedRect,
      category: category.name,
      color: category.color,
      borderStyle: "",
    };
    newAnnotation.borderStyle = annotationBorderStyle(newAnnotation);
    annotations = [...annotations, newAnnotation];
    showCategory = false;
  }

  const annotationBorderStyle = (annotation: Annotation) => {
    let yOffset = 0;

    annotations.forEach(existingAnnotation => {
      if (isOverlapping(annotation.range, existingAnnotation.range)) {
        yOffset += 20;
      }
    })
    const top = annotation.rect ? annotation.rect.bottom + yOffset : 0
    return `top: ${top}px; left: ${annotation.rect?.left}px; width: ${annotation.rect?.width}px; border-color: ${annotation.color};`
  }

  const isOverlapping = (a: Range, b: Range) => {
    if (a.startOffset >= b.startOffset && a.startOffset <= b.endOffset) { return true };
    if (a.endOffset >= b.startOffset && a.endOffset <= b.endOffset) { return true };
    if (b.startOffset >= a.startOffset && b.startOffset <= a.endOffset) { return true };
    if (b.endOffset >= a.startOffset && b.endOffset <= a.endOffset) { return true };
    return false;
  }
</script>

<div class="m-4">
  <div class="bg-white p-4 border rounded w-full min-h-[200px] min-w-[600px]" on:mouseup={handleMouseUp}>
    <p>{text}</p>
    {#if annotations.length > 0}
      {#each annotations as annotation, i (i)}
        <div class="fixed border-b-2" style={annotation.borderStyle}>
          <span class="fixed">{annotation.category}</span>
        </div>
      {/each}
    {/if}
  </div>
  <CategorySelectMenu show={showCategory} categories={categories} rect={selectedRect} on:select={onSelectCategory} />
</div>
