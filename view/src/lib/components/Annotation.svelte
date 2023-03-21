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

  const onClickCategorySelectMenu = (event: CustomEvent) => {
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
  {#if showCategory}
    <CategorySelectMenu categories={categories} rect={selectedRect} on:click={onClickCategorySelectMenu} />
  {/if}
</div>


<!--
アノテーションを表示するための別のSvelteコンポーネントを作成する
アノテーションを表示するためのコンポーネント（例：AnnotationDisplay.svelte）を作成し、それを使用してアノテーションを表示することで、コードをより読みやすくできます。

関数の名前をより具体的にする
関数名をもう少し具体的にして、それぞれの関数がどのような目的で使用されているかを明確にすると良いでしょう。例えば、handleMouseUp を handleTextSelection に変更し、handleClickCategory を addAnnotation に変更するなどです。

コード内のマジックナンバーを避ける
マジックナンバー（この場合は min-h-[200px] や min-w-[600px] など）を定数として定義し、それを使用することでコードの保守性を向上させることができます。定数を変更するだけで、全体のスタイルが変更できるようになります。

コメントを追加してコードの説明を充実させる
各関数や変数の目的を説明するコメントを追加することで、他の開発者がコードを理解しやすくなります。

stylesにcssを書く
-->
