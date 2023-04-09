<script lang="ts">
  import LabelSelectMenu from "$lib/components/LabelSelectMenu.svelte";
  import { getAnnotationTags, isOverlappingAnnotations } from "$lib/models/annotation";
  import { maxLabelNameLength } from "$lib/models/label";
  import type { RangeIndex, Label, Annotation, Span } from "$lib/types";
  import { onMount } from "svelte";

  export let text: string;
  export let labels: Label[];

  const textMarginRight = maxLabelNameLength(labels)
  let annotations: Annotation[] = []
  let selectedRangeIndex: RangeIndex | null = null;
  let menu: any = { show: false, top: null, left: null }
  $: spans = splitText(text, annotations)
  $: tags = getAnnotationTags(annotations)

  const splitText = (text: string, annotations: Annotation[]): Span[] => {
    return text.split("").map((char, index) => {
      const span: Span = { text: char, index: index, class: `span${index}` }
      if (!annotations || annotations.length === 0) {
        return span
      }
      const matchAnnotations = annotations.filter(annotation => annotation.rangeIndex.start <= index && index <= annotation.rangeIndex.end)
      if (matchAnnotations.length === 0) {
        return span
      }
      const matchAnnotation = matchAnnotations[0]
      const showLabel = index === matchAnnotation.rangeIndex.start
      return {
        text: char,
        index: index,
        class: `span${index} border-b-2 border-${matchAnnotation.label.color}`,
        annotation: matchAnnotation,
        showLabel,
      }
    })
  }

  const clearSelection = () => {
    selectedRangeIndex = null;
    menu = { show: false, top: null, left: null };
  }

  const handleMouseUp = () => {
    const selection = window.getSelection();
    if (selection === null || selection.toString().length === 0) {
      clearSelection()
      return;
    }
    // @ts-ignore
    const start = selection.anchorNode.parentNode.claim_order
    // @ts-ignore
    const end = selection.focusNode.parentNode.claim_order
    const rangeIndex: RangeIndex = { start, end }

    if (isOverlappingAnnotations(rangeIndex, annotations)) {
      clearSelection()
      return;
    }

    const range = selection.getRangeAt(0)
    const rects = range.getClientRects()
    const firstRect = rects[0]
    selectedRangeIndex = rangeIndex;
    menu = { show: true, top: firstRect.bottom, left: firstRect.left}
  }

  const onSelectLabel = (event: CustomEvent) => {
    const label = event.detail.label;
    if (selectedRangeIndex !== null) {
      const newAnnotation: Annotation = { label, rangeIndex: selectedRangeIndex };
      annotations = [...annotations, newAnnotation];
    }
    clearSelection()
  }

  const adjastSvgHeight = () => {
    const svg: any = document.getElementById('svg');
    const textElement: any = document.getElementById('text');
    const observer = new ResizeObserver(entries => {
      for (let entry of entries) {
        const height = entry.contentRect.height;
        svg.setAttribute('height', height + 20);
      }
    });
    observer.observe(textElement);
  }

  onMount(() => {
    adjastSvgHeight()
  })
</script>

<div class="m-4">
  <div class="bg-white p-4 border rounded" on:mouseup={handleMouseUp}>
    <svg id="svg" class="w-full h-full">
      <foreignObject width="100%" height="100%">
        <p id="text" style={`margin-right: ${textMarginRight}em; line-height: 3em;`} class="text-lg">
          {#each spans as span}
            <span class={span.class}>{span.text}</span>
          {/each}
        </p>
      </foreignObject>
      {#if tags.length > 0}
        {#each tags as tag}
          <text x={tag.x} y={tag.y} class={`select-none text-sm font-bold fill-${tag.label.color}`}>{tag.label.name}</text>
        {/each}
      {/if}
    </svg>
  </div>
  <LabelSelectMenu show={menu.show} labels={labels} top={menu.top} left={menu.left} on:select={onSelectLabel} on:close={() => clearSelection()} />
</div>
