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
    if (selection === null || selection.toString().length === 0) {
      selectedText = '';
      selectedRange = null;
      selectedRect = null;
      showCategory = false;
      return;
    }
    const range = selection.getRangeAt(0);
    const rect = range.getBoundingClientRect();

    const isSomeOverlapping = annotations.some(annotation => isOverlapping(range, annotation.range))
    if (isSomeOverlapping) {
      selectedText = '';
      selectedRange = null;
      selectedRect = null;
      showCategory = false;
      return;
    }

    selectedText = selection.toString();
    selectedRange = range;
    selectedRect = rect;
    showCategory = true;
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
      borderStyle: annotationBorderStyle(selectedRange, selectedRect, category.color),
    };
    annotations = [...annotations, newAnnotation];
    showCategory = false;
  }

  const annotationBorderStyle = (range: Range, rect: DOMRect, color: string) => {
    let yOffset = 0;

    annotations.forEach(existingAnnotation => {
      if (isOverlapping(range, existingAnnotation.range)) {
        yOffset += 20;
      }
    })
    return `top: ${rect.bottom + yOffset}px; left: ${rect.left}px; width: ${rect.width}px; border-color: ${color};`
  }

  const isOverlapping = (a: Range, b: Range) => {
    if (a.startOffset > b.startOffset && a.startOffset < b.endOffset) { return true };
    if (a.endOffset > b.startOffset && a.endOffset < b.endOffset) { return true };
    if (b.startOffset > a.startOffset && b.startOffset < a.endOffset) { return true };
    if (b.endOffset > a.startOffset && b.endOffset < a.endOffset) { return true };
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
