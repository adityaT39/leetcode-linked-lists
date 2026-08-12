# 2807. Insert Greatest Common Divisors in Linked List

**Status:** Passed

## Idea
Two parts: a `gcd(a, b)` helper (Euclidean algorithm on plain integers), and
a traversal that walks `curr`/`next` through adjacent pairs, inserting a new
GCD node between each pair, then advancing *both* pointers past the pair
just processed.

## Bugs I hit in `gcd()`
- Used `remain` inside the `while remain != 0:` condition before it was ever
  assigned — `NameError`. Tried `global remain` as a fix, which doesn't
  assign a value either, it just changes scope. Fixed by initializing
  `remain = 1` before the loop (any nonzero starting value works, since it's
  overwritten on the first iteration).
- Had `return` *inside* the while loop body, so the function returned after
  only one iteration of the Euclidean algorithm instead of running it to
  completion.
- First draft computed the GCD by mutating `curr.val`/`next.val` directly —
  which would have corrupted the actual linked list's data as a side effect
  of just computing a GCD. Fixed by rewriting `gcd()` to take two plain
  integers `a, b` and operate only on local variables, no `.val` involved.

## Bug I hit in `insertGreatestCommonDivisors()`
Forgot to advance `next` inside the loop (only `curr` was updated via
`curr = curr.next.next`), so `next` stayed stuck on its original node
forever instead of moving to the node after the newly-inserted pair.

## Note
The `if a > b` / `else` branches in `gcd()` are correct but redundant — the
Euclidean algorithm self-corrects even without checking which of `a`/`b` is
bigger; `b % a` is well-defined either way. Left as-is since it works, but
could be simplified.
