# 2487. Remove Nodes From Linked List

**Status:** Passed — hardest problem in this set so far.

## Idea
A node must be removed if there's anything **bigger** to its right. That
condition is naturally checked right-to-left: track the biggest value seen
so far starting from the tail, moving backward. But a singly linked list
can't be walked backward directly — so the trick is:

1. **Reverse the whole list.** Now walking forward through the reversed list
   *is* walking backward through the original.
2. **Single pass with a running max.** Walk `prev`/`curr` through the
   reversed list. For each node: if its value is *less than* `max_so_far`,
   unlink it (`prev.next = curr.next`, only `curr` advances). Otherwise it
   survives — it becomes the new `max_so_far`, and `prev` advances too.
3. **Reverse back** to restore original order before returning.

This turns the naive O(n²) brute force (nested loop: for every node, rescan
everything to its right) into O(n) — one reversal, one linear pass, one
reversal back.

## Why the first node of the reversed list is always safe
Initialize `max_so_far = 0`. Since the problem guarantees every node value
is `>= 1`, the very first node processed is *guaranteed* to survive (nothing
can be less than 0), so `prev` always gets pointed at a real node before any
removal logic can possibly run. That's why this doesn't need a dummy node
the way 203 did — 203's target value could coincide with `head`'s value, but
here the first node of the reversed list structurally can never be removed.

## Bugs / confusions along the way
- Wrote `before = none` (lowercase) in `reverse_list` — `NameError`, since
  Python's `None` is capitalized.
- Original plan used a nested `curr`/`after` scan (compare each node against
  every node to its right directly) — logically correct but O(n²), too slow
  for `n` up to `10^5`.
- Forgot to update `max_so_far` inside the "keep" branch at first — fixed by
  setting `max_so_far = prev.val` right after `prev = curr`.
- Nearly reversed the wrong variable at the end (`self.reverse_list(prev)`
  instead of `self.reverse_list(reverse_head)`). By the time the loop ends,
  `prev` points at the **tail** of the filtered list (its `.next` is already
  `None`), while `reverse_head` still points at the **head** — reversing
  from `prev` would have silently dropped every node before it.

## This reuses ideas from
234 (reversal) and 203 (prev/curr removal pattern) — the hard part here
wasn't any single technique, it was recognizing which earlier tools to
combine and in what order.
