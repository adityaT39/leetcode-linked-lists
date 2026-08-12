# 237. Delete Node in a Linked List

**Status:** Passed

## Idea
You're **not** given `head`, so the usual "find the node before it and skip
over it" approach is impossible — there's no way to reach backward. But the
problem guarantees the values are unique and `node` is never the last node.
That means instead of removing `node` from the chain, you can copy the
*next* node's value into `node`, then unlink the (now-duplicated) next node —
making `node` effectively "become" its successor.

```
node.val = node.next.val
node.next = node.next.next
```

## What was genuinely mine vs. guided
The two guarantees (unique values, node isn't last) were pointed out to me as
the reason this trick is even possible. Once I had the "copy forward" idea,
I wrote the actual two-line fix myself without being shown code.
