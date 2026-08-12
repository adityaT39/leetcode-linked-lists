# 21. Merge Two Sorted Lists

**Status:** Worked through, not re-verified with a final "Accepted" run —
retest before trusting this fully.

## Idea
Only need **one** dummy node (for the new merged list) — not one per input
list. Walk `p1` and `p2` through `list1`/`list2` at the same time; whichever
has the smaller value gets appended next via a `tail` pointer, and only that
pointer advances. `tail` always points at the last node placed into the
result so far — same role `prev` played in problem 203.

Once one list runs out, the other list's *remaining chain* can just be
attached wholesale (`tail.next = p1 if p1 else p2`) — since its nodes are
already linked to each other in sorted order, no further comparisons are
needed.

## Things I got confused about
- Thought I needed two dummy nodes, one wrapping each input list. Only the
  *output* list needs a dummy.
- Worried that once `p1` became `None` first, I'd "lose access" to the rest
  of `list2`. Resolved: `p2` is a pointer that already advanced during the
  loop, so `tail.next = p2` attaches only the *unconsumed remainder*, not the
  whole original list.
