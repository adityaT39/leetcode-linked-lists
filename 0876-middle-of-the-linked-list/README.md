# 876. Middle of the Linked List

**Status:** Passed

## Idea
Use a slow and a fast pointer, both starting at `head`. Every loop iteration,
`slow` moves 1 step and `fast` moves 2 steps. By the time `fast` reaches the
end, `slow` is sitting at the middle — this works for both odd and even length
lists.

## Bug I hit
Originally wrote the loop condition as just `while fast is not None:`. On an
odd-length list this crashes with `AttributeError: 'NoneType' object has no
attribute 'next'`, because `fast.next.next` gets evaluated even when
`fast.next` is `None`. Fixed by requiring **both** `fast is not None` and
`fast.next is not None` in the loop condition.
