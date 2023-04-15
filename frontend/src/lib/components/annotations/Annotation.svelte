<script lang="ts">
  import LabelSelectMenu from "$lib/components/annotations/LabelSelectMenu.svelte";
  import { getAnnotationTags, getMatchAnnotation, isOverlappingAnnotations } from "$lib/models/annotation";
  import { maxLabelNameLength } from "$lib/models/label";
  import type { RangeIndex, Label, Annotation, Span, LabelSelectMenuOffset } from "$lib/types/annotation-types";
  import { Tooltip } from "flowbite-svelte";
  import { onMount } from "svelte";
  import { ArrowPath } from "svelte-heros-v2";

  export let text: string;
  export let labels: Label[];

  const textMarginRight = maxLabelNameLength(labels);
  let annotations: Annotation[] = [];
  let selectedRangeIndex: RangeIndex | null = null;
  let menu: LabelSelectMenuOffset | null = null;

  $: spans = splitTextToSpans(text, annotations);
  $: tags = getAnnotationTags(annotations);

  onMount(() => {
    adjustSvgHeight();
  });

  const adjustSvgHeight = () => {
    const svg = document.getElementById("svg");
    const text = document.getElementById("text");
    if (svg === null || text === null) {
      return;
    }
    const observer = new ResizeObserver((entries) => {
      for (let entry of entries) {
        const height = entry.contentRect.height;
        svg.setAttribute("height", `${height + 20}`);
      }
    });
    observer.observe(text);
  };

  const splitTextToSpans = (text: string, annotations: Annotation[]): Span[] => {
    return text.split("").map((char, index) => {
      const span: Span = { text: char, index: index, class: `span${index}` };
      const matchAnnotation = getMatchAnnotation(index, annotations);
      if (matchAnnotation === null) {
        return span;
      } else {
        return {
          ...span,
          class: `span${index} border-b-2 border-${matchAnnotation.label.color}`,
        };
      }
    });
  };

  const clearSelection = () => {
    selectedRangeIndex = null;
    menu = null;
  };

  const handleMouseUp = () => {
    const selection = window.getSelection();
    if (selection === null || selection.toString().length === 0) {
      clearSelection();
      return;
    }
    // @ts-ignore
    const start = selection.anchorNode.parentNode.claim_order;
    // @ts-ignore
    const end = selection.focusNode.parentNode.claim_order;
    const rangeIndex: RangeIndex = { start, end };

    if (isOverlappingAnnotations(rangeIndex, annotations)) {
      clearSelection();
      return;
    }

    const range = selection.getRangeAt(0);
    const rects = range.getClientRects();
    const firstRect = rects[0];
    selectedRangeIndex = rangeIndex;
    menu = { top: firstRect.bottom, left: firstRect.left };
  };

  const onSelectLabel = (event: CustomEvent) => {
    const label = event.detail.label;
    if (selectedRangeIndex !== null) {
      const id = annotations.length === 0 ? 0 : Math.max(...(annotations.map(annotation => annotation.id))) + 1
      const newAnnotation: Annotation = { id, label, rangeIndex: selectedRangeIndex };
      annotations = [...annotations, newAnnotation];
    }
    clearSelection();
  };

  const handleKeyDownTag = (event: KeyboardEvent) => {
    if (event.key !== 'Backspace') {
      return
    }
    // @ts-ignore
    const annotationId: number = Number(event.target.dataset.value);
    // remove annotation
    annotations = [...annotations.filter(annotation => annotation.id !== annotationId)]
  }

  const resetAnnotatoins = () => {
    if (annotations.length === 0) {
      return;
    }
    if (window.confirm("reset annotations.")) {
      annotations = [];
    }
  }

  const handleClickReset = () => {
    resetAnnotatoins()
  }

  const handleWindowKeyDown = (event: KeyboardEvent) => {
    const key = event.key
    switch (key) {
      case 'c':
        resetAnnotatoins()
        break;
    }
  }
</script>

<style>
  text:focus {
    outline: 1px solid skyblue;
  }
</style>

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
      {#each tags as tag}
        <text x={tag.x} y={tag.y} data-value={tag.annotation.id} class={`select-none cursor-pointer text-sm font-bold fill-${tag.annotation.label.color}`} tabIndex="0" on:keydown={handleKeyDownTag}>
          {tag.annotation.label.name}
        </text>
      {/each}
    </svg>
    <div class="flex justify-end">
      <ArrowPath color="gray" on:click={handleClickReset} />
      <Tooltip>type "c" to reset all annotation.</Tooltip>
    </div>
  </div>
  {#if menu !== null}
    <LabelSelectMenu
      {labels}
      top={menu?.top}
      left={menu?.left}
      on:select={onSelectLabel}
      on:close={() => clearSelection()}
    />
  {/if}
</div>

<svelte:window on:keydown={handleWindowKeyDown} />

<!--
TODO: ラベルを選択したら、backspaceで削除できることをガイドしたい
-->
