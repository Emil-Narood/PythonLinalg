import unittest
from src.lib import vector2D as v2d
from src.lib import vector3D as v3d

class MyTestCase(unittest.TestCase):
    def test_add(self):
        a = [5, 3]
        b = [4, 2]
        c = v2d.add2D(a, b)
        expected_result = [9, 5]
        self.assertEqual(c, expected_result)
    def test_add3D



if __name__ == '__main__':
    unittest.main()
