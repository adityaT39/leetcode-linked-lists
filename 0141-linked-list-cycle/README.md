# 141. Linked List Cycle

**Status:** Passed

## Idea
Floyd's cycle detection (slow/fast pointers), same setup as 876. If there's a
cycle, the fast pointer will eventually "lap" the slow pointer and they'll
land on the exact same node. If there's no cycle, `fast` runs off the end
first.

## Bugs I hit
- Missing colon after the `while` line (`SyntaxError`).
- Used `or` instead of `and` in the loop condition — with `or`, the loop kept
  going even when one pointer had already hit `None`, causing a crash.
- Compared `slow.val == fast.val` instead of `slow is fast`. Comparing by
  value is wrong here — two *different* nodes could coincidentally hold the
  same value, giving a false positive. Cycle detection needs node *identity*
  (`is`), not value equality (`==`).
