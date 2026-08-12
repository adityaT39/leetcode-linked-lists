# LeetCode — Linked Lists

Personal practice log while learning linked lists from scratch. Each folder
is one problem: my own solution code plus a short writeup of the idea and
the bugs I actually hit while getting there (not just the clean final
answer).

| # | Problem | Status |
|---|---------|--------|
| [83](0083-remove-duplicates-from-sorted-list) | Remove Duplicates from Sorted List | Passed |
| [141](0141-linked-list-cycle) | Linked List Cycle | Passed |
| [203](0203-remove-linked-list-elements) | Remove Linked List Elements | Passed |
| [234](0234-palindrome-linked-list) | Palindrome Linked List | Worked through, not re-verified |
| [237](0237-delete-node-in-a-linked-list) | Delete Node in a Linked List | Passed |
| [707](0707-design-linked-list) | Design Linked List | Delivered fix, not re-verified |
| [876](0876-middle-of-the-linked-list) | Middle of the Linked List | Passed |
| [1313](1313-decompress-run-length-encoded-list) | Decompress Run-Length Encoded List | Passed |
| [2130](2130-maximum-twin-sum-of-a-linked-list) | Maximum Twin Sum of a Linked List | Passed |
| [2487](2487-remove-nodes-from-linked-list) | Remove Nodes From Linked List | Passed |
| [2807](2807-insert-greatest-common-divisors-in-linked-list) | Insert Greatest Common Divisors in Linked List | Passed |
| [21](0021-merge-two-sorted-lists) | Merge Two Sorted Lists | Worked through, not re-verified |
| [2877](2877-create-a-dataframe-from-list) | Create a DataFrame from List (pandas, not a linked list) | Passed |

## Recurring techniques across these problems

- **Slow/fast pointers** — find the middle, detect a cycle (876, 141, 234,
  2130).
- **Dummy node** — sidestep special-casing "what if head itself needs to be
  removed/replaced" (203, 21).
- **prev/curr removal pattern** — unlink a node by pointing the previous
  node's `.next` past it (203, 707, 2487).
- **Iterative reversal** (`prev`/`curr`/`nxt`) — reused directly in 234,
  2130, and 2487.
- **Reverse → process → reverse back** — turns "I need to walk this
  backward" into something a singly linked list can actually do (2487).

## Bug patterns I keep needing to watch for

- Off-by-one loop conditions (`while curr:` vs `while curr.next:`) that skip
  or crash on the last node.
- `=` vs `==` — an accidental comparison instead of an assignment fails
  silently, no crash, just wrong behavior.
- Early `return` statements that skip a bookkeeping update (like a size
  counter) on some code paths but not others.
- Forgetting to advance *every* pointer that needs to move each loop
  iteration, not just some of them.
