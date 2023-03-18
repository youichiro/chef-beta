<script lang="ts">
  type Category = '名前' | '住所' | '電話番号';
  type Annotation = {
    start: number;
    end: number;
    text: string;
    category: Category;
  };

  let text = '私は小川耀一朗です';
  let selectedText = '';
  let selectedStart = 0;
  let selectedEnd = 0;
  let selectedCategory: Category | null;
  let showCategory = false;
  let annotations: Annotation[] = [];

  const categories: Category[] = ['名前', '住所', '電話番号'];

  const handleMouseUp = () => {
    const selection = document.getSelection();
    if (selection && selection.toString().length > 0) {
      selectedText = selection.toString();
      const range = selection.getRangeAt(0);
      selectedStart = range.startOffset;
      selectedEnd = range.endOffset;
      showCategory = true;
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

<div class="flex flex-col items-center">
  <h1 class="text-2xl mb-4">テキストアノテーション</h1>
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
  {#if selectedText}
    <div class="mt-4">
      選択されたテキスト: <strong>{selectedText}</strong><br>
      開始位置: {selectedStart}<br>
      終了位置: {selectedEnd}
    </div>
  {/if}
  {#if showCategory}
    <div class="mt-4">
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
  {#if annotations.length > 0}
    <div class="mt-4">
      <h2 class="text-xl mb-2">アノテーション:</h2>
      <ul>
        {#each annotations as annotation}
          <li>{annotation.text} - {annotation.category}</li>
        {/each}
      </ul>
    </div>
  {/if}
</div>
