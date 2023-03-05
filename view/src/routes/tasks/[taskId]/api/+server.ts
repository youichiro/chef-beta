import { json } from "@sveltejs/kit";

export const GET = async () => {
  const datasetId: number = 1; // TODO: URLから取得する
  const taskId: number = 1; // TODO: URLから取得する
  const task = await fetchTask(datasetId, taskId);
  const labels = await fetchLabels(datasetId);
  return json({ datasetId, task, labels })
}

const fetchTask = async (datasetId: number, taskId: number) => {
  const task = {
    taskId: taskId,
    datasetId: datasetId,
    number: 1,
    content: {
      sm: "テキスト テキスト",
      lg: "テキスト テキスト テキスト テキスト テキスト テキスト テキスト テキスト テキスト テキスト テキスト テキスト",
    }
  };
  return task
}

const fetchLabels = async (datasetId: number) => {
  const labels = [
    {
      id: 1,
      datasetId: datasetId,
      name: "名前",
      order: 1,
      color: "blue",
    },
    {
      id: 2,
      datasetId: datasetId,
      name: "住所",
      order: 2,
      color: "green",
    },
  ];
  return labels;
}
