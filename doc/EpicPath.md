# Basic use

```python
from epicpath import EpicPath as EPath
```

Actually, I have already created some aliases which are all the same object:

```python
from epicpath import EpicPath
from epicpath import EPath
from epicpath import EP
```

## Join the paths

Paths can be join using the `/` operation, it support other `EpicPath` object but also `Path` object from `pathlib` and `str`.

```python
>>> p1 = EPath('a', 'b')
>>> p1 / EPath('c', 'd')
EpicPath('a/b/c/d')
>>> p1 / Path('c', 'd')
EpicPath('a/b/c/d')
```

It also support it with the opposite order :

```python
'z' / p1
EpicPath('z/a/b')
```

### :warning:

Because a `Path` object also supports the `/` operation, it will return a `Path` object for the following operation:

```python
>>> Path('a', 'b') / EPath('c', 'd')
WindowsPath('a/b/c/d')
```

To prevent this behavior, you can use the `//` operation which always returns a `EpicPath` object:

```python
>>> Path('a', 'b') // EPath('c', 'd')
EpicPath('a/b/c/d')
```

**In place operator**

`EpicPath` object supports the `/=` operation :

```python
>>> p1 = EPath('a', 'b')
>>> p1 /= EPath('c')
>>> p1
EpicPath('a/b/c')
>>> p1 /= Path('d')
>>> p1
EpicPath('a/b/c/d')
>>> p1 /= 'e'
>>> p1
EpicPath('a/b/c/d/e')
```

The method `.append(path)` is doing the same job:

```python
>>> p1 = EPath('a', 'b')
>>> p1.append(EPath('c', 'd'))
>>> p1
EpicPath('a/b/c/d')
>>> p1.append(Path('e', 'f'))
>>> p1
EpicPath('a/b/c/d/e/f')
>>> p1.append('g')
>>> p1
EpicPath('a/b/c/d/e/f/g')
```

The method `.extend()` can be used to apply several path:

```python
>>> p1 = EPath('a', 'b')
>>> p1.extend([EPath('c', 'd'), Path('e', 'f'), 'g'])       # With a list as argument
>>> p1
EpicPath('a/b/c/d/e/f/g')
>>> p1.extend(EPath('h', 'i'), Path('j', 'k'), 'l')         # With several arguments
>>> p1
EpicPath('a/b/c/d/e/f/g/h/i/j/k/l')
```


## Add string to the path

`EpicPath` also supports the `+` operator:

```python
>>> p1 = EPath('a', 'b')
p1 + EPath('c', 'd')
EpicPath('a/bc/d')
p1 + Path('c', 'd')
EpicPath('a/bc/d')
p1 + 'c'
EpicPath('a/bc')

>>> Path('y', 'z') + p1
EpicPath('y/za/b')
>>> 'z' + p1
EpicPath('za/b')
```

As for `/`, the `+=` operator is also supported:

```python
>>> p1 = EPath('a', 'b')
>>> p1 += EPath('c', 'd')
>>> p1
EpicPath('a/bc/d')
>>> p1 += Path('e', 'f')
>>> p1
EpicPath('a/bc/de/f')
>>> p1 += 'g'
>>> p1
EpicPath('a/bc/de/fg')
```

# Get common type

The attributs `.path` (or shorter `.p`) and `.str` can be used to get the representation of the `EpicPath` object as a `Path` object and a `string`: 

```python
>>> p1 = EPath('a', 'b', 'c')
>>> p1.path
WindowsPath('a/b/c')
>>> p1.p
WindowsPath('a/b/c')
>>> p1.str
'a\\b\\c'
```

The absolute path can be obtained with the property `.abs`:

```python
>>> p1 = EPath('a', 'b')
>>> p1.abs
EpicPath('D:/Valentin/epicpath/a/b')
```

# Create and remove files/folders

**`.mkdir(exist_ok=True, parents=True)`**

I changed the default values of the method `.mkdir()`
The only reason is because I usually use this options

This method creates the folder with the same path as the `EpicPath` object

If `exist_ok=False` and the folder already exists, it raises an error.

If the parents of the folde doesn't exists already, it creates them, unless the parameters `parents=False`, it then raises an error.

**`.rmdir(missing_ok=True)`**

The method `.rmdir` remove the directory with the path represented by the `EpicPath` object. This folder needs to be empty

If the folder doesn't exist and the parameter `missing_ok=False`, it raises an error.

**`.unlink(missing_ok=True)`**

the method `.unlink()` delete the file with the path represented by the `EpicPath` object.

If the file doesn't exist and the parameter `missing_ok=False`, it raises an error.


**`.rm(missing_ok=True)`**

the method `rm()` delete the folder/file with the path represented by the `EpicPath` object. If it is a folder, it doesn't need to be empty.

If the folder/file doesn't exist and the parameter `missing_ok=False`, it raises an error.

# Suffix

**`.stem` and `.rstem`**

The property `.stem` return the path name without the last suffix while `.rstem` return the path name without any suffix:

```python
>>> p1 = EPath('a', 'b', 'script.py.zip')
>>> p1
EpicPath('a/b/script.py.zip')
>>> p1.stem
'script.py'
>>> p1.rstem
'script'
```

**`.rm_suffixes(max=None)`**

The method `.rm_suffixes()` remove the suffix of the path.

if `max=None` then it removes all the suffixes.

```python
>>> p1 = EPath('file.py.zip.tar.ext')
>>> p1.rm_suffixes(max=1)
>>> p1
EpicPath('file.py.zip.tar')
>>> p1.rm_suffixes()
>>> p1
EpicPath('file')
```

# Unique files

**`.get_unique(ext='_{0}', always_ext=False)`**

Let's say the files `file.txt` , `file_0.txt` already exist, the method `.get_unique()` return a path that doesn't already exsit:

```python
>>> p1 = EPath('file.txt')
>>> p1.get_unique()
EpicPath('text_1.txt')
```

- The parameter `ext` allows you to change the string adding to the file name.
- If the parameters `always_ext=True`, it always add the string to the file name even though the initial path doesn't exist


**`.be_unique(ext='_{0}', always_ext=False)`**

This is the in place version of the method `.get_unique()`: 

```python
>>> p1 = EPath('file.txt')
>>> p1.be_unique()
>>> p1
EpicPath('text_1.txt')
```

# Get context information

**`.listdir(t='epicpath', concat=False)`**

The method `listdir(t='epicpath', concat=False)` lists all the files and folder in a directory
- The parameter `t` allows you to choose what type you want in the output list (`'epicpath'` (default) for `EpicPath`, `'path'` for `Path` and `'str'` for `str`)
- The parameter `concat=False` can be set to `True` to automatically include the current folder path in the output.

```python
>>> p = EPath('a')

>>> p.listdir()
[EpicPath('b'), EpicPath('setup.py'), EpicPath('file.txt')]
>>> p.listdir(t='path')
[WindowsPath('b'), WindowsPath('setup.py'), WindowsPath('file.txt')]
>>> p.listdir(t='str')
['b', 'setup.py', 'file.txt']

>>> p.listdir(concat=True)
[EpicPath('a/b'), EpicPath('a/setup.py'), EpicPath('a/file.txt')]

```

**`.walk(t='epic')`**

This method yields a generator as the function `os.walk`. The returned types are `EpicPath` for `t='epic'` (default), `Path` for `t='path'` and `str` for `t='str'`.

```python
>>> path = EPath('a')
>>> for p in path.walk():
    ... print(p)
(EpicPath('a'), [EpicPath('b')], [EpicPath('setup.py'), EpicPath('file.txt')])
(EpicPath('a/b'), [], [EpicPath('help.txt')])
>>> for p in path.walk(t='path'):
    ... print(p)
(WindowsPath('a'), [WindowsPath('b')], [WindowsPath('setup.py'), WindowsPath('file.txt')])
(WindowsPath('a/b'), [], [WindowsPath('help.txt')])
>>> for p in path.walk(t='str'):
    ... print(p)
('a', ['b'], ['setup.py', 'file.txt'])
('a/b', [], ['help.txt'])
```

**`.walkfiles(t='epic')`**

This method will return all the files encountered in a `.walk()` process.
The returned types are `EpicPath` for `t='epic'` (default), `Path` for `t='path'` and `str` for `t='str'`.

```python
>>> path = EPath('a')
>>> for p in path.walkfiles():
    ... print(p)
setup.py    # EpicPath object
file.txt    # EpicPath object
help.txt    # EpicPath object
>>> for p in path.walkfiles(t='path'):
    ... print(p)
setup.py    # WindowsPath object
file.txt    # WindowsPath object
help.txt    # WindowsPath object
>>> for p in path.walkfiles(t='str'):
    ... print(p)
setup.py    # string object
file.txt    # string object
help.txt    # string object
```



