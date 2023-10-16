import unittest

from models.base import Base


class TestBaseClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base0 = Base(None)
        cls.base1 = Base()
        cls.base2 = Base(98)
        cls.base3 = Base()

    def test_init_no_id(self):
        self.assertTrue(isinstance(self.base0, Base))

    def test_init_id(self):
        self.assertTrue(isinstance(self.base2, Base))

    def test_id_increment(self):
        self.assertEqual(self.base0.id, 1)

    def test_id_increment_again(self):
        self.assertEqual(self.base1.id, 2)

    def test_id_no_increment(self):
        self.assertEqual(self.base2.id, 98)

    def test_to_json_string(self):
        self.assertEqual(
            self.base0.to_json_string(
                [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}],
            ),
            '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]',
        )

    def test_from_json_string(self):
        self.assertEqual(
            self.base0.from_json_string(
                '[{"x": 2, "width": 10, "id": 1, "height": 7, \
                "y": 8}, {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]'
            ),
            [
                {"x": 2, "width": 10, "id": 1, "height": 7, "y": 8},
                {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4},
            ],
        )
