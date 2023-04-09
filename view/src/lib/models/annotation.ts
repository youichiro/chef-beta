import type { Annotation, AnnotationTag, RangeIndex } from "$lib/types";
import { nonNullable } from "$lib/utils";


export const getAnnotationTags = (annotations: Annotation[]): AnnotationTag[] => {
  // アノテーションからタグの位置を計算して返す
  if (annotations.length === 0) {
    return []
  }
  const tags = annotations.map(annotation => {
    const startIndexSpanClass = `span${annotation.rangeIndex.start}`;
    const spanElms = document.getElementsByClassName(startIndexSpanClass) as HTMLCollectionOf<HTMLSpanElement>;
    if (!spanElms || spanElms.length === 0) {
      return null;
    }
    const spanElm = spanElms[0];
    const tag: AnnotationTag = { x: spanElm.offsetLeft, y: spanElm.offsetTop + 40, label: annotation.label }
    return tag
  }).filter(nonNullable)
  return tags
}


export const isOverlappingAnnotations = (rangeIndex: RangeIndex, annotations: Annotation[]): boolean => {
  const isOverlappingIndex = (a: RangeIndex, b: RangeIndex): boolean => {
    // RangeIndexを比較し、範囲が重なっているかどうかを返す
    if (a.start >= b.start && a.start <= b.end) { return true };
    if (a.end >= b.start && a.end <= b.end) { return true };
    if (b.start >= a.start && b.start <= a.end) { return true };
    if (b.end >= a.start && b.end <= a.end) { return true };
    return false;
  }
  return annotations.some(annotation => isOverlappingIndex(rangeIndex, annotation.rangeIndex))
}


export const getMatchAnnotation = (index: number, annotations: Annotation[]): Annotation | null => {
  if (annotations.length === 0) {
    return null
  }
  const matchAnnotations = annotations.filter(annotation => annotation.rangeIndex.start <= index && index <= annotation.rangeIndex.end)
  if (matchAnnotations.length === 0) {
    return null
  }
  const matchAnnotation = matchAnnotations[0]
  return matchAnnotation;
}
