from Organize import Organize, MyException
from unittest import TestCase

class TestOrganize(TestCase):
    obj = None

    def test_insert(self):
        """Insert testing cases
        """
        self.obj = Organize()
        self.obj.insert('343GuiltySparks')
        self.obj.insert('2 Steaks')
        self.obj.insert('10 Chicken Winds')
        self.obj.insert('10 umbrella')
        self.assertIn('GuiltySparks', self.obj.search(343), 'key is not in container')
        self.assertIn('Steaks', self.obj.search(2), 'key is not in container')
        self.assertIn('Chicken Winds', self.obj.search(10), 'key is not in container')
        self.assertIn('umbrella', self.obj.search(10), 'key is not in container')

    def test_insertExcption(self):
        """Insert Exception raises testing
        """
        self.obj = Organize()
        self.assertRaises(MyException, self.obj.insert, None)
        self.assertRaises(MyException, self.obj.insert, '')

    def test_valuesSorted(self):
        """Check if everything is sorted alphabetically
        """
        self.obj = Organize()
        self.obj.insert('10 umbrella')
        self.obj.insert('10 Chicken Winds')
        self.obj.sort_shortWords(10)
        self.assertEqual(['Chicken Winds','umbrella'], self.obj.search(10))
        self.obj.insert('2 voting waistline')
        self.obj.insert('2 hill')
        self.obj.insert('2 side')
        self.obj.insert('2 jungle psychology')
        self.obj.insert('2 Steaks')
        self.obj.insert('2 test')
        self.assertNotEqual(['hill', 'jungle psychology', 'side', 'Steaks', 'test', 'voting waistline'], self.obj.search(2))
        self.obj.sort_shortWords(2)
        self.assertEqual(['hill', 'jungle psychology', 'side', 'Steaks', 'test', 'voting waistline'], self.obj.search(2))

    def test_search(self):
        """Validates the search function is returning the right short strings
        """
        self.obj = Organize()
        self.obj.insert('343GuiltySparks')
        self.obj.insert('343 guardsman')
        self.obj.insert('2 side')
        self.assertEqual(['GuiltySparks','guardsman'], self.obj.search(343))
        self.assertEqual(['side'], self.obj.search(2))
        self.assertIsNone(self.obj.search(10))