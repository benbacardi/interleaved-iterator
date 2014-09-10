selectiveiterable.py
====================

A Python class that, given a number of iterables, returns the next value from a particular iterable based on the provided key function, until all iterables are exhausted.

A trivial example:

```python
>>> a = iter([1, 3, 5, 7, 9])
>>> b = iter([2, 4, 6, 8])
>>> for i in SelectiveIterable([iter(a), iter(b)], key=int):
...     print i
... 
1
2
3
4
5
6
7
8
9
```
