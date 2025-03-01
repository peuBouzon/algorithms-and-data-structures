from unittest import TestCase, main
from selection import sort
class TestSorte(TestCase):
    def test_sort(self):
        self.assertEqual(sort([3, 2, 1]), [1, 2, 3])

if __name__ == '__main__':
    main()