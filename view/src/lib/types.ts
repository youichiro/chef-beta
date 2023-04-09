export type Label = {
  name: string,
  color: string,
}

export type RangeIndex = {
  start: number,
  end: number,
}

export type Annotation = {
  label: Label,
  rangeIndex: RangeIndex,
}

export type Span = {
  text: string,
  index: number,
  class: string,
  annotation?: Annotation,
  showLabel?: boolean,
}
