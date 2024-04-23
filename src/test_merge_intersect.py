import unittest
import merge_intersect

class TestMergeIntersect(unittest.TestCase):
    def test_merge_intersect(self):
        A = [ merge_intersect.Interval(chrm='1', start=1,  end=4),
              merge_intersect.Interval(chrm='1', start=5,  end=12),
              merge_intersect.Interval(chrm='1', start=6,  end=7),
              merge_intersect.Interval(chrm='1', start=10, end=11)]
        B = [ merge_intersect.Interval(chrm='1', start=2,  end=3),
              merge_intersect.Interval(chrm='1', start=4,  end=5),
              merge_intersect.Interval(chrm='1', start=8,  end=9) ]

        result = merge_intersect.merge_intersect(A, B)

        self.assertTrue( set((A[0], B[0])) in result)
        self.assertTrue( set((A[0], B[1])) in result)
        self.assertTrue( set((A[1], B[1])) in result)
        self.assertTrue( set((A[1], B[2])) in result)

        self.assertTrue( set((A[0], B[2])) not in result)

if __name__ == '__main__':
    unittest.main()

