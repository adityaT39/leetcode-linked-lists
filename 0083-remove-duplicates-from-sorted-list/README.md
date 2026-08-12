# 83. Remove Duplicates from Sorted List

**Status:** Passed

## Idea
Since the list is already sorted, duplicates are always adjacent. Walk `curr`
through the list; whenever `curr.val == curr.next.val`, skip the duplicate by
pointing `curr.next` at `curr.next.next` (and don't advance `curr` yet, since
there could be more than one duplicate in a row).

## Bugs I hit
- `while curr:` instead of `while curr and curr.next:` — without checking
  `curr.next` too, `curr.next.val` crashes with `AttributeError` once `curr`
  reaches the last node.
- `prev.next == curr.next` (comparison) instead of `prev.next = curr.next`
  (assignment) — no crash, but silently did nothing, so duplicates were never
  actually removed despite the code "running fine."
