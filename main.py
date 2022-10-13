import json
from utils import type_checker, validate_filepath
from constants import num_to_words


class SniffSchema(object):
    def __init__(self, input_filepath, output_filepath):
        self.input_file_path = input_filepath
        self.output_file_path = output_filepath

    def json_type_converter(self):
        if validate_filepath(self.input_file_path) and validate_filepath(
            self.output_file_path
        ):
            with open(self.input_file_path) as input_data:
                data = json.load(input_data)
                attribute = data.get("message", {})
                output = {}
                attr_index = 0
                if attribute != {}:
                    for _, value in attribute.items():
                        attr_index += 1
                        output[f"key_{num_to_words[attr_index]}"] = {
                            "type": type_checker(value),
                            "tag": "",
                            "description": "",
                            "required": False,
                        }
                    output_data = json.dumps(output, indent=4)
                    with open(self.output_file_path, "w") as result:
                        result.write(output_data)
        else:
            return {}


instance1 = SniffSchema("data/data_2.json", "schema/schema_2.json")
instance2 = SniffSchema("data/data_1.json", "schema/schema_1.json")

instance1.json_type_converter()
instance2.json_type_converter()
