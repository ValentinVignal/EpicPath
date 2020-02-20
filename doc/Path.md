**EpicPath** supports the functionalities of **Path**. 

Here are some examples: (this documentation is deeply inspired from the [pathlib documentation](https://docs.python.org/3/library/pathlib.html) )

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

The string representation of a path is the raw filesystem path itself (in native form, e.g. with backslashes under Windows), which you can pass to any function taking a file path as a string:

```python
>>> a = EPath('a', 'b', 'c')
>>> str(a)
'a\\b\\c'
```

Similarly, calling [bytes](https://docs.python.org/3/library/stdtypes.html#bytes) on a path gives the raw filesystem path as a bytes object, as encoded by [os.fsencode()](https://docs.python.org/3/library/os.html#os.fsencode) :

```python
>>> bytes(a)
b'a\\b\\c'
```

# Accessing individual parts

To access the individual “parts” (components) of a path, use the following property:

`EpicPath.parts`

```python
>>> a = EPath('a', 'b', 'c')
>>> a.parts
('a', 'b', 'c')
```

# Methods and properties

*EpicPath* provides the following methods and properties:

**`EpicPath.drive`**

A string representing the drive letter or name, if any:

```python
>>> EPath('c:/Program Files/').drive
'c:'
>>> EPath('/Program Files/').drive
''
```

**`EpicPath.parents`**

An immutable sequence providing access to the logical ancestors of the path:

```python
>>> p = EPath('a', 'b', 'c')
>>> p.parents
(EpicPath('a/b'), EpicPath('a'), EpicPath('.'))
>>> p.parents[0]
EpicPath('a/b')
>>> p.parents[1]
EpicPath('a')
>>> p.parents[2]
EpicPath('.')
```

**`EpicPath.parent`**

The logical parent of the path

```python
>>> p.parent
EpicPath('a/b')
```

> :warning: This is a purely lexical operation, hence the following behaviour:
>
> ```python
> >>> p = EPath('a', 'b', '..')
> >>> p.parent
> EpicPath('a/b')
> ```
> If you want to walk an arbitrary filesystem path upwards, it is recommended to first call `EpicPath.resolve()` so as to resolve symlinks and eliminate `“..”` components.

**`EpicPath.name`**

A string representing the final path component, excluding the drive and root, if any:

```python
>>> EPath('a', 'b', 'file.py').name
'file.py'
```

**`EpicPath.suffix`**

The file extension of the final component, if any:

```python
>>> EPath('a/b/file.py').suffix
'.py'
>>> EPath('a/b/file.py.zip').suffix
'.zip'
>>> EPath('a/b/file').suffix
''
```

**`EpicPath.suffixes`**

A list of the path’s file extensions:

```python
>>> EPath('a/b/file.py').suffixes
['.py']
>>> EPath('a/b/file.py.zip').suffixes
['.py', '.zip']
>>> EPath('a/b/file').suffixes
[]
```

**`EpicPath.stem`**

The final path component, without its last suffix:

```python
>>> EPath('a/b/file.py').stem
'file'
>>> EPath('a/b/file.py.zip').stem
'file.py'
>>> EPath('a/b/file').stem
'file'
```

**`EpicPath.as_posix()`**

Return a string representation of the path with forward slashes (`/`):

```python
>>> EPath('a', 'b', 'c').as_posix()
'a/b/c'
```

**`EpicPath.with_name(name)`**

Return a new path with the name changed. If the original path doesn’t have a name, ValueError is raised:

```python
>>> p = EPath('a', 'b', 'file.py')
>>> p.with_name('setup.py')
EpicPath('a/b/setup.py')
>>> p = EPath('c:/')
>>> p.with_name('setup.py')
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "epicpath\EpicPath.py", line 95, in with_name
    raise ValueError(f'{self.__repr__()} has an empty name')
ValueError: EpicPath('c:/') has an empty name
```

**`EpicPath.with_suffix`**

Return a new path with the [suffix] changed. If the original path doesn’t have a suffix, the new suffix is appended instead. If the suffix is an empty string, the original suffix is removed:

```python
>>> p = EPath('a', 'b', 'file.py.zip')
>>> p.with_suffix('.tar')
EpicPath('a/b/file.py.tar')
>>> p = EPath('README')
>>> p.with_suffix('.md')
EpicPath('README.md')
```

# Concrete Path methods

**`EpicPath.exists()`**

Whether the path points to an existing file or directory:

```python
>>> EPath('.').exists()
True
>>> EPath('file.py').exists()
True
>>> EPath('nonexistentfile').exists()
False
```

**`EpicPath.mkdir(mode=0o777, parents=True, exist_ok=True)`**

Create a new directory at this given path. If mode is given, it is combined with the process’ `umask` value to determine the file mode and access flags. If the path already exists, FileExistsError is raised.

If parents is true (the default), any missing parents of this path are created as needed; they are created with the default permissions without taking mode into account (mimicking the POSIX mkdir -p command).

If parents is false, a missing parent raises FileNotFoundError.

If exist_ok is false, FileExistsError is raised if the target directory already exists.

If exist_ok is true (the default), FileExistsError exceptions will be ignored (same behavior as the POSIX mkdir -p command), but only if the last path component is not an existing non-directory file.
**`Path.rename(target)`**

Rename this file or directory to the given *target*, and return a new EpicPath instance pointing to *target*. On Unix, if target exists and is a file, it will be replaced silently if the user has permission. *target* can be either a string, a Path object or another EpicPath object

```python
>>> p = EPath('foo')
>>> p.open('w').write('some text')
9
>>> target = EPath('bar')
>>> p.rename(target)
EpicPath('bar')
>>> target.open().read()
'some text'
```

**`EpicPath.resolve(strict=False)`**

Make the path absolute, resolving any symlinks. A new path object is returned:

```python
>>> p = EPath()
>>> p
EpicPath('.')
>>> p.resolve()
PosixPath('/home/epicpath')
```
“`..`” components are also eliminated (this is the only method to do so):

```python
>>> p = EPath('docs/../setup.py')
>>> p.resolve()
EpicPath('/home/epicpath/setup.py')
```

If the path doesn’t exist and strict is True, FileNotFoundError is raised. If strict is False, the path is resolved as far as possible and any remainder is appended without checking whether it exists. If an infinite loop is encountered along the resolution path, RuntimeError is raised.

**`EpicPath.rmdir(missing_ok=True)`**

Remove this directory.
If `missing_ok` is False, the directory must be empty 

**`EpicPath.unlink(missing_ok=True)`**

Remove this file or symbolic link. If the path points to a directory, use EpicPath.rmdir() instead.

If missing_ok is false, FileNotFoundError is raised if the path does not exist.

If missing_ok is true (the default), FileNotFoundError exceptions will be ignored (same behavior as the POSIX rm -f command).

