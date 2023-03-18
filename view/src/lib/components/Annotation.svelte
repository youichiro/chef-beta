<script lang="ts">
  export let categories: string[];
  export let text: string;

  type Annotation = {
    start: number;
    end: number;
    text: string;
    category: string;
  };

  let selectedText = '';
  let selectedStart = 0;
  let selectedEnd = 0;
  let selectedCategory: string | null;
  let annotations: Annotation[] = [];
  let showCategory = false;
  let modalStyle = '';

  const handleMouseUp = () => {
    const selection = document.getSelection();
    if (selection && selection.toString().length > 0) {
      selectedText = selection.toString();
      const range = selection.getRangeAt(0);
      selectedStart = range.startOffset;
      selectedEnd = range.endOffset;
      showCategory = true;
      // カテゴリ選択モーダルの表示位置を取得
      const rect = range.getBoundingClientRect();
      modalStyle = `top: ${rect.bottom}px; left: ${rect.left}px;`;
    } else {
      selectedText = '';
      selectedStart = selectedEnd = 0;
      showCategory = false;
    }
  }

  const addAnnotation = () => {
    if (selectedCategory === null) {
      return
    }
    const newAnnotation: Annotation = {
      start: selectedStart,
      end: selectedEnd,
      text: selectedText,
      category: selectedCategory,
    };
    annotations = [...annotations, newAnnotation];
    selectedCategory = null;
    showCategory = false;
  }
</script>

<style lang="postcss">
  .text-area {
    @apply bg-white p-4 border rounded w-full min-h-[200px];
  }
</style>

<div class="m-4">
  <div class="text-area" on:mouseup={handleMouseUp}>
    <p class="select-text">{text}</p>
    {#if annotations.length > 0}
      {#each annotations as annotation, i (i)}
        <div>
          {#each Array(text.length) as _, charIndex (charIndex)}
            {#if annotation.start <= charIndex && charIndex < annotation.end}
              <div class="inline-block border-t-2 border-sky-500 relative">
                <span class="text-white select-none">{text[charIndex]}</span>
                {#if charIndex === annotation.start}
                  <div class="inline-block absolute top-0 left-0 bg-white z-10">
                    <span class="whitespace-nowrap select-none">{annotation.category}</span>
                  </div>
                {/if}
              </div>
            {:else}
              <span class="invisible">{text[charIndex]}</span>
            {/if}
          {/each}
        </div>
      {/each}
    {/if}
  </div>
  {#if showCategory}
    <div class="fixed bg-white p-4 shadow-lg rounded z-20" style={modalStyle}>
      <label for="category">カテゴリ:</label>
      <select id="category" bind:value={selectedCategory}>
        <option value="">選択してください</option>
        {#each categories as cat}
          <option value={cat}>{cat}</option>
        {/each}
      </select>
      <button on:click={addAnnotation} disabled={!selectedCategory}>アノテーションを追加</button>
    </div>
  {/if}
</div>
