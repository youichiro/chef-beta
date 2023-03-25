export type Category = {
  value: string;
  name: string;
  color: string;
}

export type Annotation = {
  text: string;
  range: Range;
  rects: DOMRectList;
  category: string;
  color: string;
  startIndex: number;
  endIndex: number;
};
