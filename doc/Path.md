**EpicPath** supports the functionalities of **Path**. 

Here are some examples: (this documentation is inspirated from the [pathlib documentation](https://docs.python.org/3/library/pathlib.html) )

# Basic Use

Navigating inside a directory tree: 

```pythonstub
>>> p = EPath('f1', 'f2')
>>> q = p / 'f3' / 'f4'
>>> q
EpicPath('f1/f2/f3/f4')
```

Querying path properties:

```python
>>> q.exists()
False
>>> q.is_dir()
False
```

# Operators

The slash operator helps create child paths, similarly to [os.path.join()](https://docs.python.org/3/library/os.path.html#os.path.join) :

```python
>>> p = EPath('f1', 'f2')
>>> q = p / 'f3' / 'f4'
>>> q
EpicPath('f1/f2/f3/f4')
```

A path object can be used anywhere an object implementing [os.PathLike](https://docs.python.org/3/library/os.html#os.PathLike) is accepted:

```python
>>> import os
>>> p = EPath('f1')
>>> os.fspath(p)
'f1'
```

