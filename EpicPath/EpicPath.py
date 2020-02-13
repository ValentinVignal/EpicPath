from pathlib import Path
import shutil
import os
from os.path import abspath
import functools


@functools.total_ordering
class EpicPath:
    """
    This is a SubClass of Path from pathlib.
    This class aims to simplify high level operation with path
    """

    def __init__(self, *args, **kwargs):
        args = list(args)
        for i in range(len(args)):
            if isinstance(args[i], EpicPath):
                args[i] = args[i].str
        args = tuple(args)
        for k in kwargs:
            if isinstance(kwargs[k], EpicPath):
                kwargs[k] = kwargs[k].str
        self._p = Path(*args, **kwargs)

    # ----------------------------------------------------------------------------------------------------
    #                           To make EpicPath like a subclass of Path
    # ----------------------------------------------------------------------------------------------------

    def __getattr__(self, attr):
        return getattr(self.p, attr)

    def __str__(self):
        return str(self.p)

    def __truediv__(self, other):
        """

        :param other:
        :return:  self / other
        """
        return EpicPath(self.p / EpicPath.to_path(other))

    def __rtruediv__(self, other):
        """
        ⚠ IT WON T WORK WITH A PATH ⚠
        -> User floordiv instead <-
        :param other:
        :return: other / self
        """
        return EpicPath(EpicPath.to_path(other) / self.p)

    def __floordiv__(self, other):
        """

        :param other:
        :return:  self / other
        """
        return EpicPath(self.p / EpicPath.to_path(other))

    def __rfloordiv__(self, other):
        """

        :param other:
        :return: other // self = other / self (but works with Path)
        """
        return EpicPath(EpicPath.to_path(other) / self.p)

    def __repr__(self):
        return f"EpicPath('{self.str}')"

    # ----------------------------------------------------------------------------------------------------
    #                                          Comparison
    # ----------------------------------------------------------------------------------------------------

    def __eq__(self, other):
        """

        :param other:
        :return: self == other
        """
        other = EpicPath(other)
        return self.abs.str == other.abs.str

    def __lt__(self, other):
        """
        ⚠ IT IS TRUE IS SELF IS INCLUDED IN OTHER (AS FILE/FOLDER) ⚠
        :param other:
        :return: self < other (other includes self)
        """
        other = EpicPath(other)
        other_parts = other.abs.parts
        self_parts = self.abs.parts
        if len(other_parts) >= len(self_parts):
            return False
        for i in range(len(other_parts)):
            if not other_parts[i] == self_parts[i]:
                return False
        return True

    # ----------------------------------------------------------------------------------------------------
    #                                               Properties
    # ----------------------------------------------------------------------------------------------------

    @property
    def p(self):
        return self._p

    @p.setter
    def p(self, p):
        if isinstance(p, EpicPath):
            self._p = p.p
        elif isinstance(p, Path):
            self._p = p
        else:
            self._p = Path(str(p))

    @property
    def str(self):
        """
        Because it is soooooooo long to write As_poSiX if the coooode
        :return:
        """
        return self.as_posix()

    @property
    def abs(self):
        return EpicPath(abspath(self.str))

    # ----------------------------------------------------------------------------------------------------
    #                                               Add
    # ----------------------------------------------------------------------------------------------------

    @staticmethod
    def add_parts(path1, path2):
        """

        :param path1:
        :param path2:
        :return:
        """
        path1_parts = path1.parts
        path2_parts = path2.parts
        total_parts = (*path1_parts[:-1], path1_parts[-1] + path2_parts[0], *path2_parts[1:])
        return total_parts

    def __add__(self, other):
        other = EpicPath(other)
        total_parts = self.add_parts(self, other)

        return EpicPath(*total_parts)

    def __radd__(self, other):
        other = EpicPath(other)
        total_parts = self.add_parts(other, self)
        return EpicPath(*total_parts)

    def add(self, p):
        """

        :param p: Can be a list of string or just a string/path
        :return:
        """
        if not isinstance(p, list):
            p = [p]
        for p_ in p:
            self.p = self + EpicPath(p_)

    def __iadd__(self, other):
        """

        :param other:
        self += other
        """
        self.p = (self + other).p
        return self

    # ----------------------------------------------------------------------------------------------------
    #                                       Append and extend
    # ----------------------------------------------------------------------------------------------------

    # This is the inplace function for p1 / p2

    def append(self, p):
        """

        :param p:

        self /= p
        """
        self.p = (self / p).p

    def __idiv__(self, other):
        """

        :param other:

        self /= p
        """
        self.p = (self / other).p
        return self

    def extend(self, *args):
        """

        :param args: args[0]: Can be a List()

        self /= p1 / p2 / p3
        """
        if len(args) > 0:
            p_list = args[0]
            if not isinstance(p_list, list):
                p_list = [p_list]
            for p in p_list:
                self.append(p)
            for p in args[1:]:
                self.append(p)

    # ----------------------------------------------------------------------------------------------------
    #                                       Create and delete
    # ----------------------------------------------------------------------------------------------------

    def mkdir(self, exist_ok=True, parents=True, *args, **kwargs):
        """
        Change the default value of exist_ok and parents to True because I always use it like that
        :param exist_ok:
        :param parents:
        :param args:
        :param kwargs:
        :return:
        """
        super(EpicPath, self).mkdir(exist_ok=exist_ok, parents=parents, *args, **kwargs)

    def rmdir(self, missing_ok=True):
        """
        Remove a directory, but it must be empty

        :param missing_ok:
        :return:
        """
        if missing_ok and not self.exists():
            pass
        else:
            super(EpicPath, self).rmdir()

    def rm(self, missing_ok=True):
        """
        Delete a folder/file (even if the folder is not empty)

        :param missing_ok:
        :return:
        """
        if not missing_ok and not self.exists():
            raise
        if self.exists():
            # It exists, so we have to delete it
            if self.is_dir():       # If false, then it is a file because it exists
                shutil.rmtree(self)
            else:
                self.unlink()

    # ----------------------------------------------------------------------------------------------------
    #                                       Static methods
    # ----------------------------------------------------------------------------------------------------

    @staticmethod
    def to_path(p):
        """

        :param p:
        :return: Path(p)
        """
        if isinstance(p, EpicPath):
            return p.p
        elif isinstance(p, Path):
            return p
        else:
            return Path(str(p))


if __name__ == '__main__':

    p = Path('a', 'b')
    ep = EpicPath('y', 'z')
    p_ep = p / ep

