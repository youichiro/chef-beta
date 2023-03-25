export type Category = {
  value: string;
  name: string;
  color: string;
}

export type Annotation = {
  text: string;
  range: Range;
  rect: DOMRect;
  category: string;
  color: string;
  borderStyle: string;
};
