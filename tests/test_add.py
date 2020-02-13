import unittest
from EpicPath import EpicPath as EP
from pathlib import Path


class Add(unittest.TestCase):
    """
    Tests the library EpicPath
    """

    # --------------------------------------------------------------------------------
    #                           __add__(self, other)
    # --------------------------------------------------------------------------------

    def test__add__string(self):
        """
        Test the addition
        :return:
        """
        p = EP('a', 'b', 'c')
        p_truth = EP('a', 'b', 'cde')

        p_added = p + 'de'
        self.assertEqual(p_added, p_truth)

    def test__add__path(self):
        """
        test EP + Path
        :return:
        """
        p = EP('a', 'b', 'c')
        p_truth = EP('a', 'b', 'cde')

        p_added = p + Path('de')
        self.assertEqual(p_added, p_truth)

    def test__add__ep(self):
        """
        EP + EP
        :return:
        """
        p = EP('a', 'b', 'c')
        p_truth = EP('a', 'b', 'cde')

        p_added = p + EP('de')
        self.assertEqual(p_added, p_truth)

    # --------------------------------------------------------------------------------
    #                           __radd__(self, other)
    # --------------------------------------------------------------------------------

    def test__radd__string(self):
        """
        Test the addition
        :return:
        """
        p = EP('a', 'b', 'c')
        p_truth = EP('yza', 'b', 'c')

        p_added = 'yz' + p
        self.assertEqual(p_added, p_truth)

    def test__radd__path(self):
        """
        test EP + Path
        :return:
        """
        p = EP('a', 'b', 'c')
        p_truth = EP('yza', 'b', 'c')

        p_added = Path('yz') + p
        self.assertEqual(p_added, p_truth)

    def test__radd__ep(self):
        """
        EP + EP
        :return:
        """
        p = EP('a', 'b', 'c')
        p_truth = EP('yza', 'b', 'c')

        p_added = EP('yz') + p
        self.assertEqual(p_added, p_truth)

    # --------------------------------------------------------------------------------
    #                           __iadd__(self, other)
    # --------------------------------------------------------------------------------

    def test__iadd__string(self):
        """
        Test the iaddition
        :return:
        """
        p = EP('a', 'b', 'c')
        p_truth = EP('a', 'b', 'cde')

        p += 'de'
        self.assertEqual(p, p_truth)

    def test__iadd__path(self):
        """
        test EP + Path
        :return:
        """
        p = EP('a', 'b', 'c')
        p_truth = EP('a', 'b', 'cde')

        p += Path('de')
        self.assertEqual(p, p_truth)

    def test__iadd__ep(self):
        """
        EP + EP
        :return:
        """
        p = EP('a', 'b', 'c')
        p_truth = EP('a', 'b', 'cde')

        p += EP('de')
        self.assertEqual(p, p_truth)

    # --------------------------------------------------------------------------------
    #                           add(self, other)
    # --------------------------------------------------------------------------------

    def test_add_string(self):
        """
        Test the iaddition
        :return:
        """
        p = EP('a', 'b', 'c')
        p_truth = EP('a', 'b', 'cde')

        p.add('de')
        self.assertEqual(p, p_truth)

    def test_add_path(self):
        """
        test EP + Path
        :return:
        """
        p = EP('a', 'b', 'c')
        p_truth = EP('a', 'b', 'cde')

        p.add(Path('de'))
        self.assertEqual(p, p_truth)

    def test_add_ep(self):
        """
        EP + EP
        :return:
        """
        p = EP('a', 'b', 'c')
        p_truth = EP('a', 'b', 'cde')

        p.add(EP('de'))
        self.assertEqual(p, p_truth)


if __name__ == '__main__':
    unittest.main()
