import unittest

from models.rectangle import Rectangle
from models.base import Base


class TestBaseClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rectangle0 = Rectangle(3, 5)
        cls.rectangle1 = Rectangle(1, 5, 0, 0)
        cls.rectangle2 = Rectangle(10, 10, id=94)
        cls.rectangle3 = Rectangle(5, 3, 5)
        cls.rectangle4 = Rectangle(8, 3, 8, 5, 98)

    def test_init_no_id(self):
        self.assertTrue(isinstance(self.rectangle0, Rectangle))

    def test_init_id(self):
        self.assertTrue(isinstance(self.rectangle2, Rectangle))

    def test_inherited_base(self):
        self.assertTrue(isinstance(self.rectangle0, Base))

    def test_id_increment(self):
        self.assertEqual(self.rectangle0.id, 4)

    def test_id_increment_again(self):
        self.assertEqual(self.rectangle1.id, 5)

    def test_id_no_increment(self):
        self.assertEqual(self.rectangle4.id, 98)

    def test_correct_width(self):
        self.assertEqual(self.rectangle4.width, 8)

    def test_correct_height(self):
        self.assertEqual(self.rectangle4.height, 3)

    def test_correct_x_pos(self):
        self.assertEqual(self.rectangle4.x, 8)

    def test_correct_y_pos(self):
        self.assertEqual(self.rectangle4.y, 5)

    def test_incorrect_width_type(self):
        self.assertRaises(TypeError, lambda: Rectangle(None, 1))

    def test_incorrect_height_type(self):
        self.assertRaises(TypeError, lambda: Rectangle(2, True))

    def test_width_less_or_equal_zero(self):
        self.assertRaises(ValueError, lambda: Rectangle(0, 1))

    def test_height_less_or_equal_zero(self):
        self.assertRaises(ValueError, lambda: Rectangle(2, 0))

    def test_incorrect_x_pos_type(self):
        self.assertRaises(TypeError, lambda: Rectangle(1, 2, x="tis is a string"))

    def test_incorrect_y_pos_type(self):
        self.assertRaises(TypeError, lambda: Rectangle(1, 2, y=None))

    def test_x_pos_less_zero(self):
        self.assertRaises(ValueError, lambda: Rectangle(1, 2, x=-1))

    def test_y_pos_less_zero(self):
        self.assertRaises(ValueError, lambda: Rectangle(1, 2, y=-90))

    def test_update_args(self):
        self.rectangle2.update(10, 10, 10, 10, 10)
        self.assertEqual(
            str(self.rectangle2),
            "[Rectangle] (10) 10/10 - 10/10",
        )

    def test_update_kwargs(self):
        previous_val = str(self.rectangle2)
        self.rectangle2.update(
            **{"y": 0, "x": 0, "id": 2, "width": 2, "height": 4},
        )
        self.assertEqual(str(self.rectangle2), "[Rectangle] (2) 0/0 - 2/4")
        self.assertNotEqual(previous_val, str(self.rectangle2))

    def test_create_kwargs(self):
        new_rect = self.rectangle2.create(
            **{"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}
        )
        self.assertEqual(str(new_rect), "[Rectangle] (2) 0/0 - 2/4")

    def test_to_dict(self):
        self.assertEqual(
            self.rectangle4.to_dictionary(),
            {"width": 8, "height": 3, "x": 8, "y": 5, "id": 98},
        )

    def test_area(self):
        self.assertEqual(Rectangle(10, 20).area(), 200)

    def test_to_json_string(self):
        self.assertEqual(
            self.rectangle0.to_json_string(
                [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}],
            ),
            '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]',
        )

    def test_from_json_string(self):
        self.assertEqual(
            self.rectangle0.from_json_string(
                '[{"x": 2, "width": 10, "id": 1, "height": 7, \
                "y": 8}, {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]'
            ),
            [
                {"x": 2, "width": 10, "id": 1, "height": 7, "y": 8},
                {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4},
            ],
        )
