export type Category = {
  value: string;
  name: string;
  color: string;
}

export type Annotation = {
  start: number;
  end: number;
  text: string;
  category: string;
  color: string;
  rect: DOMRect | null;
};
