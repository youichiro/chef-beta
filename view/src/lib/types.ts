export type Label = {
  name: string;
  color: string;
};

export type RangeIndex = {
  start: number;
  end: number;
};

export type Annotation = {
  id: number;
  label: Label;
  rangeIndex: RangeIndex;
};

export type Span = {
  text: string;
  index: number;
  class: string;
};

export type Tag = {
  x: number;
  y: number;
  annotation: Annotation;
};

export type LabelSelectMenuOffset = {
  top: number;
  left: number;
};
