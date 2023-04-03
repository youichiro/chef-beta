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
  // $: chars = textChars(annotations)
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
    console.log(range)
    console.log(range.startContainer.parentNode?.claim_order)
    console.log(range.endContainer.parentNode?.claim_order)
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

  // const textChars = (annotations: Annotation[]): Char[] => {
  //   return text.split("").map((char, index) => {
  //     const charAnnotations = annotations.filter(annotation => annotation.rangeIndex.start <= index && index <= annotation.rangeIndex.end)
  //     if (charAnnotations.length === 0) {
  //       return { text: char, style: '', categoryName: '' }
  //     }
  //     const annotation =charAnnotations[0];
  //     const style = `border-bottom: 2px solid ${annotation.color};`;
  //     if (index !== annotation.rangeIndex.start) {
  //       return { text: char, style, categoryName: '' }
  //     }
  //     return { text: char, style, categoryName: annotation.category }
  //   })
  // }

  const splitCharIndex = (charNum: number, annotatons: Annotation[]) => {
    if (annotations.length === 0) {
      return [
        { type: "no-label", indexes: [...Array(charNum)].map((_, i) => i) }
      ]
    }
    const annotationIndexs = annotatons.map(annotation => createRangeArray(annotation.rangeIndex.start, annotation.rangeIndex.end))
    console.log(annotations)
    console.log(annotationIndexs)
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

<style>
  .hidden {
    display: hidden;
  }
</style>

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
        <!-- <span class="flex flex-col">
          <span style={char.style}>{char.text}</span>
          <span class:hidden="{char.categoryName === ''}" class="select-none">{char.categoryName}</span>
        </span> -->
      {/each}
    </p>
    <!-- {#if annotations.length > 0}
      {#each annotations as annotation, i (i)}
        {#each annotation.rects as rect, j (j)}
          <div class="absolute border-b-2" style={`top: ${rect.bottom}px; left: ${rect.left}px;`}>
            {#if j === 0}
              <span class="fixed">{annotation.category}</span>
            {/if}
          </div>
        {/each}
      {/each}
    {/if} -->
  </div>
  <CategorySelectMenu show={showCategory} categories={categories} rect={selectedRects ? selectedRects[0] : null} on:select={onSelectCategory} />
</div>
