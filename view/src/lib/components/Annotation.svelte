<script lang="ts">
  import type  { Category, Annotation, RangeIndex, Char } from "$lib/types";
  import CategorySelectMenu from "./CategorySelectMenu.svelte";

  export let categories: Category[];
  export let text: string;

  let selectedText = '';
  let selectedRangeIndex: RangeIndex | null = null;
  let selectedRects: DOMRectList | null = null;
  let showCategory = false;
  let annotations: Annotation[] = [];
  const maxCategoryLength = Math.max(...categories.map(category => category.name.length))
  $: chars = textChars(annotations)


  const clearSelect = () => {
    selectedText = '';
    selectedRangeIndex = null;
    selectedRects = null;
    showCategory = false;
  }

  const isOverlapping = (a: RangeIndex, b: RangeIndex) => {
    if (a.start >= b.start && a.start <= b.end) { return true };
    if (a.end >= b.start && a.end <= b.end) { return true };
    if (b.start >= a.start && b.start <= a.end) { return true };
    if (b.end >= a.start && b.end <= a.end) { return true };
    return false;
  }

  const handleMouseUp = () => {
    const selection = window.getSelection();
    if (selection === null || selection.toString().length === 0) {
      clearSelect();
      return;
    }
    const range = selection.getRangeAt(0);
    // @ts-ignore
    const startIndex = range.startContainer.parentNode?.claim_order
    // @ts-ignore
    const endIndex = range.endContainer.parentNode?.claim_order
    const rangeIndex: RangeIndex = { start: startIndex, end: endIndex }

    const isSomeOverlapping = annotations.some(annotation => isOverlapping(rangeIndex, annotation.rangeIndex))
    if (isSomeOverlapping) {
      clearSelect();
      return;
    }
    selectedText = selection.toString();
    selectedRangeIndex = rangeIndex;
    selectedRects = range.getClientRects();
    showCategory = true;
  }

  const onSelectCategory = (event: CustomEvent) => {
    const category = event.detail.category;
    if (selectedRects === null || selectedRangeIndex === null) {
      showCategory = false;
      return;
    }

    const newAnnotation: Annotation = {
      text: selectedText,
      rangeIndex: selectedRangeIndex,
      rects: selectedRects,
      category: category.name,
      color: category.color,
    };
    annotations = [...annotations, newAnnotation];
    showCategory = false;
  }

  const textChars = (annotations: Annotation[]): Char[] => {
    return text.split("").map((char, index) => {
      const charAnnotations = annotations.filter(annotation => annotation.rangeIndex.start <= index && index <= annotation.rangeIndex.end)
      if (charAnnotations.length === 0) {
        return { text: char, style: '' }
      }
      const annotation =charAnnotations[0];
      const borderStyle = `border-bottom: 2px solid ${annotation.color};`;
      return { text: char, style: borderStyle }
    })
  }
</script>

<div class="m-4">
  <div class="bg-white p-4 border rounded w-full min-h-[200px] min-w-[600px]" on:mouseup={handleMouseUp}>
    <p style={`margin-right: ${maxCategoryLength}em;`}>
      {#each chars as char, index (index)}
        <span style={char.style}>{char.text}</span>
      {/each}
    </p>
    {#if annotations.length > 0}
      {#each annotations as annotation, i (i)}
        {#each annotation.rects as rect, j (j)}
          <div class="absolute border-b-2" style={`top: ${rect.bottom}px; left: ${rect.left}px;`}>
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
