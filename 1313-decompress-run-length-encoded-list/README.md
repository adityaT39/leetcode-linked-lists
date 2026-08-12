# 1313. Decompress Run-Length Encoded List

**Status:** Passed

## Idea
`nums` is a flat list of `[freq, val]` pairs. Step through it two at a time,
and for each pair append `val` to the result `freq` times.

## Bugs I hit
- Reused the outer loop variable `i` for the inner loop too, and called
  `len(freq)` where `freq` is an `int`, not a list — `TypeError`. Fixed by
  renaming the inner loop variable to `j` and looping over `range(freq)`
  directly instead of `range(len(freq))`.
- Briefly misread `[val] * freq` as numeric multiplication (expecting `12`
  for `val=4, freq=3`). It's actually Python's **list repetition** operator —
  `[4] * 3` produces `[4, 4, 4]`, a valid one-line alternative to the inner
  `for` loop (`result.extend([val] * freq)`).
