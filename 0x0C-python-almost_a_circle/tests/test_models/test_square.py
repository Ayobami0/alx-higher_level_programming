import unittest

from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestBaseClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.square0 = Square(3, 5)
        cls.square1 = Square(1, 5, 0, 0)
        cls.square2 = Square(10, 10, id=94)
        cls.square3 = Square(5, 3, 5)
        cls.square4 = Square(8, 3, 8, 98)

    def test_init_no_id(self):
        self.assertTrue(isinstance(self.square0, Square))

    def test_init_id(self):
        self.assertTrue(isinstance(self.square2, Square))

    def test_inherited_base(self):
        self.assertTrue(isinstance(self.square0, Base))

    def test_inherited_rect(self):
        self.assertTrue(isinstance(self.square0, Rectangle))

    def test_correct_size(self):
        self.assertEqual(self.square4.size, 8)

    def test_correct_width(self):
        self.assertEqual(self.square4.width, 8)

    def test_correct_height(self):
        self.assertEqual(self.square4.height, 8)

    def test_correct_x_pos(self):
        self.assertEqual(self.square4.x, 3)

    def test_correct_y_pos(self):
        self.assertEqual(self.square4.y, 8)

    def test_incorrect_size_type(self):
        self.assertRaises(TypeError, lambda: Square(None))

    def test_size_less_or_equal_zero(self):
        self.assertRaises(ValueError, lambda: Square(0))

    def test_incorrect_x_pos_type(self):
        self.assertRaises(TypeError, lambda: Square(1, x="tis is a string"))

    def test_incorrect_y_pos_type(self):
        self.assertRaises(TypeError, lambda: Square(1, y=None))

    def test_x_pos_less_zero(self):
        self.assertRaises(ValueError, lambda: Square(1, x=-1))

    def test_y_pos_less_zero(self):
        self.assertRaises(ValueError, lambda: Square(1, y=-90))

    def test_update_args(self):
        self.square2.update(10, 10, 10, 10)
        self.assertEqual(
            str(self.square2),
            "[Square] (10) 10/10 - 10",
        )

    def test_update_kwargs(self):
        previous_val = str(self.square2)
        self.square2.update(
            **{"y": 0, "x": 0, "id": 2, "size": 4},
        )
        self.assertEqual(str(self.square2), "[Square] (2) 0/0 - 4")
        self.assertNotEqual(previous_val, str(self.square2))

    def test_create_kwargs(self):
        new_rect = self.square2.create(**{"y": 0, "x": 0, "id": 2, "size": 4})
        self.assertEqual(str(new_rect), "[Square] (2) 0/0 - 4")

    def test_to_dict(self):
        self.assertEqual(
            self.square4.to_dictionary(),
            {"y": 8, "x": 3, "size": 8, "id": 98},
        )

    def test_area(self):
        self.assertEqual(Square(10, 20).area(), 100)

    def test_to_json_string(self):
        self.assertEqual(
            self.square0.to_json_string(
                [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}],
            ),
            '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]',
        )

    def test_from_json_string(self):
        self.assertEqual(
            self.square0.from_json_string(
                '[{"x": 2, "size": 10, "id": 1, \
                "y": 8}, {"y": 0, "x": 0, "id": 2, "size": 2}]'
            ),
            [
                {"x": 2, "size": 10, "id": 1, "y": 8},
                {"y": 0, "x": 0, "id": 2, "size": 2},
            ],
        )
