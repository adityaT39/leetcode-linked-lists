# 707. Design Linked List

**Status:** Delivered corrected code after debugging; not re-confirmed
"Accepted" in a later session — retest before trusting this fully.

## Idea
Build a singly linked list from scratch with a private `Node` class and a
`MyLinkedList` wrapper tracking `self.head` and `self.size`.

This was the hardest problem in the set so far — lots of small bugs, mostly
from **early `return` statements skipping bookkeeping updates**.

## Bugs I hit, roughly in order
1. Constructor originally took a `val` and treated `MyLinkedList` itself as a
   node. Wrong design — split into a separate `Node` class.
2. Referenced `self.length` without ever defining it — renamed consistently
   to `self.size`.
3. `get()` returned the node object instead of `.val`.
4. Reused the public `get()` internally for node lookups. Since `get(-1)`
   returns `-1` (a truthy int, not `None`), `if before:` checks incorrectly
   passed and then crashed on `(-1).next`. Fixed by adding a private
   `get_val()` helper that returns the actual node or `None`.
5. `addAtTail` originally overshot past the last node (`while temp:` instead
   of `while temp.next:`), leaving `temp = None` right before
   `temp.next = new_node` — crash. Also crashed separately on an empty list
   (`self.head is None`).
6. `addAtIndex` was missing the upper bound check (`index > self.size`) and
   mishandled `index == 0`.
7. `deleteAtIndex` had no bounds check at all and crashed on `index == 0`.
8. **The big one:** both `addAtTail` and `deleteAtIndex` had their
   special-case branches (`index == 0` / empty list) `return` *before* the
   line that updates `self.size`. This let `self.size` drift out of sync
   with the real list length — undercounting in `addAtTail`, overcounting in
   `deleteAtIndex`. The overcounting was the direct cause of a runtime
   `AttributeError: 'NoneType' object has no attribute 'val'` in `get()`: a
   stale bounds check passed for an index that had actually run past the
   real, shorter list.

   Fixed by restructuring both methods with `if/else` so the size update
   sits *after* the branch and is always reached, no matter which path was
   taken.
9. In `addAtIndex`, once `index == 0` is handled separately and the bounds
   check guarantees `1 <= index <= self.size`, `get_val(index - 1)` is
   *guaranteed* to return a real node — so the `if before:` guard around
   `self.size += 1` was dead code that could silently swallow the size
   update. Removed it; the update is now unconditional.

## Lesson learned
Whenever a method has multiple `return` paths, check that **every** path
reaches any bookkeeping (like a counter update) it's supposed to reach — an
early `return` is an easy way to silently skip it.
