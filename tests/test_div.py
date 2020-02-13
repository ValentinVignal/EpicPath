import unittest
from EpicPath import EpicPath as EP
from pathlib import Path


class Div(unittest.TestCase):
    """
    Tests the library EpicPath
    """

    # --------------------------------------------------------------------------------
    #                           __truediv__(self, other)
    # --------------------------------------------------------------------------------

    def test__truediv__string(self):
        """
        Test the truedivition
        :return:
        """
        p = EP('a', 'b', 'c')
        p_truth = EP('a', 'b', 'c', 'de')

        p_truedived = p / 'de'
        self.assertEqual(p_truedived, p_truth)

    def test__truediv__path(self):
        """
        test EP / Path
        :return:
        """
        p = EP('a', 'b', 'c')
        p_truth = EP('a', 'b', 'c', 'd', 'e')

        p_truedived = p / Path('d', 'e')
        self.assertEqual(p_truedived, p_truth)

    def test__truediv__ep(self):
        """
        EP / EP
        :return:
        """
        p = EP('a', 'b', 'c')
        p_truth = EP('a', 'b', 'c', 'd', 'e')

        p_truedived = p / EP('d', 'e')
        self.assertEqual(p_truedived, p_truth)

    # --------------------------------------------------------------------------------
    #                           __rtruediv__(self, other)
    # --------------------------------------------------------------------------------

    def test__rtruediv__string(self):
        """
        Test the truedivition
        :return:
        """
        p = EP('a', 'b', 'c')
        p_truth = EP('yz', 'a', 'b', 'c')

        p_truedived = 'yz' / p
        self.assertEqual(p_truedived, p_truth)

    def test__rtruediv__path(self):
        """
        test EP / Path
        :return:
        """
        p = EP('a', 'b', 'c')
        p_truth = EP('y', 'z', 'a', 'b', 'c')

        p_truedived = Path('y', 'z') // p
        self.assertEqual(p_truedived, p_truth)

    def test__rtruediv__ep(self):
        """
        EP / EP
        :return:
        """
        p = EP('a', 'b', 'c')
        p_truth = EP('y', 'z', 'a', 'b', 'c')

        p_truedived = EP('y', 'z') / p
        self.assertEqual(p_truedived, p_truth)

    # --------------------------------------------------------------------------------
    #                           __itruediv__(self, other)
    # --------------------------------------------------------------------------------

    def test__itruediv__string(self):
        """
        Test the itruedivition
        :return:
        """
        p = EP('a', 'b', 'c')
        p_truth = EP('a', 'b', 'c', 'de')

        p /= 'de'
        self.assertEqual(p, p_truth)

    def test__itruediv__path(self):
        """
        test EP / Path
        :return:
        """
        p = EP('a', 'b', 'c')
        p_truth = EP('a', 'b', 'c', 'd', 'e')

        p /= Path('d', 'e')
        self.assertEqual(p, p_truth)

    def test__itruediv__ep(self):
        """
        EP / EP
        :return:
        """
        p = EP('a', 'b', 'c')
        p_truth = EP('a', 'b', 'c', 'd', 'e')

        p /= EP('d', 'e')
        self.assertEqual(p, p_truth)

    # --------------------------------------------------------------------------------
    #                           append(self, other)
    # --------------------------------------------------------------------------------

    def test_append_string(self):
        """
        Test the itruedivition
        :return:
        """
        p = EP('a', 'b', 'c')
        p_truth = EP('a', 'b', 'c', 'de')

        p.append('de')
        self.assertEqual(p, p_truth)

    def test_append_path(self):
        """
        test EP / Path
        :return:
        """
        p = EP('a', 'b', 'c')
        p_truth = EP('a', 'b', 'c', 'd', 'e')

        p.append(Path('d', 'e'))
        self.assertEqual(p, p_truth)

    def test_append_ep(self):
        """
        EP / EP
        :return:
        """
        p = EP('a', 'b', 'c')
        p_truth = EP('a', 'b', 'c', 'd', 'e')

        p.append(EP('d', 'e'))
        self.assertEqual(p, p_truth)

    # --------------------------------------------------------------------------------
    #                           extend(self, other)
    # --------------------------------------------------------------------------------

    def test_extend_string(self):
        """
        Test the itruedivition
        :return:
        """
        p = EP('a', 'b', 'c')
        p_truth = EP('a', 'b', 'c', 'd', 'e')

        p.extend(['d', 'e'])
        self.assertEqual(p, p_truth)

    def test_extend_path(self):
        """
        test EP / Path
        :return:
        """
        p = EP('a', 'b', 'c')
        p_truth = EP('a', 'b', 'c', 'd', 'e', 'f', 'g')

        p.extend(Path('d', 'e'), Path('f', 'g'))
        self.assertEqual(p, p_truth)

    def test_extend_ep(self):
        """
        EP / EP
        :return:
        """
        p = EP('a', 'b', 'c')
        p_truth = EP('a', 'b', 'c', 'd', 'e', 'f', 'g')

        p.extend([EP('d', 'e'), EP('f')], EP('g'))
        self.assertEqual(p, p_truth)


if __name__ == '__main__':
    unittest.main()


