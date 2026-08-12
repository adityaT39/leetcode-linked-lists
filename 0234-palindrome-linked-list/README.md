# 234. Palindrome Linked List

**Status:** Each piece (find-middle, reverse) was individually worked through
and verified by tracing; the full assembled solution has not yet been
submitted — retest before trusting this fully.

## Idea
Three stages, each one a technique reused later in this same session:
1. **Find the middle** with slow/fast pointers (same as 876).
2. **Reverse the second half** in place (`prev`/`curr`/`nxt` pattern).
3. **Compare** the original front half against the now-reversed back half,
   one node at a time, using two independent pointers (`p1` from `head`,
   `p2` from the new reversed head `prev`).

## Misconceptions I had (and cleared up)
- Thought reversing broke the comparison because "the nodes are in different
  memory." Comparison is by *value*, not identity — reversing only rewires
  `.next` arrows, it doesn't move where each node physically "is."
- Thought I needed a nested loop to compare against a reversed list. A single
  loop with two synced pointers is enough.
- Tried "two pointers, one from head, one from tail" directly — doesn't work
  on a singly linked list, since there's no way to walk backward from the
  tail without first reversing (or converting to an array).
- Worried `slow.next = None` during reversal was "breaking off" from the
  list. That's intentional — it's what makes the reversed second half a
  proper standalone list with `None` as its true end.

## This idea reappears later
The exact same "reverse, then walk two pointers" trick is reused in 2130 and
2487.
