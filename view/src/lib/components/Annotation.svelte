<script lang="ts">
  import type  { Category, Annotation, RangeIndex, Char } from "$lib/types";
  import CategorySelectMenu from "./LabelSelectMenu.svelte";

  export let categories: Category[];
  export let text: string;

  let selectedText = '';
  let selectedRangeIndex: RangeIndex | null = null;
  let selectedRects: DOMRectList | null = null;
  let showCategory = false;
  let annotations: Annotation[] = [];
  const maxCategoryLength = Math.max(...categories.map(category => category.name.length))
  $: charGroups = splitCharIndex(text.length, annotations)

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

  const splitCharIndex = (charNum: number, annotatons: Annotation[]) => {
    if (annotations.length === 0) {
      return [
        { type: "no-label", indexes: [...Array(charNum)].map((_, i) => i) }
      ]
    }
    const annotationIndexs = annotatons.map(annotation => createRangeArray(annotation.rangeIndex.start, annotation.rangeIndex.end))
    let hoge = []
    let current = 0
    annotationIndexs.forEach(annotationIndexArray => {
      if (annotationIndexArray[0] == current) {
        hoge.push({
          type: "label",
          indexes: annotationIndexArray,
          label: "名前",
        })
        current = annotationIndexArray.slice(-1)[0] + 1;
      } else {
        const num = annotationIndexArray[0] - current
        const betweenNums = [...Array(num)].map((_, i) => current + i)
        hoge.push({
          type: "no-label",
          indexes: betweenNums,
          label: "",
        })
        hoge.push({
          type: "label",
          indexes: annotationIndexArray,
          label: "名前",
        })
        current = annotationIndexArray.slice(-1)[0] + 1;
      }
    })
    if (current < charNum - 1) {
      const num = charNum - 1 - current
      const betweenNums = [...Array(num)].map((_, i) => current + i)
      hoge.push({
        type: "no-label",
        indexes: betweenNums,
        label: "",
      })
      current = charNum - 1
    }
    console.log(hoge)
    console.log(current)

    return hoge
  }

  const createRangeArray = (startNum: number, endNum: number): number[] => {
    let arr = [];
    for (let i = startNum; i <= endNum; i++) {
      arr.push(i);
    }
    return arr;
}
</script>

<div class="m-4">
  <div class="bg-white p-4 border rounded w-full min-h-[200px] min-w-[600px]" on:mouseup={handleMouseUp}>
    <p class="table flex-wrap" style={`margin-right: ${maxCategoryLength}em;`}>
      {#each charGroups as group, index (index)}
        {#if group.type == "no-label"}
          <span class="flex">
            {#each group.indexes as charIndex}
              <span>{text[charIndex]}</span>
            {/each}
          </span>
        {:else}
          <span class="flex flex-col">
            <span class="border-b-2 border-sky-500">{group.indexes.map(charIndex => text[charIndex]).join("")}</span>
            <span class="select-none">{group.label}</span>
          </span>
        {/if}
      {/each}
    </p>
  </div>
  <CategorySelectMenu show={showCategory} categories={categories} rect={selectedRects ? selectedRects[0] : null} on:select={onSelectCategory} />
</div>
