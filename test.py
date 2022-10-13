import json
import unittest
from main import SniffSchema


class TestSniffJson(unittest.TestCase):
    def validate(self, key, type):
        """recieves key and data type to be chekced as parameters"""
        instance = SniffSchema("test_data/test_data.json", "test_data/data_output.json")
        instance.json_type_converter()
        # value__mapper('test_data/string_test.json', 'test_data/string_output.json')
        with open("test_data/data_output.json") as file:
            result = json.load(file)[key]
            self.assertEqual(result["type"], type)

    def test_string(self):
        """test to check string type"""
        self.validate(key="key_one", type="string")

    def test_integer(self):
        """test to check integer type"""

        self.validate(key="key_two", type="integer")

    def test_invalid_enum(self):
        """test to check invalid enum type"""

        self.validate(key="key_three", type=None)

    def test_valid_enum(self):
        """test to check valid enum type"""

        self.validate(key="key_four", type="enum")

    def test_valid_array(self):
        """test to check array type"""

        self.validate(key="key_five", type="array")

    def test_boolean(self):
        """test to check boolean type"""

        self.validate(key="key_six", type=None)


if __name__ == "__main__":
    unittest.main()
