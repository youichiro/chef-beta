import { json } from '@sveltejs/kit';

export const GET = async () => {
  const projects = await fetchProjects();
  return json({projects});
}

const fetchProjects = async () => {
  const projects = [
    {
      id: 1,
      name: "個人情報アノテーション",
      description: "これは個人情報のアノテーションを行うプロジェクトです",
    },
    {
      id: 2,
      name: "感情分類アノテーション",
      description: "これは感情分類のアノテーションを行うプロジェクトです",
    }
  ]
  return projects;
}
