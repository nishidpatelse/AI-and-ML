import unittest
from fleet_agent.maintenance import is_oil_change_due, is_tire_change_due

class TestMaintenance(unittest.TestCase):
    def test_oil_change_due(self):
        self.assertTrue(is_oil_change_due(10000, 4000))
        self.assertFalse(is_oil_change_due(9000, 5000))

    def test_tire_change_due(self):
        self.assertTrue(is_tire_change_due(20000, 9000))
        self.assertFalse(is_tire_change_due(15000, 6000))

if __name__ == '__main__':
    unittest.main()
