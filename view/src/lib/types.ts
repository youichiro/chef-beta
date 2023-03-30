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
  rangeIndex: RangeIndex;
  rects: DOMRectList;
  category: string;
  color: string;
};

export type Char = {
  text: string,
  style: string,
  categoryName: string,
}
