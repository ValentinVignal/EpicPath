import unittest
from EpicPath import EpicPath as EP


class EpicPath(unittest.TestCase):
    """
    Tests the library EpicPath
    """
    def test_add(self):
        """
        Test the addition
        :return:
        """
        p = EP('a', 'b', 'c')

        p_added = p + 'de'
        p_truth = EP('a', 'b', 'cde')
        self.assertEqual(p_added.str, p_truth.str)

        p_radded = 'yz' + p
        p_rtruth = EP('yza', 'b', 'c')
        self.assertEqual(p_rtruth.str, p_radded.str)

        p2 = EP('d', 'e', 'f')
        p_added_parts = EP.add_parts(p, p2)
        p_added_parts_truth = ('a', 'b', 'cd', 'e', 'f')
        self.assertEqual(p_added_parts, p_added_parts_truth)


if __name__ == '__main__':
    unittest.main()