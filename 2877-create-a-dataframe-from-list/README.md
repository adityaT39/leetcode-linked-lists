# 2877. Create a DataFrame from List

**Status:** Passed

(Not a linked-list problem — grouped here since it came up during this same
practice session. A pandas/DataFrame basics question.)

## Bug I hit
Used `print(df)` instead of `return df`. The function printed the correct
output to console but actually returned `None`, so the judge saw no return
value. Fixed by returning the DataFrame instead of printing it.
