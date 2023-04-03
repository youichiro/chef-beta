<script lang="ts">
  const text = "私は小川耀一朗です"
  const labels = [
    { name: "名前", color: "blue" },
    { name: "メールアドレス", color: "orange" },
  ]
  let annotations: any[] = []
  $: chars = splitText(text, annotations)
  $: tags = getTags(annotations)

  const splitText = (text: string, annotations: any[]) => {
    return text.split("").map((char, index) => {
      const span = { text: char, index: index, className: `span${index}` }
      if (!annotations || annotations.length === 0) {
        return span
      }
      const matchAnnotations = annotations.filter(annotation => annotation.startIndex <= index && index <= annotation.endIndex)
      if (matchAnnotations.length === 0) {
        return span
      }
      const matchAnnotation = matchAnnotations[0]
      const showLabel = index === matchAnnotation.startIndex
      return {
        text: char,
        index: index,
        className: `span${index} border-b-2 border-blue-500`,
        annotation: matchAnnotation,
        showLabel,
      }
    })
  }

  const getTags = (annotations: any[]) => {
    if (!annotations || annotations.length === 0) {
      return []
    }
    const tags = annotations.map(annotation => {
      const span = getSpan(`span${annotation.startIndex}`)
      if (!span) {
        return null
      }
      console.log(span)
      return { x: span.left, y: span.height + 22, labelName: annotation.label.name }
    }).filter(item => item)
    return tags
  }

  const getSpan = (className: string) => {
    const spanElms = document.getElementsByClassName(className) as HTMLCollectionOf<HTMLSpanElement>;
    if (!spanElms || spanElms.length === 0) {
      return
    }
    const span = spanElms[0];
    return {
      top: span.offsetTop,
      left: span.offsetLeft,
      width: span.offsetWidth,
      height: span.offsetHeight,
    }
  }

  const handleMouseUp = () => {
    const selection = window.getSelection();
    if (selection === null || selection.toString().length === 0) {
      return;
    }
    // @ts-ignore
    const startIndex = selection.anchorNode.parentNode.claim_order
    // @ts-ignore
    const endIndex = selection.focusNode.parentNode.claim_order
    const newAnnotation = { label: labels[0], startIndex, endIndex }
    annotations = [...annotations, newAnnotation]
  }

</script>

<div class="m-4">
  <div class="relation bg-white p-4 border rounded w-full min-h-[200px] min-w-[400px]">
    <svg class="w-full">
      <g>
        <foreignObject width="100%" height="100%">
          <p on:mouseup={handleMouseUp}>
            {#each chars as char}
              <span class={char.className}>{char.text}</span>
            {/each}
          </p>
        </foreignObject>
        <g>
          {#if tags.length > 0}
            {#each tags as tag}
              <text x={tag?.x} y={tag?.y} class="select-none">{tag?.labelName}</text>
            {/each}
          {/if}
        </g>
      </g>
    </svg>
  </div>
</div>
