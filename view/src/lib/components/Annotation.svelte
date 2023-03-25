<script lang="ts">
  import type  { Category, Annotation } from "$lib/types";
  import CategorySelectMenu from "./CategorySelectMenu.svelte";

  export let categories: Category[];
  export let text: string;

  let selectedText = '';
  let selectedRange: Range | null = null;
  let selectedRects: DOMRectList | null = null;
  let showCategory = false;
  let annotations: Annotation[] = [];

  const clearSelect = () => {
    selectedText = '';
    selectedRange = null;
    selectedRects = null;
    showCategory = false;
  }

  const isOverlapping = (a: Range, b: Range) => {
    if (a.startOffset > b.startOffset && a.startOffset < b.endOffset) { return true };
    if (a.endOffset > b.startOffset && a.endOffset < b.endOffset) { return true };
    if (b.startOffset > a.startOffset && b.startOffset < a.endOffset) { return true };
    if (b.endOffset > a.startOffset && b.endOffset < a.endOffset) { return true };
    return false;
  }

  const handleMouseUp = () => {
    const selection = document.getSelection();
    if (selection === null || selection.toString().length === 0) {
      clearSelect();
      return;
    }
    const range = selection.getRangeAt(0);
    const rects = range.getClientRects();
    const isSomeOverlapping = annotations.some(annotation => isOverlapping(range, annotation.range))
    if (isSomeOverlapping) {
      clearSelect();
      return;
    }
    selectedText = selection.toString();
    selectedRange = range;
    selectedRects = rects;
    showCategory = true;
  }

  const onSelectCategory = (event: CustomEvent) => {
    const category = event.detail.category;
    if (selectedRange === null || selectedRects === null) {
      showCategory = false;
      return;
    }
    const newAnnotation: Annotation = {
      text: selectedText,
      range: selectedRange,
      rects: selectedRects,
      category: category.name,
      color: category.color,
    };
    annotations = [...annotations, newAnnotation];
    showCategory = false;
  }

  const getBorderStyle = (rect: DOMRect, borderColor: string) => {
    return `top: ${rect.bottom}px; left: ${rect.left}px; width: ${rect.width}px; border-color: ${borderColor};`
  }
</script>

<div class="m-4">
  <div class="bg-white p-4 border rounded w-full min-h-[200px] min-w-[600px]" on:mouseup={handleMouseUp}>
    <p>{text}</p>
    {#if annotations.length > 0}
      {#each annotations as annotation, i (i)}
        {#each annotation.rects as rect, j (j)}
          <div class="fixed border-b-2" style={getBorderStyle(rect, annotation.color)}>
            {#if j === 0}
              <span class="fixed">{annotation.category}</span>
            {/if}
          </div>
        {/each}
      {/each}
    {/if}
  </div>
  <CategorySelectMenu show={showCategory} categories={categories} rect={selectedRects ? selectedRects[0] : null} on:select={onSelectCategory} />
</div>
