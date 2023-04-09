import type { Label } from "$lib/types"

export const maxLabelNameLength = (labels: Label[]) => {
  return Math.max(...labels.map(label => label.name.length))
}
