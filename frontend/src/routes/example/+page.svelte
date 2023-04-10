<script lang="ts">
  import PageTop from "$lib/components/PageTop.svelte";
  import Annotation from "$lib/components/annotations/Annotation.svelte";
  import type { Label } from "$lib/types";

  const text =
    "私は小川耀一朗です 私は小川耀一朗です 私は小川耀一朗です 私は小川耀一朗です 私は小川耀一朗です 私は小川耀一朗です 私は小川耀一朗です 私は小川耀一朗です 私は小川耀一朗です 私は小川耀一朗です 私は小川耀一朗です 私は小川耀一朗です";
  const labels: Label[] = [
    { name: "名前", color: "green-500" },
    { name: "メールアドレス", color: "orange-500" },
    { name: "住所", color: "blue-500" },
  ];
</script>

<PageTop title="Annotation" />

<Annotation {text} {labels} />
