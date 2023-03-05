<script lang="ts">
  import { Card } from "flowbite-svelte";
	import type { PageData } from "./$types";

  export let data: PageData;
  const annotations = [
    {
      id: 1,
      taskId: data.task.id,
      annotatorId: 1,
    },
  ];
  const annotationLabels = [
    {
      id: 1,
      annotationId: 1,
      datasetLabelId: data.datasetId,
      startOffset: 1,
      endOffset: 3,
    }
  ]
</script>

<div class="mt-5 mx-5">
  <div class="flex justify-center">
    <Card size="lg">
      <p>{data.task.content.lg}</p>
    </Card>
  </div>
</div>
