from pathlib import Path
from pathlib import _windows_flavour, _posix_flavour
import shutil
import os


class EpicPath(Path):
    """
    This is a SubClass of Path from pathlib.
    This class aims to simplify high level operation with path
    """

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
        """

        :param other:
        :return:
        """
        other = EpicPath(other)
        total_parts = self.add_parts(self, other)

        return EpicPath(*total_parts)

    def __radd__(self, other):
        """

        :param other:
        :return:
        """
        other = EpicPath(other)
        total_parts = self.add_parts(other, self)
        return EpicPath(*total_parts)

    @property
    def str(self):
        """
        Because it is soooooooo long to write As_poSiX if the coooode
        :return:
        """
        return self.as_posix()

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



