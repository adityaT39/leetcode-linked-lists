# 203. Remove Linked List Elements

**Status:** Passed (two different approaches)

## Idea
The tricky part of removal problems: the node to remove might be `head`
itself. A **dummy node** placed before `head` sidesteps that special case —
you always have "something before" whichever node needs unlinking.

## Approach 1 — prev/curr
Walk `curr` through the list. If `curr.val == val`, skip it by pointing
`prev.next` at `curr.next` (and only advance `curr`, not `prev`). Otherwise
advance both `prev` and `curr` together.

**Bug I hit:** originally wrote `while curr and curr.next:`, which skips
processing the very last node in the list. Fixed to `while curr:`.

## Approach 2 — curr/runner
`curr` stays anchored at the last known-good node; a `run` pointer scans
ahead past any run of matching values, then `curr.next` is pointed straight
at wherever `run` lands.

## Concepts learned here
- You can create your own `ListNode` instances directly in LeetCode's editor
  even though you didn't define the class yourself — it's already provided
  above your `Solution`.
- Dummy nodes let you treat "removing the head" the same as removing any
  other node, no special-casing needed.
