# 817. Linked List Components

**Status:** Passed

## Idea
Walk the list one node at a time, keeping a single boolean —
`in_connected_component` — for "am I currently inside a run of nums-values
right now?" Each time a node's value is in `nums` **and** the flag was
`False` the step before, that's the *start* of a new component, so the
counter increments. The flag only resets to `False` when a node's value is
**not** in `nums`.

This is a per-node framing rather than a per-pair one, which naturally
covers a single-node component too (e.g. `head=[5]`, `nums=[5]` → 1
component) — a pairwise "check node n and n+1 together" approach would need
an awkward special case for that.

## Bug I hit
First draft bundled two separate conditions into one `if`:
```python
if curr.val in nums and in_connected_component is False:
    ...
else:
    in_connected_component = False   # wrong: fires even mid-component
```
The problem: once inside a component, `in_connected_component` is already
`True`, so on the *next* node (still part of the same component) the
combined condition goes false and falls into `else` — which incorrectly
resets the flag to `False`, even though the run hasn't actually broken. This
doesn't show up on components of length 2 (matches both given examples) but
silently overcounts any component of length 3+.

**Fix:** separate the two questions instead of bundling them —
```python
if curr.val in nums:
    if not in_connected_component:
        connected_component += 1
    in_connected_component = True
else:
    in_connected_component = False
```
`in_connected_component = True` now sits outside the inner `if`, so it's set
on *every* node that belongs to a component — whether it's the first node of
a new run or the fifth node of an ongoing one — instead of only on the
count-increment path.
