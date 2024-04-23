import unittest
import ucsc_db


class TestBinFunctions(unittest.TestCase):
    def test_get_bin(self):
        j = 0
        for i in range(0, 512000000, 128000):
            ucsc_bin = ucsc_db.get_bin(i+10, i+128000//2)
            self.assertEqual(ucsc_bin, j)
            j+=1

        for i in range(128000, 512000000, 128000):
            if (i-10)//1000000 != (i+128000//2)//1000000: continue
            ucsc_bin = ucsc_db.get_bin(i-10, i+128000//2)
            self.assertEqual(ucsc_bin, 512000000//128000 + i//1000000)

    def test_get_query_bins(self):

        target_bins =[0, 4000, 4512, 4576, 4584]
        ucsc_bins = ucsc_db.get_query_bins(10, 128000//2)
        self.assertEqual(ucsc_bins, target_bins)

        target_bins =[0, 1, 4000, 4512, 4576, 4584]
        ucsc_bins = ucsc_db.get_query_bins(10, 128000+10)
        self.assertEqual(ucsc_bins, target_bins)

        target_bins = [0, 1, 2, 3, 4, 5, 6, 7, 4000, 4001, 4512, 4576, 4584]
        ucsc_bins = ucsc_db.get_query_bins(10, 1000001)
        self.assertEqual(ucsc_bins, target_bins)


if __name__ == '__main__':
    unittest.main()
