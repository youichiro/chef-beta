export type Category = {
  value: string;
  name: string;
  color: string;
}

export type RangeIndex = {
  start: number,
  end: number,
}

export type Annotation = {
  text: string;
  range: Range;
  rects: DOMRectList;
  category: string;
  color: string;
  rangeIndex: RangeIndex;
};

export type Char = {
  text: string,
  style: string,
}
