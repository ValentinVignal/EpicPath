# :sparkles: EpicPath :sparkles: 
A high Level Python Library to work with Path

`EpicPath` is a SubClass of `Path` from `pathlib`.
This class aims to simplify high level operations with path

# Context and history

I'm a Computing Student tired of creating again and again the same functions through all my projects to do the exact same thing... :tired_face: 
Indeed, in every of my projects I create files, delete them, create folders and delete them *blablabla* ...
To solve this boring problem, I decided to create my own library that I can create one and only one time to use and reuse as many time as I wish to.
And because I'm trying to be nice to this cruel world I share this *Epic* project with all of you :heart:
So feel free to download, use and give feedback about this ***epic***  creation. :+1:


# Description

You already know `Path` from the library `pathlib`. Well, `EpicPath` is all like `Path` but in a ***EPIC*** way :tada: . 

It is a *pseudo* subclass of `Path` but consider it as a subclass, it supports all the methods and options of the original library.
It is also a `os.PathLike` object which allows you to use as you would want to:

```python
with open(my_epic_path_object, 'w') as f:
    f.write('This is epic !!!')
```

 
# Use it



## Install it

```shell
pip install epic-path
```

## Use it

```python
from epicpath import EpicPath as EPath

path = EPath('f1', 'f2')        # EpicPath('f1/f2')
path2 = path / 'f3'             # EpicPath('f1/f2/f3')
path2 += '_0'                   # EpicPath('f1/f2/f3_0')
```

[See the documentation](doc/README.md)   

# :warning: Warnings :warning:

Because `Path` is build-in Python libraries, some other library
(like [PIL](https://github.com/python-pillow/Pillow) or [skopt](https://github.com/scikit-optimize/scikit-optimize))
can have a specific behavior when the given filename is a `str` or a `Path` object.
Unfortunately, they don't support an `EpicPath` object ... :cry: But no worries, it is still possible to give an `EpicPath` object as a `Path` object or a `str` object using the properties `.path` and `.str`:

```python
path = EPath('f1', 'f2')        # EpicPath('f1/f2')

weird_function(path.path)       # Gives Path('f1/f2') to the function
weird_function(path.str)        # Gives the string 'f1/f2' to the function
```

 
 