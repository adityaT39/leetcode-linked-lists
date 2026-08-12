# 2130. Maximum Twin Sum of a Linked List

**Status:** Passed

## Idea
Node `i`'s twin is node `n-1-i` — front paired with back. That's the exact
same pairing structure as 234's palindrome check, so the same three-step
recipe applies: find the middle, reverse the second half, then walk `head`
and the new reversed-head (`prev`) forward together. At each step, `p1` and
`p2` are exactly one twin pair.

## Bugs I hit
- First draft computed `sum_one` *before* advancing the pointers and
  `sum_two` *after*, both inside the same loop iteration — so one iteration
  processed two pairs' worth of sums at once, and only the last two
  computed sums were ever kept (not a real running maximum). This also let
  the pointers overrun and crash (`AttributeError: 'NoneType' object has no
  attribute 'val'`) once one of them ran past the end.
- After simplifying to one sum per iteration, still just *overwrote*
  `max_sum` each time instead of comparing. Fixed with
  `max_sum = max(max_sum, p1.val + p2.val)`.
- Initially tried adding an extra `p1.val + p2.val` check *after* the loop
  ended — but by the time the loop exits, `p1`/`p2` are already `None`
  (that's *why* the loop exits), so touching `.val` on them there crashes.

## Alternative approach discussed (not implemented)
Could also traverse once to dump every value into a Python list/array, then
directly index `arr[i]` and `arr[n-1-i]` for `i` in `range(n // 2)` — trading
the reversal trick for O(n) extra space and direct index access.
