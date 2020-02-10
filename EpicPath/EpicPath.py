from pathlib import Path
import shutil
import os
from os.path import abspath


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
        self.p = Path(*args, **kwargs)

    # ----------------------------------------------------------------------------------------------------
    #                           To make EpicPath like a subclass of Path
    # ----------------------------------------------------------------------------------------------------

    def __getattr__(self, attr):
        return getattr(self.p, attr)

    def __str__(self):
        return str(self.p)

    def __truediv__(self, p):
        return EpicPath(self.p / p)

    def __rtruediv__(self, p):
        return EpicPath(p / self.p)

    def __repr__(self):
        return f"EpicPath('{self.str}')"

    # ----------------------------------------------------------------------------------------------------
    #                                          Comparaison
    # ----------------------------------------------------------------------------------------------------

    def __eq__(self, p):
        p = EpicPath(p)
        return abspath(self.str) == abspath(p.str)

    def __lt__(self, p):
        """

        :param p:
        :return: self < p (p includes self)
        """
        p = EpicPath(p)
        p_parts = p.abspath.parts
        self_parts = self.abspath.parts
        if len(p_parts) >= len(self_parts):
            return False
        for i in range(len(p_parts)):
            if not p_parts[i] == self_parts[i]:
                return False
        return True

    def __le__(self, p):
        return self < p or self == p

    def __ge__(self, p):
        """

        :param p:
        :return: self > p
        """
        return not self.__le__(p)


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

        :param p:
        :return:
        """
        p2 = self + p
        print(p2)
        self.p = Path(p2.str)

    @property
    def str(self):
        """
        Because it is soooooooo long to write As_poSiX if the coooode
        :return:
        """
        return self.as_posix()

    @property
    def abspath(self):
        return EpicPath(abspath(self.str))

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



