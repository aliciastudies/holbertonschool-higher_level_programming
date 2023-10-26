import unittest

from models.base import Base


class TestBase (unittest.TestCase):
    """
    Test cases for Base
    """
    def test_assign_id(self):
        """
        Test if Base assigns unique ID
        """
        b0 = Base()
        b1 = Base()
        self.assertNotEqual(b0.id, b1.id)

    def test_assign_next_id(self):
        """
        Test if Base assigns id that is +1 from previous id (if is exists)
        """
        b0 = Base()
        b1 = Base()
        b2 = Base()
        self.assertEqual(b0.id + 1, b1.id)
        self.assertEqual(b1.id + 1, b2.id)
